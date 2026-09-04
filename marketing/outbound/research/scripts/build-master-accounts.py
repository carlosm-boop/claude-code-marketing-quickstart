import csv, os, re, sys
from collections import defaultdict, Counter

D = os.path.expanduser("~/mnt/claude-code-marketing-quickstart/marketing/outbound/research")
DATA = os.path.join(D, "data")
HAND = os.path.expanduser("~/mnt/claude-code-marketing-quickstart/handoffs")

def norm(d):
    d = (d or "").strip().lower()
    d = re.sub(r"^https?://", "", d)
    d = re.sub(r"^www\.", "", d)
    return d.split("/")[0].strip()

def rd(p):
    return list(csv.DictReader(open(p, encoding="utf-8-sig")))

POINTS = {"EST":25, "MRG":20, "HIR":15, "MDB":15}
CREDIT = {"●":1.0, "◐":0.5, "◑":0.5,
          "○":0.0, "?":0.0, "⊗":0.0, "⊘":0.0, "✕":0.0}

# ---- 1. roster (canonical)
roster, seen = {}, set()
for ln in open(os.path.join(D,"0926-target-accounts.md"),encoding="utf-8").read().split("\n"):
    if not ln.strip().startswith("|") or "VER" not in ln: continue
    c = [x.strip() for x in ln.strip().strip("|").split("|")]
    if len(c) < 5: continue
    m = re.search(r"\*\*(.+?)\*\*\s*·\s*`(.+?)`", c[0])
    if not m: continue
    dom = norm(m.group(2))
    if dom in seen: continue
    seen.add(dom)
    roster[dom] = {"company": m.group(1).strip(),
        "marks": dict(re.findall(r"(VER|AGE|SCL|VOL|EST|MRG|HIR|ACC|MDB)(.)", c[3].strip("` "))),
        "notes": c[4] if len(c)>4 else "", "cohort": c[5] if len(c)>5 else ""}
print("roster parsed:", len(roster), file=sys.stderr)

# ---- 2. EST/HIR pull + date windows
est44 = {norm(r["Domain"]): r for r in rd(os.path.join(DATA,"0926-est-hir-results-44.csv"))}
DATED = os.path.expanduser("~/mnt/claude-code-marketing-quickstart/Claude outputs/0926-est-hir-results-44-dated.csv")
est44d = {norm(r["Domain"]): r for r in rd(DATED)}
def dated(d):
    """(iso date of the qualifying posting, sentence, pain_12m, pain_all, postings, reqs)"""
    r = est44d.get(d)
    if not r: return ("", "", "", "", "", "")
    ev = (r.get("EST Evidence (dated)") or "").strip()
    m = re.match(r"^(\d{4}-\d{2}-\d{2})\s*\|\s*(.*)$", ev, re.S)
    iso, sent = (m.group(1), m.group(2).strip()) if m else ("", ev)
    return (iso, sent, r.get("Pain postings (12m)","").strip(),
            r.get("Pain postings (all time)","").strip(),
            r.get("Postings","").strip(), r.get("Requisitions","").strip())
print("dated EST/HIR rows:", len(est44d), file=sys.stderr)
dates, pulls = defaultdict(list), defaultdict(set)
for r in rd(os.path.join(DATA,"0926-origami-job-postings.csv")):
    d = norm(r.get("Domain")); dp = (r.get("Date Posted") or "").strip()[:10]
    if d and re.match(r"^\d{4}-\d{2}-\d{2}$", dp): dates[d].append(dp)
    if d and (r.get("Pull") or "").strip(): pulls[d].add(r["Pull"].strip())
NO_DATES = ("DATES NOT IN REPO - the 949-row EST/HIR corpus behind these marks was "
            "never committed; only its per-domain aggregate was. Request "
            "0926-est-hir-results-44-dated.csv from workstream 1.")
