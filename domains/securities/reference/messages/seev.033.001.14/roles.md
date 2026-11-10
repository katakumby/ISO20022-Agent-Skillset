---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "seev.033.001.14 participant and direction evidence"
domain: "securities"
message_id: "seev.033.001.14"
message_family: "seev.033"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.033.001.14"
source_ids: ["src-000080", "src-000084"]
message_sets: ["corporate-actions"]
role_labels: ["account owner", "account servicer", "an account owner", "an account servicer", "corporate", "custodian", "third party"]
search_terms: ["account owner", "account servicer", "an account owner", "an account servicer", "corporate", "custodian", "third party"]
participant_ids: ["participant-narrative-src-000080-corporate", "participant-narrative-src-000080-custodian", "participant-narrative-src-000080-third-party", "participant-src-000079-account-owner", "participant-src-000079-account-servicer"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000080", "heading": "5 seev.033.001.14 CorporateActionInstructionV14", "file_pages": [274, 319]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# seev.033.001.14 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 5 uniquely resolved participant references.

## src-000080 — 5 seev.033.001.14 CorporateActionInstructionV14

[src-000080](../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf); Functionality file pp274, 275; publication February 2026.

### Direction and initiation clauses

#### src-000080-seev.033.001.14-p274-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000080 file p274, scope.

- Sender: **an account owner**. [an account owner](../../../../../shared/reference/participants/participant-src-000079-account-owner.md).
- Receiver: **an account servicer**. [an account servicer](../../../../../shared/reference/participants/participant-src-000079-account-servicer.md).

> The CorporateActionInstruction message is sent by an account owner to an account servicer to instruct election on a corporate action event.

#### src-000080-seev.033.001.14-p274-c006-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000080 file p274, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-narrative-src-000080-third-party.md).

> re-send to a third party a copy of a message for information (the sub-function of the message is Copy Duplicate), using the relevant elements in the business application header (BAH).

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000080-seev.033.001.14-p274-c001 — file p274, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/participant-src-000079-account-owner.md); [account servicer](../../../../../shared/reference/participants/participant-src-000079-account-servicer.md); [corporate](../../../../../shared/reference/participants/participant-narrative-src-000080-corporate.md).

Quoted above in src-000080-seev.033.001.14-p274-c001-d1.

**src-000080-seev.033.001.14-p274-c002 — file p274, scope.**

Mentioned roles: [custodian](../../../../../shared/reference/participants/participant-narrative-src-000080-custodian.md); [account owner](../../../../../shared/reference/participants/participant-src-000079-account-owner.md); [corporate](../../../../../shared/reference/participants/participant-narrative-src-000080-corporate.md).

> This message is used to provide the custodian with instructions on how the account owner wishes to proceed with a corporate action event.

**src-000080-seev.033.001.14-p274-c003 — file p274, scope.**

> Instructions include investment decisions regarding the exercise of rights issues, the election of stock or cash when the option is available, and decisions on the conversion or tendering of securities.

**src-000080-seev.033.001.14-p274-c004 — file p274, usage.**

Reviewed clause disposition: **resend-option-no-new-named-direction**. The source allows resending a previously sent message. This clause names no new sender or receiver; it is a usage option, not absent extraction of a direction.

> re-send a message previously sent (the sub-function of the message is Duplicate),

**src-000080-seev.033.001.14-p274-c005 — file p274, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000080-third-party.md).

> provide a third party with a copy of a message for information (the sub-function of the message is Copy),

**src-000080-seev.033.001.14-p274-c006 — file p274, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000080-third-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000080-seev.033.001.14-p274-c006-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p274, usage.**

> The message may also be used to:

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
