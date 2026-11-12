---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "acmt.002.001.08 participant and direction evidence"
domain: "securities"
message_id: "acmt.002.001.08"
message_family: "acmt.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08"
source_ids: ["src-000096", "src-000099"]
message_sets: ["investment-funds"]
role_labels: ["account owner", "account servicer", "an account servicer", "bank", "custodian", "investor", "registrar", "securities depository", "the account owner", "transfer agent"]
search_terms: ["account owner", "account servicer", "an account servicer", "bank", "custodian", "investor", "registrar", "securities depository", "the account owner", "transfer agent"]
participant_ids: ["participant-narrative-src-000096-account-owner", "participant-narrative-src-000096-account-servicer", "participant-narrative-src-000096-bank", "participant-narrative-src-000096-investor", "participant-narrative-src-000096-registrar", "participant-narrative-src-000096-securities-depository", "participant-src-000095-custodian", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "3 acmt.002.001.08 AccountDetailsConfirmationV08", "file_pages": [38, 56]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# acmt.002.001.08 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 8 uniquely resolved participant references.

## src-000096 — 3 acmt.002.001.08 AccountDetailsConfirmationV08

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp38, 39; publication May 2026.

### Direction and initiation clauses

#### src-000096-acmt.002.001.08-p38-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p38, scope.

- Sender: **an account servicer, for example, a registrar, transfer agent, custodian bank or securities depository**. [an account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md).
- Receiver: **the account owner, for example, an investor**. [the account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md).

> The AccountDetailsConfirmation message is sent by an account servicer, for example, a registrar, transfer agent, custodian bank or securities depository to the account owner, for example, an investor to confirm the opening of an account, execution of an AccountModificationInstruction or to return information requested in a GetAccountDetails message.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-acmt.002.001.08-p38-c001 — file p38, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md); [registrar](../../../../../shared/reference/participants/participant-narrative-src-000096-registrar.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [custodian](../../../../../shared/reference/participants/participant-src-000095-custodian.md); [bank](../../../../../shared/reference/participants/participant-narrative-src-000096-bank.md); [securities depository](../../../../../shared/reference/participants/participant-narrative-src-000096-securities-depository.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md); [investor](../../../../../shared/reference/participants/participant-narrative-src-000096-investor.md).

Quoted above in src-000096-acmt.002.001.08-p38-c001-d1.

**src-000096-acmt.002.001.08-p38-c002 — file p38, usage.**

Reviewed clause disposition: **usage-condition-or-related-message-context**. The sentence supplies purpose, response linkage, timing, content, status or a condition. It does not independently identify an additional complete current-message sender/receiver direction. Its full literal wording remains available.

> The AccountDetailsConfirmation message is used to confirm the opening of an account, modification of an account or the provision of information requested in a previously sent GetAccountDetails message.

**src-000096-acmt.002.001.08-p38-c003 — file p38, usage.**

> When the AccountModificationInstruction message is used to instruct the closure of an account, the AccountDetailsConfirmation message is used to confirm the account has been closed.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p38, usage.**

> The message contains detailed information relevant to the opened account.

**File p38, usage.**

> When the AccountDetailsConfirmation is used to confirm execution of an AccountModificationInstruction message, it may:

**File p38, usage.**

> contain the modified subsets of account details that were specified in the AccountModificationInstruction, and/or

**File p38, usage.**

> provide the status of the account.

**File p38, usage.**

> When the AccountDetailsConfirmation is used to reply to a GetAccountDetails message, it returns the selected subsets of account details that were specified in the GetAccountDetails message.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
