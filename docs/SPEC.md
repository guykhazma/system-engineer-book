# The Systems Engineer's Path — SPEC (data-track deep-mastery companion; ONE repo, FIVE volumes)

> Status: **structure locked, drafting after the earlier data-track volumes.** This is the deep-systems + leadership
> companion to the data track (after *The Data Engineer's Path* V1, *The Data Architect's Path* V2, and *The
> Algorithmic Thinker's Path* V3). Per the author, the five advanced books are bundled as **one book with five
> volumes in one repo** (like the bioinformatics book), one build with per-volume Part-groups. Title is provisional.
> NO-FABRICATION rule (BIBLIOGRAPHY.md) governs everything; nothing committed to git until asked.

## 1. Thesis & reader
**Thesis.** Take an engineer who can build and design data systems (V1–V2) and think algorithmically (V3), and make
them a **deep systems engineer and technical leader**: someone who understands the machine to the metal, can *build*
the hard infrastructure (a database, a distributed system) rather than only assemble it, can secure it, run it, and
lead the people and technical strategy around it. The arc is deliberately **from the machine to the org.**

**Reader.** A working data/backend/infrastructure engineer leveling from senior toward staff/principal. Comfortable
coding; this book supplies the depth and rigor. Each volume is self-contained enough to read on its own, but they
compose into a single progression.

**What makes it different.** *Implementation depth, not survey.* V2 (Architect) chooses and designs systems from the
architect's chair; here the reader **builds** them (a storage engine, a query engine, a Raft implementation, a
TLA+-checked protocol) and reasons about them formally. Every systems guarantee (a memory-ordering rule, an isolation
anomaly, a consensus safety/liveness property) is stated **precisely** and, where possible, demonstrated in running
code or a model checker.

## 2. Pedagogy
Shared series conventions (`docs/PEDAGOGY.md`, grounded in the Google Learn-Your-Way RCT & Harvard Deslauriers 2019
PNAS): recall openers with spaced retrieval, in-chapter quick checks, worked→faded→independent ladders (`faded` +
interleaved `mixed`), prompt-then-reveal `communicate` boxes, "can you… without looking?" takeaways, closed-book
retrieval, and TEACHING solutions (why + method-selection + named tempting-wrong-answer + feed-forward). Systems-
specific asides: a **Guarantee box** (state the exact invariant/guarantee and its assumptions), a **Failure box**
(what breaks it and the blast radius), and a **Cost box** (time/space/coordination/latency). Every volume ends with a
build-along the reader can run; each is a portfolio artifact.

## 3. The five volumes (see build.py `_SPEC` for the exact part/chapter map)
- **Volume 1 — Systems Programming & Performance.** The machine & cost model → C & manual memory → the OS → concurrency
  & parallelism (memory models, lock-free) → Rust for systems → performance engineering (profiling, cache-aware, SIMD)
  → low-level I/O & networking (epoll/io_uring, zero-copy). *Exit: you understand what your code actually runs on and
  can make it fast.*
- **Volume 2 — Database Internals (Build a Database).** Storage & buffer pool → storage engines (B-tree/LSM) →
  durability & recovery (WAL/ARIES) → transactions & concurrency control (2PL/MVCC/OCC) → query processing & execution
  → query optimization → indexing → **[BUILD] a working relational engine** → toward distributed databases. *Exit: you
  have built a database.* (Deepens V2's storage/query parts from design into implementation; pairs with V3 algorithms.)
- **Volume 3 — Distributed Systems, Deeply.** Models & FLP & time/causality → replication & consistency
  (linearizability, CAP/PACELC) → consensus (Paxos/Raft) → coordination & distributed transactions → CRDTs & gossip →
  partitioning/consistent hashing → distributed algorithms → **formal methods (TLA+)** → building & operating. *Exit:
  you can reason about, specify, and build correct distributed systems.*
- **Volume 4 — Security & Privacy Engineering.** Threat modeling → applied cryptography (used correctly) → authn/authz
  → software & systems security → data security → **privacy engineering** (differential privacy, GDPR/CCPA) → secure
  data pipelines → detection & response. *Exit: you can build and run data systems that resist attack and respect
  privacy.*
- **Volume 5 — The Staff/Principal Engineer & Tech Lead.** The staff+ role & scope → technical leadership & strategy →
  architecture & design at scale → influence without authority → communication & writing (RFCs/design docs) →
  mentoring & sponsorship → execution & judgment → career & the org. *Exit: you multiply your impact through
  technical leadership.* (Leadership content is framed as informed practice, not invented studies; empirical claims
  need real citations.)

## 4. Cross-track integration & overlap management
- **Complements, doesn't duplicate:** V2 Architect *designs/selects*; this book *implements/proves*. The AI book owns
  ML/MLOps systems; this book stays on general systems/infra. The Quant/Bio books own their domains.
- **Reuses vetted sources** from *The Data Architect's Path* bibliography where a systems claim overlaps (storage
  engines, MVCC/ARIES, consensus, columnar/indexing) — re-verify before citing.
- **Feeds back:** Vol 3/operations material and Vol 5 leadership double as the maturity layer the whole series points
  toward (e.g. the career capstones in the AI and Bio books can reference Vol 5's leadership treatment).

## 5. Open questions to settle
1. **Title.** "The Systems Engineer's Path" (provisional) vs. something that foregrounds the build-and-lead arc.
2. **Placement/numbering in the data track.** Is this a single "Volume 4" (multi-part) or does each internal volume get
   a track number (V4–V8)? (Recommendation: keep it ONE book with five internal volumes, referenced as the track's
   deep-mastery companion, to match the author's "one book, multiple volumes" directive.)
3. **Language.** C + Rust for Vol 1–2 (systems norm); Python/pseudocode elsewhere; a build language for Vol 2/3 labs
   (Rust or Go recommended for the DB/Raft builds). Confirm.
4. **Streaming/real-time.** Fold into Vol 2 (log/storage) + Vol 3 (ordering/exactly-once), or add a sixth volume?
   (Recommendation: fold in, to avoid overlap with the Architect book's streaming part.)
