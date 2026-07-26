# ⛔ NO FABRICATION — THE #1 RULE (overrides everything, including length/comprehensiveness)

NEVER make anything up. This is the single most important rule in the entire series.
- **Citations:** cite ONLY real sources that exist, with the CORRECT author, year, and venue, and only for a
  claim the source ACTUALLY makes. Never invent a paper, book, URL, author, date, or a "fact" attributed to a
  source. Prefer this file's list; any addition must be a real, checkable source.
- **Numbers/benchmarks/dates:** never invent a statistic, benchmark, version number, or date. If not verifiable,
  state it qualitatively or omit it; mark fast-moving figures with their date and source.
- **Tools/features/APIs:** describe only real, documented behavior (syscalls, flags, protocol guarantees); hedge or
  omit otherwise. Systems facts (memory-ordering guarantees, isolation-level anomalies, consensus safety/liveness)
  must be stated PRECISELY and correctly.
- **When unsure: HEDGE or OMIT.** A confident wrong statement is the worst outcome.
- **Fact-checkers:** a FABRICATION AUDIT is the FIRST and highest-severity check; any invented/misattributed
  citation, unsourceable figure, or wrong systems guarantee is a BLOCKER.

---

# BIBLIOGRAPHY — The Systems Engineer's Path (five volumes, one repo)

> Single source of truth for citations. Every chapter reference resolves here. FREE/legal unless marked
> `[⚠ reference — not free]` (named as a pointer only). Re-verify every URL/edition/date at authoring. Tags `[chNN]`
> added as chapters are written. Volume-scoped sections below.

## Vol 1 — Systems Programming & Performance
- **Bryant & O'Hallaron — *Computer Systems: A Programmer's Perspective* (CS:APP).** `[⚠ reference — not free]`
  The canonical machine/OS-from-the-programmer's-view text; the CMU 15-213 course materials are free.
- **Arpaci-Dusseau — *Operating Systems: Three Easy Pieces* (OSTEP).** FREE full text (`pages.cs.wisc.edu/~remzi/OSTEP/`).
  Processes, scheduling, virtual memory, concurrency, persistence.
