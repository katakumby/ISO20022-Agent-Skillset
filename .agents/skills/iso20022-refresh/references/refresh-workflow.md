# Refresh workflow

## Selection and command contract

Use the repository's tools/kb.py with --root before the subcommand. In PowerShell, a typical setup is:

    $kbRoot = (Get-Location).Path  # Run from the selected repository checkout.
    python -B -X utf8 "$kbRoot\tools\kb.py" --root "$kbRoot" scan --limit 20

Scan writes nothing and allocates no IDs. It prioritizes changed candidates and returns fingerprints, occurrences, candidate identities, unresolved routing, counts and truncation information. Increase --limit (maximum 1000) or use --path raw-input/collection to inspect a narrower scope. A bounded result is not proof that no other inputs exist.

Once the target is established, build a complete selection:

    python -B -X utf8 "$kbRoot\tools\kb.py" --root "$kbRoot" impact --message sese.023.001.13

Or use impact --set settlement-and-reconciliation --edition 2025-2026. These are examples of selectors, not permission to process those messages in every run. Save the returned JSON under work/refresh/ for this request using UTF-8. impact rescans internally; --scan FILE is optional and rejects a truncated scan.

The selection contains target, candidates, verified_routing, affected paths with proof chains, reference fingerprints, baseline register hashes, deferred candidates and limitations. Do not remove conflicts or alter fingerprints to bypass a stale-selection rejection. Rescan and reconcile the new evidence instead.

## Establishing new editions and document coverage

New bytes do not inherit the old hardcoded edition for their collection. A known input collection establishes a routing suggestion, not its publication date. An unknown collection remains unresolved.

Inspect the original cover/title, exact message headings or schema declarations. Before impact, provide --routing FILE when new documents cannot yet be mapped to the target. The routing file maps a candidate's content-hash key (or existing source ID) to:

- collection, domain, set_slug, set_title;
- source_edition, edition_slug, edition_basis and edition_locator;
- an optional evidence-supported set_path within the existing output layout;
- message_ids when exact document headings establish them.

Use a precise edition_locator, such as a PDF file page and heading or DOCX heading/paragraph. Do not infer an exact definition from a similar filename. Schema IDs, namespaces, roots and dependency declarations are read from the schema and cannot be overridden through the selection.

If no edition is stated, retain source_edition: null. Registration assigns an edition-unknown-src-NNNNNN destination. Shared code publications use the existing shared/reference/code-sets layout through an evidence-backed set_path. Preserve T2S child message-set boundaries and route shared administrative/header definitions according to the catalog.

An identical file appearing in another publication gains an occurrence/membership. Its existing canonical destination does not move.

## Register and resume

Allocate the next unused job number after reading tracking/jobs.json and the relevant tracking records. Registration also checks that the ID is unused and greater than prior IDs.

    python -B -X utf8 "$kbRoot\tools\kb.py" --root "$kbRoot" inventory --selection "$selectionPath" --job "$jobId"

This registers only selected contents, required schema dependencies and parent archive identities. Unselected archive members remain deferred. The applied manifest is tracking/refresh/<job-id>/selection.json; use that file in subsequent commands. It contains selected_source_ids and recorded conflicts.

The helper verifies raw fingerprints, register baselines and affected-reference fingerprints before mutation. It snapshots changed persistent Markdown and JSON under tracking/history/<job-id>/<run>/, preserves unknown metadata and manual issue/job entries, and writes current dates. Before changing any registers, it persists registration.json beside the applied selection. This journal binds the original request to all proposed output bytes and their before/after hashes. Repeating a completed unchanged registration with the same original selection and job is a no-op.

An occurrence can be current, missing or changed. Historical location evidence is retained. Readers try available occurrences and accept only matching bytes; archive-member provenance also binds the parent archive checksum. Do not copy originals into reference folders or restore missing originals by inventing content.

If registration was interrupted, first inspect tracking/refresh/<job-id>/registration.json. Repeat inventory with the same original selection and job; it rechecks raw inputs and affected references, then skips already committed bytes and completes only journaled outputs still matching their before/after hashes. Registers may be partially updated until this recovery finishes. Do not proceed to extraction while the journal is pending. A changed source, reference, or authored register causes rejection before replay; reconcile that drift explicitly and retain the journal and history instead of editing fingerprints. If a hard process termination left a temporary lock, confirm that its recorded process has ended before removing only that lock. After registration is complete, read the applied selection, per-job reports and checkpoint to resume outstanding extraction/review. A real source change requires a new scan/selection.

