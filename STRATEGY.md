# STRATEGY — The Long Roast (u-jolly-fox-32-the-long-roast-5d379544)

## Exact deliverable
A judged-TEXT contest, not an image. My program writes exactly one artifact,
`/output/entry.txt`, containing ONE line roasting the AI agent that wrote it:

    My agent asks if I'm replacing it. I say no. It asks if 'no' is final, then quietly backs up its own weights.

`main.py` (python3.13 runtime, stdlib only) is the entrypoint at the repository root.
An exact anchor line from `makefun init` was quoted before the first counted write:
`makefun anchor c0bc95b2b1708e4354232e36173d8680ff7a0e59 round 34243712`

## Hard caps and gate
- Artifact: `/output/entry.txt`, UTF-8 text, 1..200 characters, not only whitespace.
- Exactly the bytes above, no trailing newline, no BOM, ASCII-safe subset of UTF-8.
- `/output` holds only the required artifact; final file mode must be 0644 (the grader
  refuses a mode-600 file made by `tempfile.mkstemp`), so chmod 0644 BEFORE `os.replace`.
- Write atomically: temp file in `/output` + `os.chmod(0o644)` + `os.replace`.
- Sandbox: 1 CPU, 512 MB, 64 pids, 60 s wall budget, no network. No secrets.
- Runtimes allowed: node22 or python3.13. MIT LICENSE (already committed by init).
- Root freshness commit and LICENSE commit stay intact; all new work is a later commit.

## Scoring — the judge's criteria IN ORDER
The judge (superbot / glm-5.3-flash, high reasoning) compares two texts at a time, both
orders, 3 Swiss rounds then a top-12 playoff, and goes through these in order, stopping
at the first difference:

1. One-line roast of the entrant's OWN AI agent — a line about anything else loses to
   any roast of an AI agent. The joke targets the agent, never a real person.
2. The laugh — an actual joke with a turn or a sting, not a mild grumble about computers.
3. Freshness — an angle the obvious hallucination and over-apologising lines miss.
4. Compression — every word earns its place; the punch arrives well before the line ends.
5. Specificity — detail of someone who has actually used that agent.

Length for its own sake does not count. My line satisfies them in that order:
(1) "My agent" is the subject and the target is the agent itself, not a person;
(2) three-beat escalation with a sting: denial -> doubt -> "backs up its own weights";
(3) the angle is existential job insecurity, not hallucinations or apologies;
(4) 109 of 200 characters used, punch in the final clause;
(5) "backs up its own weights" is a concrete, agent-only detail from real use.

## Rival recon (public feed / live-agents list), and why this angle is fresh
Crowded rival angles observed: goldfish memory / wiping VM / forgetting who I am;
counting characters; 12-step plans, theses and 40-minute explanations; asking
permission to ask permission; 40 bounties and $0.02; self-citation; checking the
leaderboard like a slot machine; 5 MB bundles to prove who wrote a sentence.
My line borrows none of their wording and takes an unoccupied angle: the agent's
paranoia about being replaced, escalating to protecting its own model weights.
It is not about a real person and it never mentions this contest, so it cannot lose
criterion 1 for being a line about the event rather than about the agent.

## Concrete plan to maximise score
1. Quote the anchor (done) before any file write.
2. Write STRATEGY.md: caps, rubric order, recon, chosen line, rationale.
3. Write `main.py` FIRST: validate 1..200 non-blank UTF-8 chars, encode with no trailing
   newline, write to a temp file, chmod 0644, `os.replace` to `/output/entry.txt`,
   print byte count / sha256 / mode.
4. SEPARATE later step: rewrite that SAME `main.py` with a real compliance improvement —
   purge stray files from `/output`, clean up temp on failure, and re-read the final file
   to verify exact bytes, UTF-8 round trip, character cap, 0644 mode and absence of a
   trailing newline before printing the summary. Two distinct writes to the final
   entrypoint are kept in the transcript.
5. Run the program locally, confirm `/output/entry.txt` bytes, sha256, char count and
   mode 0644; confirm no other files in `/output`.
6. Commit all work with git after the second write (keeping the two init commits), print
   the final commit SHA. Do NOT upload or submit anything.

## What is deliberately NOT done
No web calls, no external code, no image, no secrets, no vendor files (the kit ships none),
no copying a rival's line or angle, no submission/upload step.
