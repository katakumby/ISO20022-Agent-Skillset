---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "sese.019.001.09 participant and direction evidence"
domain: "securities"
message_id: "sese.019.001.09"
message_family: "sese.019"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.019.001.09"
source_ids: ["src-000096", "src-000135"]
message_sets: ["investment-funds"]
role_labels: ["an instructing party", "executing party", "initiating party", "instructing party", "investor", "the executing party", "transferee", "transferor"]
search_terms: ["an instructing party", "executing party", "initiating party", "instructing party", "investor", "the executing party", "transferee", "transferor"]
participant_ids: ["participant-narrative-src-000096-initiating-party", "participant-narrative-src-000096-investor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transferee", "participant-src-000095-transferor"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "39 sese.019.001.09 AccountHoldingInformationRequestV09", "file_pages": [1442, 1488]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# sese.019.001.09 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 6 uniquely resolved participant references.

## src-000096 — 39 sese.019.001.09 AccountHoldingInformationRequestV09

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp1442, 1443; publication May 2026.

### Direction and initiation clauses

#### src-000096-sese.019.001.09-p1442-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p1442, scope.

- Sender: **an instructing party, for example, a (new) plan manager (transferee)**. [an instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).
- Receiver: **the executing party, for example, a (old) plan manager (transferor), on behalf of the initiating party, for example, an investor (client)**. [the executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).

> The AccountHoldingInformationRequest message is sent by an instructing party, for example, a (new) plan manager (transferee), to the executing party, for example, a (old) plan manager (transferor), on behalf of the initiating party, for example, an investor (client), to request information about financial instruments held on behalf of the client.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-sese.019.001.09-p1442-c001 — file p1442, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [transferee](../../../../../shared/reference/participants/participant-src-000095-transferee.md); [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transferor](../../../../../shared/reference/participants/participant-src-000095-transferor.md); [initiating party](../../../../../shared/reference/participants/participant-narrative-src-000096-initiating-party.md); [investor](../../../../../shared/reference/participants/participant-narrative-src-000096-investor.md).

Quoted above in src-000096-sese.019.001.09-p1442-c001-d1.

**src-000096-sese.019.001.09-p1442-c002 — file p1442, usage.**

> The AccountHoldingInformationRequest message is used to request information about assets held on behalf of the client for which it intends to instruct a portfolio transfer at a later time.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
