---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "admi.006.001.01 participant and direction evidence"
domain: "shared"
message_id: "admi.006.001.01"
message_family: "admi.006"
namespace: "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01"
source_ids: ["src-000233", "src-000238", "src-000344"]
message_sets: ["t2s", "t2s-administration"]
role_labels: ["A system member", "any parties authorised by them", "Central System", "requesting party", "system member", "the Central System"]
search_terms: ["A system member", "any parties authorised by them", "Central System", "requesting party", "system member", "the Central System"]
participant_ids: ["participant-functionality-src-000344-central-system", "participant-functionality-src-000344-party-authorised-by-system-member", "participant-functionality-src-000344-requesting-party", "participant-src-000343-system-member"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "3 admi.006.001.01 ResendRequestV01", "file_pages": [57, 61]}, {"source_id": "src-000344", "heading": "3 admi.006.001.01 ResendRequestV01", "file_pages": [27, 31]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# admi.006.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 4 uniquely resolved participant references.

## src-000233 — 3 admi.006.001.01 ResendRequestV01

[src-000233](../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp57; publication August 2026.

### Direction and initiation clauses

#### src-000233-admi.006.001.01-p57-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p57, scope.

- Sender: **A system member or any parties authorised by them**. [A system member](../../participants/participant-src-000343-system-member.md); [any parties authorised by them](../../participants/participant-functionality-src-000344-party-authorised-by-system-member.md).
- Receiver: **the Central System (such as the T2S platform)**. [the Central System](../../participants/participant-functionality-src-000344-central-system.md).

> A system member or any parties authorised by them send a ResendRequest message to the Central System (such as the T2S platform).

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-admi.006.001.01-p57-c001 — file p57, scope.**

Mentioned roles: [system member](../../participants/participant-src-000343-system-member.md); [any parties authorised by them](../../participants/participant-functionality-src-000344-party-authorised-by-system-member.md); [Central System](../../participants/participant-functionality-src-000344-central-system.md).

Literal actions: any parties authorised by them send.

Quoted above in src-000233-admi.006.001.01-p57-c001-d1.

**src-000233-admi.006.001.01-p57-c002 — file p57, scope.**

Mentioned roles: [requesting party](../../participants/participant-functionality-src-000344-requesting-party.md).

Literal actions: requesting party wants to receive.

Reviewed clause disposition: **source-explicit-role-action**. The actor and action are named in this sentence; the action object and conditions are retained and are not automatically the indexed message.

> The purpose of this request is, that the requesting party wants to receive the "original" message once again.

**src-000233-admi.006.001.01-p57-c003 — file p57, scope.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> This might be caused through technical problems on the receiving side (message could not be received or processed or is missing in the message sequencing) or for archiving purposes.

## src-000344 — 3 admi.006.001.01 ResendRequestV01

[src-000344](../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`; Functionality file pp27; publication march-2024.

### Direction and initiation clauses

#### src-000344-admi.006.001.01-p27-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000344 file p27, scope.

- Sender: **A system member or any parties authorised by them**. [A system member](../../participants/participant-src-000343-system-member.md); [any parties authorised by them](../../participants/participant-functionality-src-000344-party-authorised-by-system-member.md).
- Receiver: **the Central System (such as the T2S platform)**. [the Central System](../../participants/participant-functionality-src-000344-central-system.md).

> A system member or any parties authorised by them send a ResendRequest message to the Central System (such as the T2S platform).

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000344-admi.006.001.01-p27-c001 — file p27, scope.**

Mentioned roles: [system member](../../participants/participant-src-000343-system-member.md); [any parties authorised by them](../../participants/participant-functionality-src-000344-party-authorised-by-system-member.md); [Central System](../../participants/participant-functionality-src-000344-central-system.md).

Literal actions: any parties authorised by them send.

Quoted above in src-000344-admi.006.001.01-p27-c001-d1.

**src-000344-admi.006.001.01-p27-c002 — file p27, scope.**

Mentioned roles: [requesting party](../../participants/participant-functionality-src-000344-requesting-party.md).

Literal actions: requesting party wants to receive.

Reviewed clause disposition: **source-explicit-role-action**. The actor and action are named in this sentence; the action object and conditions are retained and are not automatically the indexed message.

> The purpose of this request is, that the requesting party wants to receive the "original" message once again.

**src-000344-admi.006.001.01-p27-c003 — file p27, scope.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> This might be caused through technical problems on the receiving side (message could not be received or processed or is missing in the message sequencing) or for archiving purposes.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../tracking/issues.md)
