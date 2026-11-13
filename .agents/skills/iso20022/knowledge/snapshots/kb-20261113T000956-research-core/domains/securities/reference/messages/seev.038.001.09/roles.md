---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "seev.038.001.09 participant and direction evidence"
domain: "securities"
message_id: "seev.038.001.09"
message_family: "seev.038"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09"
source_ids: ["src-000080", "src-000089"]
message_sets: ["corporate-actions"]
role_labels: ["account owner", "account servicer", "its designated agent", "third party"]
search_terms: ["account owner", "account servicer", "its designated agent", "third party"]
participant_ids: ["participant-corporate-actions-designated-agent", "participant-narrative-src-000080-third-party", "participant-src-000079-account-owner", "participant-src-000079-account-servicer"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000080", "heading": "10 seev.038.001.09 CorporateActionNarrativeV09", "file_pages": [692, 700]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# seev.038.001.09 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 4 uniquely resolved participant references.

## src-000080 — 10 seev.038.001.09 CorporateActionNarrativeV09

[src-000080](../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md); Functionality file pp692; publication February 2026.

### Direction and initiation clauses

#### src-000080-seev.038.001.09-p692-c001-d1

Kind: exchange-participants; message applicability: **current-message**; src-000080 file p692, scope.

- Exchange participants: **account servicer and account owner or its designated agent**. [account servicer](../../../../../shared/reference/participants/participant-src-000079-account-servicer.md); [account owner](../../../../../shared/reference/participants/participant-src-000079-account-owner.md); [its designated agent](../../../../../shared/reference/participants/participant-corporate-actions-designated-agent.md).

> The CorporateActionNarrative message is sent between an account servicer and an account owner or its designated agent to cater for such processes that cannot be handled using messages such as the CorporateActionNotification.

“Sent between” establishes participants, not an ordered sender/receiver direction. Designated agent remains an alternative to account owner.

#### src-000080-seev.038.001.09-p692-c004-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000080 file p692, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-narrative-src-000080-third-party.md).

> re-send to a third party a copy of a message for information (the sub-function of the message is Copy Duplicate), using the relevant elements in the business application header (BAH).

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000080-seev.038.001.09-p692-c001 — file p692, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/participant-src-000079-account-servicer.md); [account owner](../../../../../shared/reference/participants/participant-src-000079-account-owner.md); [its designated agent](../../../../../shared/reference/participants/participant-corporate-actions-designated-agent.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000080-seev.038.001.09-p692-c001-d1.

**src-000080-seev.038.001.09-p692-c002 — file p692, usage.**

Reviewed clause disposition: **resend-option-no-new-named-direction**. The source allows resending a previously sent message. This clause names no new sender or receiver; it is a usage option, not absent extraction of a direction.

> re-send a message previously sent (the sub-function of the message is Duplicate),

**src-000080-seev.038.001.09-p692-c003 — file p692, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000080-third-party.md).

> provide a third party with a copy of a message for information (the sub-function of the message is Copy),

**src-000080-seev.038.001.09-p692-c004 — file p692, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000080-third-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000080-seev.038.001.09-p692-c004-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p692, scope.**

> It is not to be used for event narrative as that should be included in the CorporateActionNotification.

**File p692, scope.**

> Examples of when the CorporateActionNarrative message may be used include tax reclaims, restrictions, documentation requirements.

**File p692, scope.**

> This message should only be used when bilaterally agreed.

**File p692, scope.**

> This message is bi-directional.

**File p692, usage.**

> The message may also be used to:

Functionality role scope was directly reviewed on 2026-11-09. No unstated sender/receiver is manufactured. Header composition, creation/distribution, source wording defects and action-only evidence remain distinct; curated Part1 flow evidence may supply broader context.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
