---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "acmt.003.001.08 participant and direction evidence"
domain: "securities"
message_id: "acmt.003.001.08"
message_family: "acmt.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08"
source_ids: ["src-000096", "src-000100"]
message_sets: ["investment-funds"]
role_labels: ["account owner", "account servicer", "an account owner", "bank", "beneficiary", "custodian", "designated agent", "investor", "registrar", "securities depository", "the account servicer", "transfer agent"]
search_terms: ["account owner", "account servicer", "an account owner", "bank", "beneficiary", "custodian", "designated agent", "investor", "registrar", "securities depository", "the account servicer", "transfer agent"]
participant_ids: ["participant-narrative-src-000096-account-owner", "participant-narrative-src-000096-account-servicer", "participant-narrative-src-000096-bank", "participant-narrative-src-000096-beneficiary", "participant-narrative-src-000096-designated-agent", "participant-narrative-src-000096-investor", "participant-narrative-src-000096-registrar", "participant-narrative-src-000096-securities-depository", "participant-src-000095-custodian", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "4 acmt.003.001.08 AccountModificationInstructionV08", "file_pages": [57, 76]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# acmt.003.001.08 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 10 uniquely resolved participant references.

## src-000096 — 4 acmt.003.001.08 AccountModificationInstructionV08

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); Functionality file pp57, 58; publication May 2026.

### Direction and initiation clauses

#### src-000096-acmt.003.001.08-p57-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p57, scope.

- Sender: **an account owner, for example, an investor or its designated agent**. [an account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md).
- Receiver: **the account servicer, for example, a registrar, transfer agent, custodian bank or securities depository**. [the account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md).

> The AccountModificationInstruction message is sent by an account owner, for example, an investor or its designated agent to the account servicer, for example, a registrar, transfer agent, custodian bank or securities depository to modify, that is, create, update or delete specific details of an existing account.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-acmt.003.001.08-p57-c001 — file p57, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md); [investor](../../../../../shared/reference/participants/participant-narrative-src-000096-investor.md); [designated agent](../../../../../shared/reference/participants/participant-narrative-src-000096-designated-agent.md); [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md); [registrar](../../../../../shared/reference/participants/participant-narrative-src-000096-registrar.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [custodian](../../../../../shared/reference/participants/participant-src-000095-custodian.md); [bank](../../../../../shared/reference/participants/participant-narrative-src-000096-bank.md); [securities depository](../../../../../shared/reference/participants/participant-narrative-src-000096-securities-depository.md).

Quoted above in src-000096-acmt.003.001.08-p57-c001-d1.

**src-000096-acmt.003.001.08-p57-c002 — file p57, usage.**

Mentioned roles: [beneficiary](../../../../../shared/reference/participants/participant-narrative-src-000096-beneficiary.md).

> maintain/update any of the existing account details, for example, to update the address of the beneficiary or modify the preference to income from distribution to capitalisation, or,

**src-000096-acmt.003.001.08-p57-c003 — file p57, usage.**

> add/create specific details to the existing account when these details were not yet recorded at the time of account creation, for example, to add a second address or to establish new cash settlement standing instructions, or,

**src-000096-acmt.003.001.08-p57-c004 — file p57, usage.**

> delete specific account details, for example, delete cash standing instructions, or,

**src-000096-acmt.003.001.08-p57-c005 — file p57, usage.**

> instruct a change to the status of the account, for example, instruct the closure of the account.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p57, usage.**

> The AccountModificationInstruction message is used to modify the details of an existing account.

**File p57, usage.**

> The AccountModificationInstruction message can be used to:

**File p57, usage.**

> The usage of this message may be subject to service level agreement (SLA) between the counterparties.

**File p57, usage.**

> Execution of the AccountModificationInstruction is confirmed via an AccountDetailsConfirmation message.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
