#!/usr/bin/env python3
"""Assemble The Systems Engineer's Path chapter fragments into one HTML file and render the PDF.

Same fragment-per-chapter toolchain as the rest of the series. This is a FIVE-VOLUME book kept in ONE
repo (like the bioinformatics book): volumes are sequential Part-groups; each Part's chapter ids are
generated sequentially. The deep-mastery + leadership companion to the data track (after Data Engineer,
Data Architect, and Algorithmic Thinker).

Volumes: 1 Systems Programming & Performance · 2 Database Internals (build a DB) · 3 Distributed Systems,
Deeply · 4 Security & Privacy Engineering · 5 The Staff/Principal Engineer & Tech Lead.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"
SOL = ROOT / "solutions"
APP = ROOT / "appendices"

# (volume label, part title, blurb, chapter count). Chapter ids are assigned sequentially across the
# whole book so build.py stays glob-ordered (chNN by filename). Counts are planning estimates.
_SPEC = [
    # ---- VOLUME 1 — Systems Programming & Performance ----
    ("Vol 1 · Systems Programming & Performance", "The Machine & the Cost Model",
     "What a program actually runs on: CPU, memory hierarchy, caches, and mechanical sympathy — the "
     "real cost model that the RAM abstraction hides.", 6),
    ("Vol 1 · Systems Programming & Performance", "C & Manual Memory",
     "Pointers, layout, the stack/heap, manual allocation, and undefined behavior — programming with no "
     "safety net so you understand the net.", 6),
    ("Vol 1 · Systems Programming & Performance", "The Operating System",
     "Processes, threads, scheduling, virtual memory, and the system-call boundary — how the OS "
     "multiplexes the machine.", 7),
    ("Vol 1 · Systems Programming & Performance", "Concurrency & Parallelism",
     "Threads, locks and their hazards, lock-free techniques, atomics, and the memory model that makes "
     "concurrent code correct (or not).", 7),
    ("Vol 1 · Systems Programming & Performance", "Rust for Systems",
     "Ownership, borrowing, and lifetimes — memory safety without a GC, and how the type system encodes "
     "the invariants the previous parts made you prove by hand.", 6),
    ("Vol 1 · Systems Programming & Performance", "Performance Engineering",
     "Measure before you optimize: profiling, benchmarking, cache-aware and data-oriented design, SIMD, "
     "and reasoning about where time actually goes.", 7),
    ("Vol 1 · Systems Programming & Performance", "I/O & Networking, Low-Level",
     "Files, sockets, blocking vs async, epoll/io_uring, zero-copy — the systems substrate under every "
     "data pipeline and service.", 6),
    # ---- VOLUME 2 — Database Internals ----
    ("Vol 2 · Database Internals (Build a Database)", "Storage & the Disk",
     "Pages, files, the buffer pool, and the storage manager — the foundation you build a database on.", 5),
    ("Vol 2 · Database Internals (Build a Database)", "Storage Engines",
     "B-trees and LSM-trees implemented and analyzed — the two families and when each wins.", 6),
    ("Vol 2 · Database Internals (Build a Database)", "Durability & Recovery",
     "Write-ahead logging, ARIES, checkpoints, and crash recovery — how a database keeps its promises "
     "across failures.", 6),
    ("Vol 2 · Database Internals (Build a Database)", "Transactions & Concurrency Control",
     "ACID, isolation levels and their anomalies, 2PL, MVCC, and OCC — correctness under concurrency, "
     "implemented.", 7),
    ("Vol 2 · Database Internals (Build a Database)", "Query Processing & Execution",
     "Parser, planner, physical operators, and execution models (Volcano/vectorized/codegen) — turning "
     "SQL into work.", 7),
    ("Vol 2 · Database Internals (Build a Database)", "Query Optimization",
     "Statistics, cardinality estimation, cost models, and join ordering — the optimizer, honestly.", 6),
    ("Vol 2 · Database Internals (Build a Database)", "Indexing & Access Methods",
     "Secondary/clustered/covering indexes, and specialized structures — the access-method layer.", 5),
    ("Vol 2 · Database Internals (Build a Database)", "[BUILD] A Working Database",
     "Assemble the pieces into a small but real relational engine — storage → txn → query → execute — "
     "with tests.", 5),
    ("Vol 2 · Database Internals (Build a Database)", "Toward Distributed Databases",
     "Sharding, replication, and the distributed-transaction problem — the bridge to Volume 3.", 5),
    # ---- VOLUME 3 — Distributed Systems, Deeply ----
    ("Vol 3 · Distributed Systems, Deeply", "Models & Foundations",
     "System and failure models, the FLP impossibility, time and clocks, causality and logical time — "
     "the formal ground.", 6),
    ("Vol 3 · Distributed Systems, Deeply", "Replication & Consistency",
     "Consistency models, linearizability, CAP/PACELC, and quorums — what 'consistent' actually means.", 6),
    ("Vol 3 · Distributed Systems, Deeply", "Consensus",
     "Paxos, Raft, and view-stamped replication (with a note on Byzantine fault tolerance) — agreement "
     "under failure.", 6),
    ("Vol 3 · Distributed Systems, Deeply", "Coordination & Transactions",
     "Leader election, distributed transactions, 2PC/3PC, and sagas — coordinating across nodes.", 6),
    ("Vol 3 · Distributed Systems, Deeply", "Replicated Data & Convergence",
     "Eventual consistency, anti-entropy, gossip, and CRDTs — converging without coordination.", 6),
    ("Vol 3 · Distributed Systems, Deeply", "Partitioning & Scale",
     "Consistent hashing, rebalancing, and hot-spot handling — spreading state and load.", 5),
    ("Vol 3 · Distributed Systems, Deeply", "Distributed Algorithms & Patterns",
     "Broadcast/ordering, failure detectors, distributed snapshots, and the patterns real systems use.", 5),
    ("Vol 3 · Distributed Systems, Deeply", "Formal Methods",
     "Specifying and model-checking a protocol with TLA+ — finding the bug before production does.", 5),
    ("Vol 3 · Distributed Systems, Deeply", "Building & Operating Distributed Systems",
     "From spec to a real, observable, testable distributed system — and operating it.", 5),
    # ---- VOLUME 4 — Security & Privacy Engineering ----
    ("Vol 4 · Security & Privacy Engineering", "Security Foundations & Threat Modeling",
     "The security mindset, threat modeling, trust boundaries, and reasoning about adversaries.", 5),
    ("Vol 4 · Security & Privacy Engineering", "Applied Cryptography",
     "Symmetric/asymmetric crypto, hashing, MACs, signatures, TLS, and key management — used correctly, "
     "not invented.", 7),
    ("Vol 4 · Security & Privacy Engineering", "Authentication & Authorization",
     "Identity, sessions, OAuth2/OIDC, access-control models, and zero-trust — who can do what.", 6),
    ("Vol 4 · Security & Privacy Engineering", "Software & Systems Security",
     "Memory-safety bugs, injection, the supply chain, and secure-by-design coding — the common failure "
     "modes and their defenses.", 7),
    ("Vol 4 · Security & Privacy Engineering", "Data Security",
     "Encryption at rest and in transit, secrets management, tokenization, and secure key handling for "
     "data platforms.", 5),
    ("Vol 4 · Security & Privacy Engineering", "Privacy Engineering",
     "Differential privacy, anonymization vs pseudonymization, GDPR/CCPA, and data governance — privacy "
     "as an engineering discipline.", 6),
    ("Vol 4 · Security & Privacy Engineering", "Secure Data Pipelines & Platforms",
     "Applying the above to real data systems: lineage, access, multi-tenancy, and compliance-by-design.", 5),
    ("Vol 4 · Security & Privacy Engineering", "Detection, Response & Operations",
     "Logging, monitoring, detection, and incident response — assuming breach and limiting blast radius.", 5),
    # ---- VOLUME 5 — The Staff/Principal Engineer & Tech Lead ----
    ("Vol 5 · The Staff/Principal Engineer & Tech Lead", "The Staff+ Role & Scope",
     "Archetypes (tech lead, architect, solver, right-hand), what 'impact' means above senior, and the "
     "shift from output to leverage.", 5),
    ("Vol 5 · The Staff/Principal Engineer & Tech Lead", "Technical Leadership & Strategy",
     "Technical vision, strategy, and roadmaps — setting direction others can follow.", 5),
    ("Vol 5 · The Staff/Principal Engineer & Tech Lead", "Architecture & Design at Scale",
     "Design review, ADRs, trade-off analysis, and evolving systems without a rewrite — the architect's "
     "judgment, applied.", 6),
    ("Vol 5 · The Staff/Principal Engineer & Tech Lead", "Influence Without Authority",
     "Building alignment and buy-in, driving decisions across teams, and disagree-and-commit.", 5),
    ("Vol 5 · The Staff/Principal Engineer & Tech Lead", "Communication & Writing",
     "The written word as a staff engineer's main tool: design docs, RFCs, and making complex ideas "
     "land.", 5),
    ("Vol 5 · The Staff/Principal Engineer & Tech Lead", "Mentoring & Growing Engineers",
     "Mentorship, sponsorship, code/design review as teaching, and multiplying the people around you.", 5),
    ("Vol 5 · The Staff/Principal Engineer & Tech Lead", "Execution & Judgment",
     "Leading projects and incidents, making decisions under uncertainty, and knowing what NOT to do.", 5),
    ("Vol 5 · The Staff/Principal Engineer & Tech Lead", "Career & the Organization",
     "Navigating the org, the promotion case, sustainability, and a durable definition of technical "
     "leadership.", 5),
]


def _roman(n):
    vals = [(10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    out = ""
    for v, s in vals:
        while n >= v:
            out += s
            n -= v
    return out


def _build_parts():
    parts = []
    cid = 1
    part_no = 0
    for vol_label, title, blurb, count in _SPEC:
        part_no += 1
        ids = [f"ch{cid + i:02d}" for i in range(count)]
        cid += count
        parts.append((f"{vol_label} · Part {_roman(part_no)}", title, blurb, ids))
    return parts


PARTS = _build_parts()


def chapter_files():
    return {p.name.split("-")[0]: p for p in sorted(CH.glob("ch*.html"))}


def solution_files():
    out = {}
    for p in sorted(SOL.glob("sol*.html")):
        num = re.match(r"sol(\d+)", p.name)
        if num:
            out[f"ch{int(num.group(1)):02d}"] = p
    return out


def appendix_files():
    if not APP.exists():
        return []
    return [p for p in sorted(APP.glob("app*.html"))]


def _title_of(fragment_path):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", fragment_path.read_text(), re.S)
    return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else fragment_path.stem


def toc_html(files, sols):
    out = ['<nav class="toc"><h1>Contents</h1><ol>']
    for part_num, part_title, _blurb, chapters in PARTS:
        out.append(f'<li class="toc-part">{part_num} &mdash; {part_title}</li>')
        for cid in chapters:
            f = files.get(cid)
            if not f:
                continue
            out.append(f'<li class="toc-ch"><a href="#{cid}">{_title_of(f)}</a></li>')
    apps = appendix_files()
    if sols or apps or (ROOT / "cheatsheet.html").exists() or (ROOT / "backmatter-index.html").exists():
        out.append('<li class="toc-part">Back Matter</li>')
    if sols:
        out.append('<li class="toc-ch"><a href="#solutions">Solutions to Exercises</a></li>')
    for app in apps:
        m = re.match(r"app([A-Z])", app.name)
        aid = f"app{m.group(1)}" if m else app.stem
        out.append(f'<li class="toc-ch"><a href="#{aid}">{_title_of(app)}</a></li>')
    if (ROOT / "cheatsheet.html").exists():
        out.append('<li class="toc-ch"><a href="#cheatsheet">Cheat Sheet</a></li>')
    if (ROOT / "backmatter-index.html").exists():
        out.append('<li class="toc-ch"><a href="#index">Index</a></li>')
    out.append("</ol></nav>")
    return "\n".join(out)


def assemble():
    files = chapter_files()
    sols = solution_files()
    css = (ROOT / "style.css").read_text()
    front = (ROOT / "frontmatter.html").read_text() if (ROOT / "frontmatter.html").exists() else ""
    body = [front, toc_html(files, sols)]
    for part_num, part_title, blurb, chapters in PARTS:
        body.append(
            f'<div class="part-page"><div class="part-num">{part_num}</div>'
            f"<h1>{part_title}</h1><p class='part-blurb'>{blurb}</p></div>"
        )
        for cid in chapters:
            if cid in files:
                body.append(files[cid].read_text())
            else:
                print(f"  !! missing {cid}", file=sys.stderr)

    if sols:
        body.append(
            '<div class="part-page" id="solutions"><div class="part-num">Back Matter</div>'
            "<h1>Solutions to Exercises</h1><p class='part-blurb'>Worked solutions to the "
            "end-of-chapter exercises. Try each before reading its solution.</p></div>"
        )
        ordered = [cid for *_r, chapters in PARTS for cid in chapters if cid in sols]
        for cid in ordered:
            body.append(sols[cid].read_text())

    apps = appendix_files()
    if apps:
        body.append(
            '<div class="part-page" id="appendices"><div class="part-num">Back Matter</div>'
            "<h1>Appendices</h1><p class='part-blurb'>Supplementary and reference material.</p></div>"
        )
        for app in apps:
            body.append(app.read_text())
        print(f"  + appended {len(apps)} appendices")

    for extra, marker in [("cheatsheet.html", "cheat sheet"), ("backmatter-index.html", "concept index")]:
        f = ROOT / extra
        if f.exists():
            body.append(f.read_text())
            print(f"  + appended {marker}")

    html = (
        "<!DOCTYPE html><html><head><meta charset='utf-8'>"
        "<title>The Systems Engineer's Path</title>"
        f"<style>{css}</style></head><body>" + "\n".join(body) + "</body></html>"
    )
    out = ROOT / "book.html"
    out.write_text(html)
    expected = sum(len(ch) for *_r, ch in PARTS)
    print(f"assembled {out} ({len(html)//1024} KiB, {len(files)}/{expected} chapters, {len(sols)} solution sets)")
    return out


def render(html_path):
    from weasyprint import HTML
    pdf = ROOT / "the-systems-engineers-path.pdf"
    HTML(filename=str(html_path)).write_pdf(str(pdf))
    print(f"rendered {pdf} ({pdf.stat().st_size//1024} KiB)")


if __name__ == "__main__":
    path = assemble()
    if "--html-only" not in sys.argv:
        render(path)
