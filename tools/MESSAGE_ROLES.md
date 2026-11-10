# Exact-message participant and direction evidence

Start in the repository directory; `$kbRoot` can also be set explicitly when running from elsewhere:

```powershell
$kbRoot = (Get-Location).Path
python "$kbRoot\tools\index_message_roles.py" --root "$kbRoot"
python "$kbRoot\tools\audit_message_roles.py" --root "$kbRoot"
```

The helper reads the registered source manifest, canonical schema message identities, exact MDR definition manifests and PDF page text under `work/documents/`. It reads participant labels from the maintained shared participant pages. It writes focused `roles.md` pages beside canonical message references, appends one generated navigation link to each message index, and derives `catalog/message-roles.json` for bounded lookup. It does not modify supplied inputs or curated message context.

The catalog contains one record per exact supplied schema message, including schema-only and extraction-pending records. Each direction, initiation or exchange claim carries the exact message ID, publication source ID, source checksum, heading, one-based file pages and full source sentence. Source occurrences preserve loose/archive provenance. Separate publications remain separate evidence claims. The family identifier is navigation metadata only.

Use `message_target` when interpreting a claim:

- `current-message`: the sentence explicitly names the current message or uses “the/this message”.
- `current-message-scope-name-variant`: the exact definition's Scope spells out a message name differently, such as FinancialInstitutionToFinancialInstitution versus FIToFI. This is local evidence, not an alias applied to other publications.
- `anaphoric-context-needs-review`: pronoun or generic reference requires contextual review.
- `related-or-unspecified-message`: retained context; do not treat it as a direction of the indexed message.

Claims distinguish sender-to-receiver, receiver-only, initiator and exchange participants. “Exchanged between” does not establish direction. A sender is not assumed to be an initiator. Literal actions retain their full source sentence and are not automatically actions on the indexed message. Institutional examples and routing qualifiers stay in the original expression. Role alternatives and conjunctions are retained rather than silently choosing one recipient.

The role keys also include `creator`, `distribution_recipient` and `intermediary`. A source that says ESMA creates a report for distribution to national competent authorities establishes creation and intended distribution; it does not automatically establish the wire sender. Routing through a matching utility is recorded separately from sender and receiver. An explicit “and vice versa” creates two qualified directions, not a participant called “vice versa”. Parenthetical examples are kept in the quoted evidence while complete functional labels remain intact.

Additional `message_target` values deliberately preserve scope: `current-message-copy-or-copyduplicate-option`, `current-message-conditional-return`, `current-message-source-examples`, `current-message-qualified-source-wording`, `original-message-in-duplicate-option`, `related-response-message`, and `business-message-with-accompanying-header`. Read the value and limitation instead of treating every claim on the page as the main message direction. Conditional responses can reverse the servicing roles; an informational-copy recipient does not establish the sender of that copy. A source typo remains in the literal quote with a qualification.

Participant resolution uses explicit source labels/aliases within the same source or message-set publication context. Matching labels from unrelated publications are not merged. Two pilot narrative labels have a narrow documented mapping to the already curated same-source account-owner/account-servicer references, supported by src-000197 file p491. Unmatched labels and multiple candidates remain unresolved. Full Scope/Usage narrative is retained on the reference page, including sentences not classified as roles, so extraction gaps stay inspectable.

`catalog/participant-role-overrides.json` may select one existing exact-label, in-scope candidate using the full message ID, effective source ID, normalized role label and exact quoted-sentence SHA-256. Each selection retains its source locations and rationale. The resolver fails if a selection is ambiguous or is not an eligible candidate. For the combined T2S publication, effective child scope is used only after the same complete sentence has independently matched under the same exact message ID. This is not a general cross-publication equivalence rule.

`tracking/reviews/message-role-clause-decisions.json` maintains directly reviewed, source-checksummed clause decisions. Each record includes the exact quote/hash, definition, file pages, disposition, and any explicit role/action additions. The initial review covers all 364 flagged occurrences (144 different sentences) and the 21 publications that initially lacked parsed directions. Resend options without named parties, status values, report coverage, timing and prohibitions remain retrievable with explicit dispositions. New or changed quotes receive no inherited review. `source-does-not-state-complete-direction` means the Functionality was read and does not supply a complete pair; it is not a claim that the broader message has no actors. All page and claim statuses still remain `needs-review` for unresolved semantic/contextual qualifications.

`work/message-roles/<full-message-id>.json` preserves detailed extraction units and review items. `tracking/reviews/message-role-coverage.json` reconciles canonical schema coverage; it is not a semantic-review certificate. `work/message-roles/review-items.json` lists unresolved labels, unparsed clauses and missing boundaries. All generated role pages remain `needs-review`.

Re-run after PDF extraction or participant metadata changes; completed pages are reused by their source fingerprints. Existing generated pages are backed up through the repository write helper before replacement. Definition-manifest checksums in the catalog identify the exact extraction snapshot. The source checksum in each page-text extraction must match the source register or the helper stops.
