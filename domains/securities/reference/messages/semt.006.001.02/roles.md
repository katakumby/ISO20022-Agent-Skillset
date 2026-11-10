---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "semt.006.001.02 participant and direction evidence"
domain: "securities"
message_id: "semt.006.001.02"
message_family: "semt.006"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.006.001.02"
source_ids: ["src-000096", "src-000118"]
message_sets: ["investment-funds"]
role_labels: ["account owner", "account servicer", "An account servicer", "authorised representative", "investment manager", "the account owner", "transfer agent"]
search_terms: ["account owner", "account servicer", "An account servicer", "authorised representative", "investment manager", "the account owner", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-authorised-representative", "participant-narrative-src-000096-account-owner", "participant-narrative-src-000096-account-servicer", "participant-narrative-src-000096-investment-manager", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02", "file_pages": [408, 426]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# semt.006.001.02 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 5 uniquely resolved participant references.

## src-000096 — 22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); Functionality file pp408, 409; publication May 2026.

### Direction and initiation clauses

#### src-000096-semt.006.001.02-p408-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p408, scope.

- Sender: **An account servicer, for example, a transfer agent**. [An account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md).
- Receiver: **the account owner, for example, an investment manager or its authorised representative**. [the account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md).

> An account servicer, for example, a transfer agent sends the StatementOfInvestmentFundTransactions message to the account owner, for example, an investment manager or its authorised representative to provide detailed transactions (increases and decreases) of holdings which occurred during a specified period of time.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-semt.006.001.02-p408-c001 — file p408, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representative](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md).

Literal actions: transfer agent sends.

Quoted above in src-000096-semt.006.001.02-p408-c001-d1.

**src-000096-semt.006.001.02-p408-c002 — file p408, usage.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md).

> This message should be used at a frequency agreed bi-laterally between the account servicer and the account owner.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p408, usage.**

> The StatementOfInvestmentFundTransactions message is used to list the holdings transactions of a single (master) account or several sub-accounts.

**File p408, usage.**

> This message must not be used in place of confirmation messages.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