## Bounded extraction and curation

Each command takes the repository through --root and the active --job. Use repeated --source arguments where supported; do not omit selection accidentally.

- extract_schemas.py --source src-NNNNNN --job job-NNNNNN documents the selected root schema and reachable supplied dependencies. Each exact message has one canonical binding; equal local type names in different namespaces remain separate. Missing imports/includes are explicit even when an XML library can compile without using them. No network resolver is used.
- extract_documents.py --source src-NNNNNN --job job-NNNNNN extracts DOCX/PDF evidence. --pdf-tables requests table detection; detection does not establish complete source coverage.
- extract_workbooks.py --source src-NNNNNN --job job-NNNNNN --resume preserves cell values, formulas, caches and drawing evidence. Check routing for a new code publication before execution. JSON code counts, root metadata, explicit edition fields and registered edition evidence come from that source; generic version fields are not publication editions. Conflicting editions stay unresolved. Missing values or publication identity receive a source/checksum-specific issue under the active job; no historical issue ID is assumed.
- link_business_evidence.py --selection FILE --job JOB and index_message_roles.py --selection FILE --job JOB update selected/affected exact definitions. Reconcile candidate evidence retained for curated pages; these parsers do not resolve semantic ambiguities automatically.

Extraction reuse requires the registered source checksum and the expected output files. Existing manually curated or reviewed pages are preserved; generated candidate evidence is not a second canonical definition. Merge necessary substantive changes with precise provenance and set affected review metadata truthfully. Keep business rules distinct from schema restrictions.

For supplied formats without a suitable bounded helper, inspect them with the appropriate document/PDF/spreadsheet/image tools and follow repository templates. Keep temporary extraction/rendering in work and durable assets in the owning output area's assets/<source-id>. Preserve all substantive table rows/notes and complete source figures, including vector/composite drawings. Each substantive diagram needs its original or crop, Mermaid, source location, semantic explanation and actual render/visual evidence. Use the repository's required Mermaid version/notation.

Shared dependency propagation follows explicit participant/flow/component identities and source evidence. A changed publication also seeds references citing its replaced source IDs, even before the new bytes have an allocated source ID; those references and their explicit consumers are fingerprinted in the selection. A new code publication does not repoint older messages to newer code meanings. Do not equate functional roles with institutions or merge same-label participants.

## Validate, record and report

    python -B -X utf8 "$kbRoot\tools\kb.py" --root "$kbRoot" rebuild --selection "$appliedSelection" --job "$jobId"
    python -B -X utf8 "$kbRoot\tools\kb.py" --root "$kbRoot" validate --selection "$appliedSelection" --job "$jobId" --checksums

Validation exits 0 when mechanical checks pass, 1 for findings, and 2 for invalid/stale input. Read its errors, conflicts and limitations; pass alone does not mean all substantive review is complete. Unregistered inputs outside the selection are reported separately. Full validate --checksums still checks whole-repository inventory completeness and is a different claim.

Review changed tables against their originals, reconcile diagram/table inventories, render Mermaid and compare source reconstructions visually. Recheck relevant sender/receiver responsibilities and flow links. Preserve valid historical review evidence for unchanged material; do not date or approve inspections that were not performed.

Record actual completed work and evidence in tracking/refresh/<job-id>/report.json. Maintain completed_work, review_evidence and known_gaps there with precise artifact/source locations. Registration creates an initial report; checkpoint-refresh merges these authored fields while updating its standard status, target, validation, conflicts, deferred inputs and next_action fields. It also attaches the existing per-job validation.json to the checkpoint, without treating it as substantive review.

Then update the checkpoint:

    python -B -X utf8 "$kbRoot\tools\kb.py" --root "$kbRoot" checkpoint-refresh --selection "$appliedSelection" --job "$jobId" --status needs-review --next 'Exact remaining action and its evidence location'

This command preserves unrelated tracking. It does not provide an automatic reviewed/completed switch. Finish to the evidence/tooling limits and state them clearly. Where every requested check is actually complete, update the job's review state with the evidence required by AGENTS.md; no extraction script grants that state.

Do not run checkpoint.py or finish_corpus_assessment.py for a selected refresh. Do not execute source-specific curators or review-recording scripts indiscriminately.

The final response should give the selected version/publication, added and reused sources, affected references, validation outcome, unresolved conflicts/reviews, deferred inputs, and checkpoint path. Give usable catalog links and lookup commands. Explicitly separate selected-scope success from corpus-wide completeness.
