# Retrieval commands

Run the installed scripts/kb.py using its absolute path from any working directory. The examples below show arguments after that script path. Python invocation: python -B -X utf8.

Global options precede the command: --snapshot ID, --budget CHARACTERS, and optional --root RESEARCH_SKILL_DIRECTORY. Do not point --root to the original corpus. Default output budget is 12,000 characters, adjustable from 3,000 to 60,000; these are characters, not measured model tokens.

| Command arguments | Purpose |
| --- | --- |
| info | Snapshot identity, package profile, archive identity/counts, corpus size and active defaults |
| resolve pacs.008.001.14 | Exact message and focused navigation |
| resolve semt.002 | All supplied versions of a family |
| resolve urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14 | Namespace resolution |
| search "AccountIdentification4Choice" --message pacs.008.001.14 --kind schema-type | Exact scoped schema search |
| search "Constraints" --source src-000163 --kind source-section | Locate MDR rules in source text |
| search "account servicer" --kind participant --limit 5 | Contextual participants |
| outline PATH | Available section headings and line numbers |
| links PATH --match Constraints | Focused navigation without reading the entire index |
| read PATH --section "Complete compositor, member and restriction reference" | One complete section, or explicit continuation |
| read PATH --start-line 40 --end-line 55 | Inclusive packaged-file line range; return necessary surrounding context too |
| metadata PATH | Full front matter through bounded continuations |
| source src-000169 | Provenance page and matching optional local originals |

Search includes reference body text, tables, literal declarations and metadata terms. Terms are ANDed. Filters: --message, --namespace, --collection, --edition, --source, --kind, --domain, --status, --under. --under is a directory relative to the snapshot. An exact title match ranks first; other results use full-text relevance, then path. Use --offset and --limit for subsequent result pages.

An explicit namespace is matched in full and case-sensitively. A foreign namespace with a familiar message suffix does not resolve, and an example-only reference cannot establish an unknown namespace. Use --namespace for namespace filters; --message accepts exact IDs or families.

Message filters match explicitly tagged references, not every MDR section that might discuss the message. Follow the message's mdr-evidence links or search its source/collection for rules. Most rules are source-section content; limiting everything to business-rule would miss them.

## Minimal sufficient reading

Start with five candidates and a few focused sections. Do not load whole catalogs or every type dependency. Read the smallest evidence that preserves the condition, exception, table header/footnote or enclosing compositor needed for the claim.

Every response supplies snapshot_id. Pin it in later calls. A pinned call reads that retained snapshot independently of the current active pointer. For read or metadata, repeat the same path/section with --offset NEXT_OFFSET until the needed selection is complete. Offsets are Unicode character positions in the selected text. selection_complete means there is no remaining text in the selected packaged section/file after this chunk; it does not certify that the original document's semantic section ends there. Follow source-section continuation links where present. contains_entire_selection indicates whether the complete selection fits in this one response. Combine prior chunks when offset is nonzero. partial_line means even a single row/line was split; never interpret the fragment as complete. Citation line numbers refer to the packaged file, while original PDF/DOCX/XSD locators remain in the reference.

Search results include snippet_line. For a large table, use a line-range read around the relevant row and separately retrieve its header and applicable notes; a line range never establishes the complete surrounding rule. Search snippets can omit qualifiers. Compact metadata explicitly identifies omitted fields; inspect full metadata before relying on those fields. Increase the budget for justified complex work. No fixed limit permits silently omitting substantive constraints.

links returns actual inline, image and reference-style Markdown links. Code examples, comments, tag attributes and XML/JSON evidence literals are excluded. Relative targets retain their fragments; use the separate path field for read/outline and the fragment to locate the intended heading or anchor.

## Missing evidence

Zero hits means no indexed match under the displayed filters. Inspect resolved references, vary the search, or remove defaults with --all-scopes before concluding that evidence is unavailable.

Source IDs, source hashes and original locations remain intact. Availability pages identify omitted binaries or working artifacts. In a research-core snapshot, archived-derived-evidence notices identify detached supporting artifacts by their original packaged path, checksum, size, known source IDs and archive identity. These artifacts were intentionally archived; their availability notices do not establish missing originals, a review failure or a new review. Notices are packaging records and do not establish the contents of archived evidence. Follow retained reference qualifications and do not claim to have inspected an artifact through its notice.

The maintenance archive is outside the installed skill and is not required for retrieval. The helper does not locate, open or attach it. Do not use evidence_pack for derived archive material: that optional facility authenticates separately supplied original-source bytes. A missing schema, code enumeration, supplied dependency or unresolved source contradiction remains a limitation. Availability pages do not stand in for visual inspection.

The helper never renders or executes documents, contacts a network service, or mutates the active corpus. source hashes selected optional evidence files, checks their registered source identity, and verifies exact ZIP member bytes when a registered archive is attached. It returns verified locations and original occurrence/member provenance, not a semantic inspection result. If the index is missing/incompatible, report the problem for the separate maintenance workflow.
