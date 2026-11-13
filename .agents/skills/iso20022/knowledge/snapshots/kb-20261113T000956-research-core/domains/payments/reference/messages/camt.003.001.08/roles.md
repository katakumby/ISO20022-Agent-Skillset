---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.003.001.08 participant and direction evidence"
domain: "payments"
message_id: "camt.003.001.08"
message_family: "camt.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.003.001.08"
source_ids: ["src-000015", "src-000017"]
message_sets: ["cash-management"]
role_labels: ["a member", "member", "the transaction administrator", "transaction administrator"]
search_terms: ["a member", "member", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "2 camt.003.001.08 GetAccountV08", "file_pages": [13, 47]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.003.001.08 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 2 camt.003.001.08 GetAccountV08

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp13, 14; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.003.001.08-p13-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p13, scope.

- Sender: **a member**. [a member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).
- Receiver: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The GetAccount message is sent by a member to the transaction administrator.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.003.001.08-p13-c001 — file p13, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Quoted above in src-000015-camt.003.001.08-p13-c001-d1.

**src-000015-camt.003.001.08-p13-c002 — file p13, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> It is used to request information on the details of one or more accounts held at the transaction administrator, including information on the balances.

**src-000015-camt.003.001.08-p13-c003 — file p13, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: transaction administrator maintains.

> At any time during the operating hours of the system, the member can query the transaction administrator to get information about the account(s) that the transaction administrator maintains for the member.

**src-000015-camt.003.001.08-p13-c004 — file p13, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: member request.

> The member can request information about accounts through a series of criteria, corresponding to the known information stored at the transaction administrator.

**src-000015-camt.003.001.08-p13-c005 — file p13, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member request.

> The member can request information based on the following elements:

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p13, usage.**

> For example, this may be necessary in order to perform the appropriate liquidity management and the funds transfers between accounts.

**File p13, usage.**

> The query can concern one or more specific accounts, accounts of a particular identification, or a particular type.

**File p13, usage.**

> The purpose of the query may be to obtain one or more types of balance.

**File p13, usage.**

> account identification

**File p13, usage.**

> account type (this element can be used to refine the query when the account identification represents, for example, a group of accounts)

**File p13, usage.**

> balance type (if not present, all balances are requested)

**File p13, usage.**

> type of counterparty: bilateral or multilateral (note that, by default, a balance is multilateral unless a particular counterparty is specified)

**File p13, usage.**

> identification of the counterparty when a bilateral balance is requested

**File p13, usage.**

> balance value date (if not present in the GetAccount message, the ReturnAccount message will contain the latest available balance) This message will be answered by a ReturnAccount message.

**File p13, usage.**

> Additional information on the generic design of the Get/Return messages can be found in the section How to Use the Cash Management Messages.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
