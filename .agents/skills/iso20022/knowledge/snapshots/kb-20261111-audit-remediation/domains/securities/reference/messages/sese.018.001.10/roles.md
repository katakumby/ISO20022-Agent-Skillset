---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "sese.018.001.10 participant and direction evidence"
domain: "securities"
message_id: "sese.018.001.10"
message_family: "sese.018"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.018.001.10"
source_ids: ["src-000096", "src-000134"]
message_sets: ["investment-funds"]
role_labels: ["an executing party", "executing party", "instructing party", "the instructing party", "transferee", "transferor"]
search_terms: ["an executing party", "executing party", "instructing party", "the instructing party", "transferee", "transferor"]
participant_ids: ["participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transferee", "participant-src-000095-transferor"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "38 sese.018.001.10 AccountHoldingInformationV10", "file_pages": [1308, 1441]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# sese.018.001.10 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 4 uniquely resolved participant references.

## src-000096 — 38 sese.018.001.10 AccountHoldingInformationV10

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp1308, 1309; publication May 2026.

### Direction and initiation clauses

#### src-000096-sese.018.001.10-p1308-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p1308, scope.

- Sender: **an executing party, for example, a (old) plan manager (transferor)**. [an executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).
- Receiver: **the instructing party, for example, a (new) plan manager (transferee)**. [the instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).

> The AccountHoldingInformation message is sent by an executing party, for example, a (old) plan manager (transferor), to the instructing party, for example, a (new) plan manager (transferee), to provide information about financial instruments held on behalf of a client.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-sese.018.001.10-p1308-c001 — file p1308, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transferor](../../../../../shared/reference/participants/participant-src-000095-transferor.md); [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [transferee](../../../../../shared/reference/participants/participant-src-000095-transferee.md).

Quoted above in src-000096-sese.018.001.10-p1308-c001-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p1308, usage.**

> The AccountHoldingInformation message is used to provide information on the individual assets held in a client's account.

**File p1308, usage.**

> The assets may be part of a tax efficient product, a pension of general investment product.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
