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
  The canonical machine/OS-from-the-programmer's-view text; the CMU 15-213 course materials are free. Cited in
  **ch13** (Ch 8, exceptional control flow / traps & system calls), **ch14** (Ch 8, processes, process creation,
  reaping children), **ch15** (Ch 12, concurrent programming — threads, shared variables, races), **ch16** (Ch 8,
  context switches and the timer interrupt behind preemption), **ch17** (Ch 9, virtual memory — address spaces, page
  tables, demand paging, memory mapping), **ch18** (Ch 8 §8.5, signals — exceptional control flow, handlers, and the
  hazards of handler code).
- **Arpaci-Dusseau — *Operating Systems: Three Easy Pieces* (OSTEP).** FREE full text (`pages.cs.wisc.edu/~remzi/OSTEP/`).
  Processes, scheduling, virtual memory, concurrency, persistence. Cited in **ch13** ("Mechanism: Limited Direct
  Execution" — user/kernel mode, traps, the system-call mechanism), **ch14** ("Abstraction: The Process" and
  "Interlude: Process API" — <code>fork</code>/<code>exec</code>/<code>wait</code>), **ch15** ("Concurrency: An
  Introduction" and "Interlude: Thread API" — threads, the shared/private split, the data race), **ch16**
  ("Scheduling: Introduction" — turnaround/response metrics, FIFO/SJF/STCF/round-robin — and "Scheduling: The
  Multi-Level Feedback Queue" — MLFQ, boosting, anti-gaming), **ch17** ("Paging: Introduction," "Beyond Physical
  Memory: Mechanisms," and "Beyond Physical Memory: Policies" — the page, demand paging/swapping, and OPT/FIFO/LRU
  replacement). *(Exact chapter titles verified against the OSTEP PDFs.)*
- **Beej's Guide to C / Network Programming.** Free (`beej.us`). Practical C and sockets.
- **The Rust Programming Language ("the book").** Free (`doc.rust-lang.org/book/`), and the Rustonomicon for unsafe.
- **Drepper — *What Every Programmer Should Know About Memory* (2007).** Free PDF. Caches/memory (dated but seminal).
- **Agner Fog — optimization manuals.** Free (`agner.org`). Microarchitecture/perf (dated; verify).
- **Wulf & McKee — "Hitting the Memory Wall: Implications of the Obvious," ACM SIGARCH Computer Architecture News 23(1):20–24 (1995).** The paper that named the "memory wall." Cited in ch01 for the term's origin; real and widely available.
- **"Latency Numbers Every Programmer Should Know"** (community list attributed to Jeff Dean; Colin Scott's interactive version, `colin-scott.github.io/personal_website/research/interactive_latency.html`). Free. Cited in ch01 **only as orders-of-magnitude ratios** (SSD/network rows); the register→DRAM figures are anchored to CS:APP instead. Treat every number as approximate and dated.
- **Martin Thompson — "Mechanical Sympathy"** (mechanical-sympathy.blogspot.com; talks/QCon). Free. Popularized the term "mechanical sympathy" (borrowed from motor racing) for writing software that works *with* the hardware; co-designer of the LMAX Disruptor. Cited in ch05 as the descriptive origin of the term (the underlying cache/layout technique is attributed to Drepper / MIT 6.172).
- **MIT 6.172 *Performance Engineering of Software Systems*.** Free OCW. Profiling, cache-aware, vectorization.
- **The Linux `man` pages / `io_uring` docs (Jens Axboe).** Primary source for syscalls; verify per kernel version.
  Cited for documented behavior in **ch13** (`syscall(2)` — the x86-64 calling convention: number in `rax`, args in
  `rdi,rsi,rdx,r10,r8,r9`, result in `rax`; `vdso(7)` — the vDSO serving `clock_gettime`/`gettimeofday` without a
  trap), **ch14** (`fork(2)`, `execve(2)`, `wait(2)` — copy-on-write, image replacement, zombies/orphans), **ch15**
  (`pthreads(7)`, `clone(2)` — the NPTL one-to-one model and the `CLONE_VM`/`CLONE_FILES`/`CLONE_THREAD` flags that
  distinguish a thread from a `fork`), **ch16** (`sched(7)`, `nice(2)`, `sched_setscheduler(2)` — scheduling classes
  `SCHED_OTHER`/`SCHED_FIFO`/`SCHED_RR`, the nice range −20..+19, and real-time throttling), **ch17** (`mmap(2)`,
  `madvise(2)`, `proc(5)` — demand-paged memory mapping and the `/proc/<pid>/status` `VmRSS` residency field), **ch18**
  (`signal(7)`, `sigaction(2)`, `signal-safety(7)`, `signalfd(2)` — the signal list and default dispositions, the
  `SA_RESTART`/`EINTR` behavior, the async-signal-safe function set, and file-based signal delivery). Verify per
  kernel/architecture.
- **The Linux kernel scheduler documentation** (`docs.kernel.org/scheduler/`, including the EEVDF scheduler page). Free.
  The authority for Linux's proportional-share scheduler and the CFS→EEVDF change in kernel 6.6 (2023). Cited in **ch16**
  for documented behavior; fast-moving, treat details as version-specific. *(CFS→EEVDF-in-6.6 corroborated by the kernel
  docs and Phoronix's 6.6 merge coverage; verified.)*
- **Belady — "A study of replacement algorithms for a virtual-storage computer," *IBM Systems Journal* 5(2):78–101
  (1966);** and **Belady, Nelson & Shedler — "An anomaly in space-time characteristics of certain programs running in a
  paging machine," *Communications of the ACM* 12(6):349–353 (1969)** (DOI 10.1145/363011.363155). Primary sources for
  the optimal (MIN/OPT) replacement policy and for Belady's anomaly (FIFO can fault more with more frames). Cited in
  **ch17**; author/venue/year verified via dblp and the ACM Digital Library.
- **Stevens & Rago — *Advanced Programming in the UNIX Environment*, 3rd ed. (2013), Addison-Wesley.** `[⚠ reference —
  not free]` The canonical UNIX systems-programming reference. Cited in **ch18** (Chapter 10, Signals — `sigaction`,
  reliable signals, interrupted system calls). Author/edition/year verified.
- **AddressSanitizer / LeakSanitizer / MemorySanitizer documentation** (Clang/GCC; `github.com/google/sanitizers`, LLVM/GCC docs). Free. The compile-time (`-fsanitize=address`) memory-error detectors; cited in ch09 for documented behavior only (use-after-free, heap-overflow, double-free, leaks — ASan does not catch uninitialized reads; that is MSan/Valgrind). Verify flags per compiler version.
- **Valgrind (Memcheck) documentation** (`valgrind.org`). Free. The runtime memory-error/leak detector; cited in ch09 as a complementary tool to the sanitizers. Documented behavior only.
- **Chris Lattner — "What Every C Programmer Should Know About Undefined Behavior"** (The LLVM Project Blog, May 2011, three parts; `blog.llvm.org/2011/05/what-every-c-programmer-should-know.html`). Free. The compiler-writer's account of how/why optimizers exploit UB (signed overflow, null-check elimination, strict aliasing). Cited in ch10.
- **John Regehr — "A Guide to Undefined Behavior in C and C++"** (Embedded in Academia, 2010, three parts; `blog.regehr.org/archives/213`). Free. Researcher's catalogue of UB and its interaction with aggressive compilers ("UB can time-travel"). Cited in ch10.
- **UndefinedBehaviorSanitizer (UBSan) documentation** (Clang/GCC; `clang.llvm.org/docs/UndefinedBehaviorSanitizer.html` and GCC docs). Free. Runtime detector for many UB categories (`-fsanitize=undefined`). Cited in ch10 for documented behavior only; verify checks/flags per compiler version.
- **CVE-2009-1897 — Linux kernel `tun_chr_poll` null-check elimination** (NVD; kernel `drivers/net/tun.c`, 2.6.30; kernel Makefile adoption of `-fno-delete-null-pointer-checks`). Primary sources. Cited in ch10 as a real instance of the optimizer deleting a null check placed after a dereference.
- **Aleph One (Elias Levy) — "Smashing the Stack for Fun and Profit,"** Phrack Magazine, Issue 49, file 14 (1996; `phrack.org/issues/49/14`). Free. The first widely read step-by-step account of stack-buffer-overflow exploitation. Cited in ch11 for the mechanism (historical; mitigations postdate it).
- **CS:APP §3.10 (buffer overflows).** Buffer overflow, stack smashing, and mitigations (canaries, ASLR, NX) on the stack-frame model. Cited in ch11 (see CS:APP entry above; `[⚠ reference — not free]`, CMU 15-213 materials free).
- **Berger, Zorn & McKinley — "Reconsidering Custom Memory Allocation," OOPSLA 2002** (ACM SIGPLAN; free from authors, `people.cs.umass.edu/~emery/pubs/berger-oopsla2002.pdf`). Empirical study: a good general-purpose allocator matches/beats most hand-written custom allocators; regions (arenas) the exception (up to 44% faster, with a memory-consumption downside). Cited in ch12.
- **Jeff Bonwick — "The Slab Allocator: An Object-Caching Kernel Memory Allocator," USENIX Summer 1994**, pp. 87–98. Free. The production pool/slab allocator (SunOS; later Linux). Cited in ch12 for the fixed-size/free-list model.
- **cppreference.com / the C standard — `<string.h>` functions and integer/overflow rules.** The authority for `strcpy`/`strncpy`/`strcat`/`snprintf`/`fgets` contracts (and the removal of `gets` in C11), and for signed/unsigned overflow and the §3.4 behavior categories. Cited in ch10–ch12,
  and in **ch15** for the C11/C++11 memory model — a data race is undefined behavior.

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