def window(d):
    iso, _, p12, pall, npost, nreq = dated(d)
    if d in est44d:
        if iso:
            return f"qualifying posting {iso}; {p12} pain postings in 12m of {pall} all-time, across {nreq} requisitions"
        return f"no qualifying posting; {npost} postings / {nreq} requisitions searched"
    v = sorted(dates.get(d,[]))
    if v: return f"{v[0]}..{v[-1]} (n={len(v)} postings in repo)"
    return NO_DATES if d in est44 else ""

# ---- 3. MongoDB enrichment
mdb = {norm(r["Domain"]): r for r in rd(os.path.join(DATA,"0926-mongodb-status-39-accounts.csv"))}

# ---- 4. firmographics (first non-empty wins)
firmo = {}
def put(d, **kw):
    cur = firmo.setdefault(d, {})
    for k,v in kw.items():
        if v and not cur.get(k): cur[k] = v
for r in rd(os.path.join(DATA,"0926-origami-companies.csv")):
    d = norm(r.get("Domain"))
    if d: put(d, company=r.get("Company"), founded=r.get("Founded Year"),
              employees=r.get("Employee Count"), ownership=r.get("Ownership Type"),
              round=r.get("Funding Stage"), funding=r.get("Total Funding"),
              hq=r.get("HQ Location"), industry=r.get("Industry"))

# ---- 5. populations
islands = defaultdict(set)
for d in roster: islands[d].add("roster-31")
fresh = {}
for r in rd(os.path.join(DATA,"0926-c1-fresh-pull-graded.csv")):
    if r["Verdict"].strip().upper() != "KEEP": continue
    d = norm(r.get("Domain"))
    if not d: continue
    fresh[d] = r; islands[d].add("c1-fresh-pull-56")
    put(d, company=r.get("Company"), founded=r.get("Founded Year"), employees=r.get("Employee Count"),
        ownership=r.get("Ownership Type"), round=r.get("Latest Round"),
        funding=r.get("Total Funding"), hq=r.get("Headquarters"), industry=r.get("Industry Label"))
consol = {}
for r in rd(os.path.join(DATA,"0926-new-accounts-for-roster.csv")):
    d = norm(r.get("domain"))
    if not d: continue
    consol[d] = r; islands[d].add("consolidation-19")
    put(d, company=r.get("company"), founded=r.get("founded"), employees=r.get("employees"),
        ownership=r.get("ownership"), round=r.get("stage"), funding=r.get("funding"),
        hq=r.get("hq"), industry=r.get("type"))
costtest = {}
ct = open(os.path.join(HAND,"0926-costtest-graded-accounts.md"),encoding="utf-8").read().split("\n")
for ln in ct[:38]:
    if not ln.strip().startswith("|"): continue
    c = [x.strip() for x in ln.strip().strip("|").split("|")]
    if len(c) < 8 or c[0] in ("Company","") or set(c[0]) <= set("-: "): continue
    d = norm(c[1])
    if not d or "." not in d: continue
    costtest[d] = c; islands[d].add("cost-test-9")
    put(d, company=c[0], founded=c[2], employees=c[3].replace(",",""),
        funding=c[4], ownership=c[5], hq=c[6])
for d,nm in (("vinted.com","Vinted"),("shiftkey.com","ShiftKey")):
    islands[d].add("c1-gated-CHAT-ONLY"); put(d, company=nm)
print(f"fresh {len(fresh)} consol {len(consol)} costtest {len(costtest)} union {len(islands)}", file=sys.stderr)