- **Beej's Guide to C / Network Programming.** Free (`beej.us`). Practical C and sockets.
- **The Rust Programming Language ("the book").** Free (`doc.rust-lang.org/book/`), and the Rustonomicon for unsafe.
- **Drepper — *What Every Programmer Should Know About Memory* (2007).** Free PDF. Caches/memory (dated but seminal).
- **Agner Fog — optimization manuals.** Free (`agner.org`). Microarchitecture/perf (dated; verify).
- **Wulf & McKee — "Hitting the Memory Wall: Implications of the Obvious," ACM SIGARCH Computer Architecture News 23(1):20–24 (1995).** The paper that named the "memory wall." Cited in ch01 for the term's origin; real and widely available.
- **"Latency Numbers Every Programmer Should Know"** (community list attributed to Jeff Dean; Colin Scott's interactive version, `colin-scott.github.io/personal_website/research/interactive_latency.html`). Free. Cited in ch01 **only as orders-of-magnitude ratios** (SSD/network rows); the register→DRAM figures are anchored to CS:APP instead. Treat every number as approximate and dated.
- **Martin Thompson — "Mechanical Sympathy"** (mechanical-sympathy.blogspot.com; talks/QCon). Free. Popularized the term "mechanical sympathy" (borrowed from motor racing) for writing software that works *with* the hardware; co-designer of the LMAX Disruptor. Cited in ch05 as the descriptive origin of the term (the underlying cache/layout technique is attributed to Drepper / MIT 6.172).
- **MIT 6.172 *Performance Engineering of Software Systems*.** Free OCW. Profiling, cache-aware, vectorization.
- **The Linux `man` pages / `io_uring` docs (Jens Axboe).** Primary source for syscalls; verify per kernel version.
- **AddressSanitizer / LeakSanitizer / MemorySanitizer documentation** (Clang/GCC; `github.com/google/sanitizers`, LLVM/GCC docs). Free. The compile-time (`-fsanitize=address`) memory-error detectors; cited in ch09 for documented behavior only (use-after-free, heap-overflow, double-free, leaks — ASan does not catch uninitialized reads; that is MSan/Valgrind). Verify flags per compiler version.
- **Valgrind (Memcheck) documentation** (`valgrind.org`). Free. The runtime memory-error/leak detector; cited in ch09 as a complementary tool to the sanitizers. Documented behavior only.

## Vol 2 — Database Internals
- **Petrov — *Database Internals* (2019).** `[⚠ reference — not free]` Storage engines, B-trees/LSM, distributed DBs.
- **Hellerstein, Stonebraker & Hamilton — *Architecture of a Database System* (2007).** Free monograph.
- **Mohan et al. — *ARIES* (ACM TODS 1992).** The recovery algorithm; verify a legal copy.
- **Bernstein, Hadzilacos & Goodman — *Concurrency Control and Recovery in Database Systems* (1987).** Free from authors.
- **CMU 15-445/645 *Database Systems* (Pavlo).** Free course (videos, notes, the BusTub project). Primary build spine.
- **Graefe — *Query Evaluation Techniques for Large Databases* (ACM Computing Surveys 1993);** *Volcano* (1994).
- **Selinger et al. — *Access Path Selection…* (System R, SIGMOD 1979).** Cost-based optimization.

## Vol 3 — Distributed Systems, Deeply
- **Kleppmann — *Designing Data-Intensive Applications* (2017).** `[⚠ reference — not free]` The applied through-line.
- **Cachin, Guerraoui & Rodrigues — *Introduction to Reliable and Secure Distributed Programming*.** `[⚠ reference]`
- **Lamport — *Time, Clocks…* (CACM 1978); *The Part-Time Parliament* (Paxos, TOCS 1998); *Paxos Made Simple* (2001).**
- **Ongaro & Ousterhout — *In Search of an Understandable Consensus Algorithm* (Raft, USENIX ATC 2014).** Free.
- **Fischer, Lynch & Paterson — *Impossibility of Distributed Consensus…* (FLP, JACM 1985).**
- **Shapiro et al. — *Conflict-free Replicated Data Types* (2011).** Free (INRIA).
- **Karger et al. — *Consistent Hashing…* (STOC 1997).**
- **Lamport — *Specifying Systems* (TLA+).** Free PDF (Microsoft/author); the TLA+ tools & Learn TLA+ (free).
- **MIT 6.824 *Distributed Systems* (Morris).** Free course + labs.

## Vol 4 — Security & Privacy Engineering
- **Anderson — *Security Engineering*, 3rd ed. (2020).** FREE full PDF (`cl.cam.ac.uk/~rja14/book.html`). Primary spine.
- **OWASP** — Top 10, ASVS, Cheat Sheet Series (free; dated — cite the version/year).
- **Boneh & Shoup — *A Graduate Course in Applied Cryptography*.** Free draft (`toc.cryptobook.us`). Crypto done right.
- **NIST publications** (SP 800-series, FIPS) — free, authoritative; cite the specific document + revision.
- **Dwork & Roth — *The Algorithmic Foundations of Differential Privacy* (2014).** Free monograph.
- **The GDPR / CCPA statutory texts** — primary sources; cite the article/section, not a summary, for legal claims.

## Vol 5 — The Staff/Principal Engineer & Tech Lead
- **Larson — *Staff Engineer: Leadership Beyond the Management Track* (2021).** `[⚠ reference — not free]`; StaffEng
  stories (`staffeng.com`) are free.
- **Google *Site Reliability Engineering* & *The SRE Workbook*.** FREE full text (`sre.google/books/`). (Also seeds
  the Vol 3/operations material.)
- **Google's *Engineering Practices* (code review) & re:Work** — free.
- **Nygard — *Release It!*** `[⚠ reference — not free]` (patterns already used in the data track).
- *(Leadership claims are judgment, not fact; attribute frameworks to real sources, present as informed practice,
  and avoid inventing studies or statistics. Where an empirical claim is made, it must have a real citation.)*
