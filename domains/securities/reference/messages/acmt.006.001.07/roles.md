---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "acmt.006.001.07 participant and direction evidence"
domain: "securities"
message_id: "acmt.006.001.07"
message_family: "acmt.006"
namespace: "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07"
source_ids: ["src-000096", "src-000102"]
message_sets: ["investment-funds"]
role_labels: ["account owner", "account servicer", "an account servicer", "bank", "custodian", "designated agent", "investor", "its designated agent", "registrar", "securities depository", "the account owner", "transfer agent"]
search_terms: ["account owner", "account servicer", "an account servicer", "bank", "custodian", "designated agent", "investor", "its designated agent", "registrar", "securities depository", "the account owner", "transfer agent"]
participant_ids: ["participant-narrative-src-000096-account-owner", "participant-narrative-src-000096-account-servicer", "participant-narrative-src-000096-bank", "participant-narrative-src-000096-designated-agent", "participant-narrative-src-000096-investor", "participant-narrative-src-000096-registrar", "participant-narrative-src-000096-securities-depository", "participant-src-000095-custodian", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "6 acmt.006.001.07 AccountManagementStatusReportV07", "file_pages": [86, 93]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# acmt.006.001.07 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 9 uniquely resolved participant references.

## src-000096 — 6 acmt.006.001.07 AccountManagementStatusReportV07

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); Functionality file pp86; publication May 2026.

### Direction and initiation clauses

#### src-000096-acmt.006.001.07-p86-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p86, scope.

- Sender: **an account servicer, for example, a registrar, transfer agent, custodian bank or securities depository**. [an account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md).
- Receiver: **the account owner or its designated agent, for example, an investor**. [the account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md); [its designated agent](../../../../../shared/reference/participants/participant-narrative-src-000096-designated-agent.md).

> The AccountManagementStatusReport message is sent by an account servicer, for example, a registrar, transfer agent, custodian bank or securities depository to the account owner or its designated agent, for example, an investor to report on the receipt or the processing status of a previously received account management message.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-acmt.006.001.07-p86-c001 — file p86, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md); [registrar](../../../../../shared/reference/participants/participant-narrative-src-000096-registrar.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [custodian](../../../../../shared/reference/participants/participant-src-000095-custodian.md); [bank](../../../../../shared/reference/participants/participant-narrative-src-000096-bank.md); [securities depository](../../../../../shared/reference/participants/participant-narrative-src-000096-securities-depository.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md); [designated agent](../../../../../shared/reference/participants/participant-narrative-src-000096-designated-agent.md); [investor](../../../../../shared/reference/participants/participant-narrative-src-000096-investor.md).

Quoted above in src-000096-acmt.006.001.07-p86-c001-d1.

**src-000096-acmt.006.001.07-p86-c002 — file p86, usage.**

Reviewed clause disposition: **usage-condition-or-related-message-context**. The sentence supplies purpose, response linkage, timing, content, status or a condition. It does not independently identify an additional complete current-message sender/receiver direction. Its full literal wording remains available.

> The AccountManagementStatusReport message is used to provide the status of a previously received AccountOpeningInstruction, an AccountModificationInstruction or a GetAccountDetails message.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p86, usage.**

> It may also be used to report the status of the account.

**File p86, usage.**

> The AccountManagementStatusReport message is also used to reject an AccountOpeningInstruction, AccountModificationInstruction or GetAccountDetails message when the message is not compliant with the agreed SLA or when the account cannot be uniquely identified.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
