---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "semt.002.001.02 participant and direction evidence"
domain: "securities"
message_id: "semt.002.001.02"
message_family: "semt.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.002.001.02"
source_ids: ["src-000096", "src-000114"]
message_sets: ["investment-funds"]
role_labels: ["account owner", "account servicer", "An account servicer", "designated agent", "fund manager", "the account owner", "transfer agent"]
search_terms: ["account owner", "account servicer", "An account servicer", "designated agent", "fund manager", "the account owner", "transfer agent"]
participant_ids: ["participant-narrative-src-000096-account-owner", "participant-narrative-src-000096-account-servicer", "participant-narrative-src-000096-designated-agent", "participant-src-000095-fund-manager", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "18 semt.002.001.02 CustodyStatementOfHoldingsV02", "file_pages": [375, 386]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# semt.002.001.02 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 5 uniquely resolved participant references.

## src-000096 — 18 semt.002.001.02 CustodyStatementOfHoldingsV02

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); Functionality file pp375, 376; publication May 2026.

### Direction and initiation clauses

#### src-000096-semt.002.001.02-p375-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p375, scope.

- Sender: **An account servicer, for example, a transfer agent**. [An account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md).
- Receiver: **the account owner, for example, a fund manager or an account owner's designated agent**. [the account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md).

> An account servicer, for example, a transfer agent sends the CustodyStatementOfHoldings message to the account owner, for example, a fund manager or an account owner's designated agent to provide detailed holdings of the portfolio at a specified moment in time.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-semt.002.001.02-p375-c001 — file p375, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md); [fund manager](../../../../../shared/reference/participants/participant-src-000095-fund-manager.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md); [designated agent](../../../../../shared/reference/participants/participant-narrative-src-000096-designated-agent.md).

Literal actions: transfer agent sends.

Quoted above in src-000096-semt.002.001.02-p375-c001-d1.

**src-000096-semt.002.001.02-p375-c002 — file p375, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md).

Literal actions: account servicer holds.

> The message provides, at a moment in time, the quantity and identification of the financial instruments that the account servicer holds for the account owner.

**src-000096-semt.002.001.02-p375-c003 — file p375, usage.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md).

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> The message should be sent at a frequency agreed bi-laterally between the account servicer and the account owner.

**src-000096-semt.002.001.02-p375-c004 — file p375, usage.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> This message can reflect all outstanding holding information or may only contain changes since the previously sent statement.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p375, scope.**

> The message can also include availability and the location of holdings to facilitate trading and minimise settlement issues.

**File p375, scope.**

> The message reports all information per financial instrument, ie, when a financial instrument is held at multiple places of safekeeping, the total holdings for all locations can be provided.

**File p375, usage.**

> The CustodyStatementOfHoldings message is used to provide detailed quantity and availability information for financial instrument holdings of a portfolio.

**File p375, usage.**

> This message can be also be used to report where the financial instruments are safe-kept, physically or notionally.

**File p375, usage.**

> If a security is held in more than one safekeeping place, this can also be indicated.

**File p375, usage.**

> The CustodyStatementOfHoldings message can only be used to list the holdings of a single (master) account.

**File p375, usage.**

> However, it is possible to break down these holdings into one or several sub-accounts.

**File p375, usage.**

> Therefore, this message can be used to either specify holdings at

**File p375, usage.**

> the main account level, or,

**File p375, usage.**

> the sub-account level.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
