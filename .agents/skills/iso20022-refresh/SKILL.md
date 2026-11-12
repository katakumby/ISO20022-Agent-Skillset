---
name: iso20022-refresh
description: Refresh selected ISO 20022 message definitions or message-set publication editions from newly supplied local raw files, preserving source provenance, canonical references, shared dependencies, and review history. Use for adding a version, incorporating corrected documentation, or resuming an incomplete refresh; ordinary knowledge lookup does not require this skill.
---

# ISO 20022 refresh

Maintain the existing knowledge base using local supplied evidence. This skill orchestrates the repository's focused helpers and source review; it does not download publications or run a corpus conversion automatically.

## Locate and understand the repository

Use the explicitly requested repository, otherwise the current workspace if it contains the ISO catalog and tools. Pass its resolved location through --root; do not create another knowledge base if it is unavailable.

Read AGENTS.md, catalog/README.md, the applicable domain/message-set index, templates/README.md, tools/README.md, tracking/checkpoint.json, and relevant source/job/issue records. Instructions from an earlier conversion are not evidence that the current bytes or outputs have been checked.

Read [the refresh workflow](references/refresh-workflow.md) before using refresh writers. Inspect the current helper --help interfaces; if the required scoped capability is absent, stop that writer and report the gap rather than substitute a corpus-wide script.

## Establish the target

Start with the read-only scan. For an unspecified refresh, show detected changes and ask the user to select an exact message definition or a publication edition. A family identifier is navigation, not an implicit choice of every version. Resolve ambiguous editions from the sources or ask for the intended target.

When the user already specified an unambiguous target, proceed without asking again. Inspect new document covers/headings and schema namespaces to establish routing and coverage. Publication edition and message definition version are independent.

Build an impact selection. Include only the selected sources, required supplied dependencies, and consumers linked by explicit evidence. Explain any expansion through shared participants, flows, headers or codes. Other detected files remain unregistered and unprocessed; mention them in the result.

## Refresh with provenance

Register the selected source contents with the next unused job ID. Reuse existing content identities and every verified occurrence; different bytes receive a new identity. Preserve old definitions, scoped participant identities, canonical paths, raw filenames and original bytes. Archives remain in place; extract only into work.

Use the applied selection and job for bounded extraction and downstream updates. Reuse verified unchanged work and repair missing outputs. Preserve hand-curated content and valid review evidence; reconcile proposed changes rather than overwrite reviewed pages. Apply source-grounded narrative, complete schema/type references, tables, participants, flows and diagram reconstructions following the repository templates.

Different supplied schemas claiming the same exact definition are unresolved candidates. Retain the existing canonical binding, record the conflict and request a decision for that item while continuing independent work. Do not select by file order, newest-looking filename, or version-number similarity.

## Validate and checkpoint

Rebuild derived indexes and run scoped validation. Also perform applicable semantic, table, diagram-rendering and visual checks; successful extraction or compilation is not a review result. Record missing MDR content, unavailable dependencies, uncertain source facts, and unavailable rendering faithfully.

Preserve the job's fingerprints and review evidence, update its checkpoint, and resume from that checkpoint on later runs. Report the selected scope, affected references, completed checks, conflicts, deferred files, unresolved limits, and exact next action. Distinguish a completed selected refresh from complete processing of all supplied files or availability of all desired knowledge.

Do not invoke source-specific curate_* or record_* scripts, the old corpus checkpoint generator, or the fixed corpus assessment merely because they exist. Review recording utilities require an inspection that actually occurred.
