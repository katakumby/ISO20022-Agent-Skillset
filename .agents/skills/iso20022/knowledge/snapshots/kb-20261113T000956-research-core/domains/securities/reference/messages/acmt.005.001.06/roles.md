---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "acmt.005.001.06 participant and direction evidence"
domain: "securities"
message_id: "acmt.005.001.06"
message_family: "acmt.005"
namespace: "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06"
source_ids: ["src-000096", "src-000101"]
message_sets: ["investment-funds"]
role_labels: ["account owner", "account servicer", "an account owner", "bank", "custodian", "designated agent", "investor", "registrar", "securities depository", "the account servicer", "transfer agent"]
search_terms: ["account owner", "account servicer", "an account owner", "bank", "custodian", "designated agent", "investor", "registrar", "securities depository", "the account servicer", "transfer agent"]
participant_ids: ["participant-narrative-src-000096-account-owner", "participant-narrative-src-000096-account-servicer", "participant-narrative-src-000096-bank", "participant-narrative-src-000096-designated-agent", "participant-narrative-src-000096-investor", "participant-narrative-src-000096-registrar", "participant-narrative-src-000096-securities-depository", "participant-src-000095-custodian", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "5 acmt.005.001.06 RequestForAccountManagementStatusReportV06", "file_pages": [77, 85]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# acmt.005.001.06 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 9 uniquely resolved participant references.

## src-000096 — 5 acmt.005.001.06 RequestForAccountManagementStatusReportV06

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp77; publication May 2026.

### Direction and initiation clauses

#### src-000096-acmt.005.001.06-p77-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p77, scope.

- Sender: **an account owner, for example, an investor or its designated agent**. [an account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md).
- Receiver: **the account servicer, for example, a registrar, transfer agent, custodian bank or securities depository**. [the account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md).

> The RequestForAccountManagementStatusReport message is sent by an account owner, for example, an investor or its designated agent, to the account servicer, for example, a registrar, transfer agent, custodian bank or securities depository to request the status of an AccountOpeningInstruction, GetAccountDetails or an AccountModificationInstruction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-acmt.005.001.06-p77-c001 — file p77, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md); [investor](../../../../../shared/reference/participants/participant-narrative-src-000096-investor.md); [designated agent](../../../../../shared/reference/participants/participant-narrative-src-000096-designated-agent.md); [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md); [registrar](../../../../../shared/reference/participants/participant-narrative-src-000096-registrar.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [custodian](../../../../../shared/reference/participants/participant-src-000095-custodian.md); [bank](../../../../../shared/reference/participants/participant-narrative-src-000096-bank.md); [securities depository](../../../../../shared/reference/participants/participant-narrative-src-000096-securities-depository.md).

Quoted above in src-000096-acmt.005.001.06-p77-c001-d1.

**src-000096-acmt.005.001.06-p77-c002 — file p77, usage.**

Reviewed clause disposition: **usage-condition-or-related-message-context**. The sentence supplies purpose, response linkage, timing, content, status or a condition. It does not independently identify an additional complete current-message sender/receiver direction. Its full literal wording remains available.

> The RequestForAccountManagementStatusReport message is used to request the processing status of a previously sent AccountOpeningInstruction, GetAccountDetails or an AccountModificationInstruction message for which an AccountDetailsConfirmation message has not yet been received.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
