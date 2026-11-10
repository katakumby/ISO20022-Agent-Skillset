---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "pacs.010.001.06 participant and direction evidence"
domain: "payments"
message_id: "pacs.010.001.06"
message_family: "pacs.010"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06"
source_ids: ["src-000163", "src-000171"]
message_sets: ["payments-clearing-and-settlement"]
role_labels: ["a financial institution", "agent", "agents", "an exchange", "clearing house", "creditor", "debtor", "DebtorAgent", "exchange", "financial institution", "financial institutions", "the DebtorAgent"]
search_terms: ["a financial institution", "agent", "agents", "an exchange", "clearing house", "creditor", "debtor", "DebtorAgent", "exchange", "financial institution", "financial institutions", "the DebtorAgent"]
participant_ids: ["participant-functionality-src-000163-agent", "participant-narrative-src-000163-financial-institution", "participant-src-000162-clearing-house", "participant-src-000162-creditor", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-exchange", "participant-src-000162-financial-institution"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000163", "heading": "8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "file_pages": [1016, 1048]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# pacs.010.001.06 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 8 uniquely resolved participant references.

## src-000163 — 8 pacs.010.001.06 FinancialInstitutionDirectDebitV06

[src-000163](../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md); Functionality file pp1016; publication March 2026.

### Direction and initiation clauses

#### src-000163-pacs.010.001.06-p1016-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000163 file p1016, scope.

- Sender: **an exchange or clearing house, or a financial institution, directly or through another agent**. [an exchange](../../../../../shared/reference/participants/participant-src-000162-exchange.md); [clearing house](../../../../../shared/reference/participants/participant-src-000162-clearing-house.md); [a financial institution](../../../../../shared/reference/participants/participant-src-000162-financial-institution.md).
- Receiver: **the DebtorAgent**. [the DebtorAgent](../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md).

> The FinancialInstitutionDirectDebit message is sent by an exchange or clearing house, or a financial institution, directly or through another agent, to the DebtorAgent.

#### src-000163-pacs.010.001.06-p1016-c003-d1

Kind: exchange-participants; message applicability: **current-message**; src-000163 file p1016, usage.

- Exchange participants: **agents**. [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md).

> The FinancialInstitutionDirectDebit message is exchanged between agents and can contain one or more financial institution direct debit instruction(s) for one or more creditor(s).

An exchange-between statement establishes participation, not sender/receiver direction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000163-pacs.010.001.06-p1016-c001 — file p1016, scope.**

Mentioned roles: [exchange](../../../../../shared/reference/participants/participant-src-000162-exchange.md); [clearing house](../../../../../shared/reference/participants/participant-src-000162-clearing-house.md); [financial institution](../../../../../shared/reference/participants/participant-src-000162-financial-institution.md); [agent](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md); [DebtorAgent](../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md).

Quoted above in src-000163-pacs.010.001.06-p1016-c001-d1.

**src-000163-pacs.010.001.06-p1016-c002 — file p1016, scope.**

Mentioned roles: [DebtorAgent](../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md); [debtor](../../../../../shared/reference/participants/participant-src-000162-debtor.md); [creditor](../../../../../shared/reference/participants/participant-src-000162-creditor.md); [debtor](../../../../../shared/reference/participants/participant-src-000162-debtor.md); [creditor](../../../../../shared/reference/participants/participant-src-000162-creditor.md); [financial institutions](../../../../../shared/reference/participants/participant-narrative-src-000163-financial-institution.md).

> It is used to instruct the DebtorAgent to move funds from one or more debtor(s) account(s) to one or more creditor(s), where both debtor and creditor are financial institutions.

**src-000163-pacs.010.001.06-p1016-c003 — file p1016, usage.**

Mentioned roles: [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md); [financial institution](../../../../../shared/reference/participants/participant-src-000162-financial-institution.md); [creditor](../../../../../shared/reference/participants/participant-src-000162-creditor.md).

Quoted above in src-000163-pacs.010.001.06-p1016-c003-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p1016, usage.**

> The FinancialInstitutionDirectDebit message can be used in domestic and cross-border scenarios.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
