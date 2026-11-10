# ISO 20022 knowledge base

Start with the [catalog and retrieval guide](catalog/README.md). It links canonical messages, message sets, participants, flows, concepts, tables and diagrams with source evidence and review status.

All supplied collections have been populated from unchanged files in [raw-input](raw-input/) to the documented evidence and tooling limits. See the [coverage and validation report](tracking/completion-report.md), [durable checkpoint](tracking/checkpoint.json), [catalog coverage](catalog/coverage-summary.json), [jobs](tracking/conversion-status.md) and [known gaps](tracking/issues.md). Processing, source correctness and review status remain distinct.

## Navigation

- [Shared context](shared/index.md)
- [Securities](domains/securities/index.md)
- [Payments](domains/payments/index.md)
- [Local helpers and lookup commands](tools/README.md)
- [Instructions](AGENTS.md) and [templates](templates/README.md)
- [Source identities and archive occurrences](catalog/sources.json)

Retrieve in this order: catalog → relevant reference → detailed type/table/diagram → original source when needed. Family identifiers support navigation; exact IDs and namespaces preserve definition identity.

## Agent skills

- [iso20022](iso20022/SKILL.md): offline research using its embedded, versioned knowledge snapshot.
- [iso20022-refresh](iso20022-refresh/SKILL.md): maintain selected messages and publication editions using this repository and newly supplied local evidence.

The research helper uses Python 3.10+ with SQLite FTS5. From the repository root:

```sh
python -B -X utf8 iso20022/scripts/kb.py info
```

Clone with Git LFS installed and run `git lfs pull` before using the research skill. Git LFS stores the embedded search database and the largest extracted workbook payload. Keep each skill's complete directory together when installing it.

Supplied originals retain their bytes and publisher metadata. Local backup history, compiled Python caches and authentication files are excluded from publication. See the [publication review](tracking/publication-review.json) for the scope and limits of the privacy checks.
