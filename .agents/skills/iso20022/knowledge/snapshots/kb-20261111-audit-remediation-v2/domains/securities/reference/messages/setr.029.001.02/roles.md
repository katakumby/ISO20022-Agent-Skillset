---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "setr.029.001.02 participant and direction evidence"
domain: "securities"
message_id: "setr.029.001.02"
message_family: "setr.029"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.029.001.02"
source_ids: ["src-000181", "src-000185"]
message_sets: ["post-trade-matching"]
role_labels: ["affirming party", "an executing party", "an instructing party", "broker/dealer", "Central Matching Utility (CMU)", "custodian", "executing party", "Executing Party", "Instructing Party", "Instructing party", "instructing party", "intermediary", "investment manager", "investors"]
search_terms: ["affirming party", "an executing party", "an instructing party", "broker/dealer", "Central Matching Utility (CMU)", "custodian", "executing party", "Executing Party", "Instructing Party", "Instructing party", "instructing party", "intermediary", "investment manager", "investors"]
participant_ids: ["participant-narrative-src-000181-broker-dealer", "participant-narrative-src-000181-executing-party", "participant-narrative-src-000181-intermediary", "participant-narrative-src-000181-investor", "participant-src-000180-affirming-party", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-custodian", "participant-src-000180-instructing-party", "participant-src-000180-investment-manager"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000181", "heading": "4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02", "file_pages": [140, 147]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# setr.029.001.02 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 9 uniquely resolved participant references.

## src-000181 — 4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02

[src-000181](../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md); Functionality file pp140; publication February 2025.

### Direction and initiation clauses

#### src-000181-setr.029.001.02-p140-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000181 file p140, scope.

- Sender: **an executing party**. [an executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md).
- Receiver: **an instructing party directly or through Central Matching Utility (CMU)**. [an instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md).

> Sent by an executing party to an instructing party directly or through Central Matching Utility (CMU) to cancel the referenced SecuritiesTradeConfirmation message that was previously sent.

#### src-000181-setr.029.001.02-p140-c004-d1

Kind: sender-to-receiver; message applicability: **related-previous-trade-confirmation**; src-000181 file p140, scope.

- Sender: **executing party or instructing party**. [executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md).
- Receiver: **custodian or affirming party**. [custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md); [affirming party](../../../../../shared/reference/participants/participant-src-000180-affirming-party.md).

> It may also be used to cancel the trade confirmation previously sent from an executing party or an instructing party to a custodian or an affirming party directly or through CMU.

This is the previously sent confirmation being cancelled. Direct/CMU routing alternatives remain in the source quote.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000181-setr.029.001.02-p140-c001 — file p140, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md); [Central Matching Utility (CMU)](../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md).

Quoted above in src-000181-setr.029.001.02-p140-c001-d1.

**src-000181-setr.029.001.02-p140-c002 — file p140, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-src-000180-investment-manager.md); [intermediary](../../../../../shared/reference/participants/participant-narrative-src-000181-intermediary.md); [investment manager](../../../../../shared/reference/participants/participant-src-000180-investment-manager.md); [investors](../../../../../shared/reference/participants/participant-narrative-src-000181-investor.md).

> The instructing party is typically the investment manager or an intermediary system/vendor communicating on behalf of the investment manager or of other categories of investors.

**src-000181-setr.029.001.02-p140-c003 — file p140, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [broker/dealer](../../../../../shared/reference/participants/participant-narrative-src-000181-broker-dealer.md); [intermediary](../../../../../shared/reference/participants/participant-narrative-src-000181-intermediary.md); [broker/dealer](../../../../../shared/reference/participants/participant-narrative-src-000181-broker-dealer.md).

> The executing party is typically the broker/dealer or an intermediary system/vendor communicating on behalf of the broker/dealer.

**src-000181-setr.029.001.02-p140-c004 — file p140, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md); [custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md); [affirming party](../../../../../shared/reference/participants/participant-src-000180-affirming-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000181-setr.029.001.02-p140-c004-d1.

**src-000181-setr.029.001.02-p140-c005 — file p140, usage.**

Mentioned roles: [Executing Party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [Instructing Party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md).

> Initiator: Both in local and central matching, the Initiator may be either the Executing Party or Instructing Party.

**src-000181-setr.029.001.02-p140-c006 — file p140, usage.**

Mentioned roles: [Instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md); [custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md); [affirming party](../../../../../shared/reference/participants/participant-src-000180-affirming-party.md).

> Respondent: Instructing party, a custodian or an affirming party optionally responds with SecuritiesTradeConfirmationResponse (accept or reject) message.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p140, scope.**

> The ISO 20022 Business Application Header must be used

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