PE = ("PRIVATE_EQUITY","POST_IPO")
def resolve(d):
    r, e, o = roster.get(d), est44.get(d), {}
    # EST
    if r and "EST" in r["marks"]:
        o["est_mark"]="EST"+r["marks"]["EST"]
        o["est_retrieval"]="job-postings pull, 44 domains, 12-month window" if d in est44d else (("job-postings pull ("+"+".join(sorted(pulls.get(d,[])))+")") if d in est44 else "roster hand-read, pre-pull")
        o["est_window"]=window(d); o["est_sentence"]=dated(d)[1] or (e or {}).get("EST Evidence","").strip()
    elif d in est44d:
        o["est_mark"]=est44d[d]["EST"].split(" ")[0]
        o["est_retrieval"]="job-postings pull, 44 domains, 12-month window"
        o["est_window"]=window(d); o["est_sentence"]=dated(d)[1] or e.get("EST Evidence","").strip()
    else:
        o["est_mark"]="EST?"; o["est_retrieval"]="NOT RETRIEVED"; o["est_window"]=""; o["est_sentence"]=""
    # HIR
    if r and "HIR" in r["marks"]:
        o["hir_mark"]="HIR"+r["marks"]["HIR"]
        o["hir_retrieval"]="job-postings pull, 44 domains, recency-windowed" if d in est44d else "roster hand-read, pre-pull"
        o["hir_window"]=window(d)
    elif d in est44d:
        o["hir_mark"]=est44d[d]["HIR"].split(" ")[0]; o["hir_retrieval"]="job-postings pull, 44 domains, recency-windowed"; o["hir_window"]=window(d)
    elif d in fresh:
        b = fresh[d]["Infra/SRE Posting"].strip().lower()
        o["hir_mark"]="HIR●" if b=="true" else "HIR?"
        o["hir_retrieval"]="Origami search-time Infra/SRE boolean (derived; probe-validated 0/10 false negatives 2026-09-04)"
        o["hir_window"]="search-time snapshot, no date range"
    else:
        o["hir_mark"]="HIR?"; o["hir_retrieval"]="NOT RETRIEVED"; o["hir_window"]=""
    # MDB
    if r and "MDB" in r["marks"]: o["mdb_mark"]="MDB"+r["marks"]["MDB"]
    elif d in mdb: o["mdb_mark"]="MDB●" if mdb[d].get("MongoDB","").lower()=="yes" else "MDB○"
    else: o["mdb_mark"]="MDB?"
    if d in mdb:
        o["mdb_retrieval"]="MongoDB enrichment: "+((mdb[d].get("MongoDB Evidence") or "").strip() or "no evidence string")
    elif d in est44 and (est44[d].get("Databases Named") or "").strip():
        o["mdb_retrieval"]="job-posting database mentions: "+est44[d]["Databases Named"].strip()
    else:
        o["mdb_retrieval"]="NOT RETRIEVED"
    # MRG
    f = firmo.get(d,{}); blob = ((f.get("ownership") or "")+" "+(f.get("round") or "")).upper()
    ispe = any(t in blob for t in PE)
    if r and "MRG" in r["marks"]: o["mrg_mark"]="MRG"+r["marks"]["MRG"]
    elif ispe: o["mrg_mark"]="MRG●"
    else: o["mrg_mark"]="MRG?"
    if ispe: o["mrg_retrieval"]="Origami firmographics: "+(f.get("round") or f.get("ownership") or "")
    elif f.get("round"): o["mrg_retrieval"]="funding stage only ("+f["round"]+") - capital gate passed by construction, not a margin event"
    else: o["mrg_retrieval"]="NOT RETRIEVED"
    _i,_s,_p12,_pall,_np,_nr = dated(d)
    o["est_pain_postings_12m"]=_p12; o["est_pain_postings_alltime"]=_pall
    o["postings_searched"]=_np; o["requisitions_searched"]=_nr
    for g in ("VER","AGE","SCL","ACC"):
        o[g.lower()+"_gate"] = (g+r["marks"][g]) if (r and g in r["marks"]) else g+"?"
    return o

