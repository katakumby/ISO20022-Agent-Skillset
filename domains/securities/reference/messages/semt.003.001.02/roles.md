---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "semt.003.001.02 participant and direction evidence"
domain: "securities"
message_id: "semt.003.001.02"
message_family: "semt.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.003.001.02"
source_ids: ["src-000096", "src-000115"]
message_sets: ["investment-funds"]
role_labels: ["account owner", "account servicer", "An account servicer", "designated agent", "fund manager", "the account owner", "transfer agent"]
search_terms: ["account owner", "account servicer", "An account servicer", "designated agent", "fund manager", "the account owner", "transfer agent"]
participant_ids: ["participant-narrative-src-000096-account-owner", "participant-narrative-src-000096-account-servicer", "participant-narrative-src-000096-designated-agent", "participant-src-000095-fund-manager", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "19 semt.003.001.02 AccountingStatementOfHoldingsV02", "file_pages": [387, 397]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# semt.003.001.02 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 5 uniquely resolved participant references.

## src-000096 — 19 semt.003.001.02 AccountingStatementOfHoldingsV02

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); Functionality file pp387, 388; publication May 2026.

### Direction and initiation clauses

#### src-000096-semt.003.001.02-p387-c001-d1

Kind: sender-to-receiver; message applicability: **current-message-scope-name-variant**; src-000096 file p387, scope.

- Sender: **An account servicer, for example, a transfer agent**. [An account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md).
- Receiver: **the account owner, for example, a fund manager or an account owner's designated agent**. [the account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md).

> An account servicer, for example, a transfer agent sends the AccountStatementOfHoldings message to the account owner, for example, a fund manager or an account owner's designated agent to provide detailed holdings of the portfolio at a specified moment in time.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-semt.003.001.02-p387-c001 — file p387, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md); [fund manager](../../../../../shared/reference/participants/participant-src-000095-fund-manager.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md); [designated agent](../../../../../shared/reference/participants/participant-narrative-src-000096-designated-agent.md).

Literal actions: transfer agent sends.

Quoted above in src-000096-semt.003.001.02-p387-c001-d1.

**src-000096-semt.003.001.02-p387-c002 — file p387, scope.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> The message can be sent either audited or un-audited and may be provided on a trade date or settlement date basis.

**src-000096-semt.003.001.02-p387-c003 — file p387, usage.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md).

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> The message should be sent at a frequency agreed bi-laterally between the account servicer and the account owner.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p387, scope.**

> The message provides, at a moment in time, valuations of the portfolio together with details of each financial instrument holding.

**File p387, usage.**

> The AccountingStatementOfHoldings message is used to provide valuation detail for each financial instrument held in a portfolio.

**File p387, usage.**

> This message can only be used to list the holdings of a single (master) account.

**File p387, usage.**

> However, it is possible to break down these holdings into one or several sub-accounts.

**File p387, usage.**

> Therefore, the message can be used to either specify holdings at

**File p387, usage.**

> the main account level, or,

**File p387, usage.**

> the sub-account level.

**File p387, usage.**

> This message can be used to report where the financial instruments are safe-kept, physically or notionally.

**File p387, usage.**

> If a security is held in more than one safekeeping place, this can also be indicated.

**File p387, usage.**

> The AccountingStatementOfHoldings message should not be used for trading purposes.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