def score_tier(row):
    """Points earned, plus the ceiling the account can still reach given what has
    actually been retrieved. A signal that was never retrieved is UNKNOWN: it scores
    zero AND it lowers the ceiling. Reporting only the score would present an
    unmeasured account as a measured-and-weak one, which is the defect this whole
    file exists to stop."""
    tot, ceil, miss = 0.0, 0.0, []
    for s in ("EST","MRG","HIR","MDB"):
        mk = row[s.lower()+"_mark"]; gl = mk[len(s):] or "?"
        tot += POINTS[s]*CREDIT.get(gl,0.0)
        if row[s.lower()+"_retrieval"]=="NOT RETRIEVED":
            miss.append(s)
        else:
            ceil += POINTS[s]
    tier = "1" if tot>=56.25 else "2" if tot>=37.5 else "3"
    if ceil < 37.5:
        conf = f"UNSCOREABLE - ceiling {ceil:g}, below the Tier 2 line"
        tier = "UNSCORED"
    elif ceil < 56.25:
        conf = f"CANNOT REACH TIER 1 - ceiling {ceil:g}"
    elif miss:
        conf = f"PROVISIONAL - ceiling {ceil:g}"
    else:
        conf = "FIRM - all four signals retrieved"
    return round(tot,2), tier, ";".join(miss), round(ceil,2), conf

FIELDS = ["domain","company","tier","tier_confidence","score_75","score_ceiling","unretrieved_signals","evidence_tier",
  "est_mark","est_retrieval","est_window","est_sentence","est_pain_postings_12m","est_pain_postings_alltime","postings_searched","requisitions_searched","hir_mark","hir_retrieval","hir_window",
  "mdb_mark","mdb_retrieval","mrg_mark","mrg_retrieval","ver_gate","age_gate","scl_gate","acc_gate",
  "cohort","founded_year","employees","ownership_type","latest_round","total_funding","hq","industry",
  "source_islands","notes"]

rows = []
for d in sorted(islands):
    f = firmo.get(d,{}); r = roster.get(d)
    row = {"domain":d, "company":(r or {}).get("company") or f.get("company") or "",
      "cohort":(r or {}).get("cohort",""), "notes":(r or {}).get("notes",""),
      "founded_year":f.get("founded",""), "employees":f.get("employees",""),
      "ownership_type":f.get("ownership",""), "latest_round":f.get("round",""),
      "total_funding":f.get("funding",""), "hq":f.get("hq",""), "industry":f.get("industry",""),
      "source_islands":";".join(sorted(islands[d]))}
    row.update(resolve(d))
    sc, tier, miss, ceil, conf = score_tier(row)
    row["score_75"] = sc
    row["score_ceiling"] = ceil
    row["tier"] = tier
    row["tier_confidence"] = conf
    row["unretrieved_signals"] = miss
    if row["est_mark"]=="EST●" and row["est_sentence"]:
        row["evidence_tier"]="A - named pain, sentence on file"
    elif row["est_retrieval"]!="NOT RETRIEVED":
        row["evidence_tier"]="B - estate measured, no qualifying sentence"
    else:
        row["evidence_tier"]="C - estate never retrieved; category line only"
    rows.append(row)

out = os.path.join(DATA,"0926-master-accounts.csv")
with open(out,"w",newline="",encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=FIELDS, extrasaction="ignore")
    w.writeheader(); w.writerows(rows)
print(f"\nwrote {out}: {len(rows)} rows", file=sys.stderr)
print("tier:", dict(Counter(r["tier"] for r in rows)), file=sys.stderr)
print("evidence:", dict(Counter(r["evidence_tier"][0] for r in rows)), file=sys.stderr)
print("confidence:", dict(Counter(r["tier_confidence"].split(" -")[0] for r in rows)), file=sys.stderr)
print("\nTier 1:", [r["company"] for r in rows if r["tier"]=="1"], file=sys.stderr)
print("\nTier 2:", [(r["company"], r["score_75"], r["tier_confidence"].split(" -")[0]) for r in rows if r["tier"]=="2"], file=sys.stderr)
print("islands:", dict(Counter(r["source_islands"] for r in rows)), file=sys.stderr)
