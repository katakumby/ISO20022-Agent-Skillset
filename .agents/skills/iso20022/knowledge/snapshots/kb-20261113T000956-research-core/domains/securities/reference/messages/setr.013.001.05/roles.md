---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "setr.013.001.05 participant and direction evidence"
domain: "securities"
message_id: "setr.013.001.05"
message_family: "setr.013"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.013.001.05"
source_ids: ["src-000096", "src-000149"]
message_sets: ["investment-funds"]
role_labels: ["an instructing party", "authorised representative", "executing party", "instructing party", "investment manager", "investor", "the executing party", "transfer agent"]
search_terms: ["an instructing party", "authorised representative", "executing party", "instructing party", "investment manager", "investor", "the executing party", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-authorised-representative", "participant-narrative-src-000096-investment-manager", "participant-narrative-src-000096-investor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "53 setr.013.001.05 SwitchOrderV05", "file_pages": [3487, 3796]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# setr.013.001.05 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 6 uniquely resolved participant references.

## src-000096 — 53 setr.013.001.05 SwitchOrderV05

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp3487, 3488; publication May 2026.

### Direction and initiation clauses

#### src-000096-setr.013.001.05-p3487-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p3487, scope.

- Sender: **an instructing party, for example, an investment manager or its authorised representative**. [an instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).
- Receiver: **the executing party, for example, a transfer agent**. [the executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).

> The SwitchOrder message is sent by an instructing party, for example, an investment manager or its authorised representative, to the executing party, for example, a transfer agent, to instruct a switch transaction from a financial instrument or multiple financial instruments to a different specified financial instrument or instruments for a specified amount/quantity.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-setr.013.001.05-p3487-c001 — file p3487, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representative](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md); [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md).

Quoted above in src-000096-setr.013.001.05-p3487-c001-d1.

**src-000096-setr.013.001.05-p3487-c002 — file p3487, usage.**

> instruct one switch transaction comprising one or more redemption legs and one or more subscription legs, that is, a single switch transaction that can be a one to one, many to one, many to many or one to many switch transaction, or,

**src-000096-setr.013.001.05-p3487-c003 — file p3487, usage.**

> instruct one or many switch transactions each comprising one redemption leg and one subscription leg, that is, multiple simple switch transactions.

**src-000096-setr.013.001.05-p3487-c004 — file p3487, usage.**

> instruct a switch transaction for one investment account, or,

**src-000096-setr.013.001.05-p3487-c005 — file p3487, usage.**

> instruct a switch transaction for separate accounts at the redemption and subscription leg levels.

**src-000096-setr.013.001.05-p3487-c006 — file p3487, usage.**

Mentioned roles: [investor](../../../../../shared/reference/participants/participant-narrative-src-000096-investor.md); [investor](../../../../../shared/reference/participants/participant-narrative-src-000096-investor.md).

> The message caters for switch transactions that result in an additional cash payment from the investor or a transaction that results in a net payment to the investor.

**src-000096-setr.013.001.05-p3487-c007 — file p3487, usage.**

> The number allowed is defined by the fund prospectus or by the service level agreement (SLA) in place between the two parties.

**src-000096-setr.013.001.05-p3487-c008 — file p3487, usage.**

Mentioned roles: [investor](../../../../../shared/reference/participants/participant-narrative-src-000096-investor.md).

> This functionality is to be used by institutions that set up two accounts per investor, rather than one investment account.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p3487, usage.**

> The SwitchOrder message is used to either:

**File p3487, usage.**

> The SwitchOrder message may be used to either:

**File p3487, usage.**

> The message caters for a switch from one financial instrument to another financial instrument (within the same fund family), many to one, many to many and one to many.

**File p3487, usage.**

> Not all institutions or funds permit this type of switch and acceptance is therefore not automatic.

**File p3487, usage.**

> There is no limitation on the number of switch legs in a switch message.

**File p3487, usage.**

> However, if the SwitchOrderDetails sequence is present more than once, then the RedemptionLegDetails and SubscriptionLegDetails sequences may only be present once.

**File p3487, usage.**

> If SwitchOrderDetails\InvestmentAccount is used, then the InvestmentAccountDetails sequences in SubscriptionLegDetails and RedemptionLegDetails are not allowed.

**File p3487, usage.**

> There is no switch driver type in the message to indicate whether the switch is buy or sell driven.

**File p3487, usage.**

> A driver is not needed since it is possible to indicate the total subscription amount or the total redemption amount.

**File p3487, usage.**

> Only one of these two amounts should be used.

**File p3487, usage.**

> The subscription quantity can be expressed in one of the following ways:

**File p3487, usage.**

> Amount: the monetary value (either GROSS or NET) of the financial instrument to be subscribed to, for example, the subscription of EUR 1,000 of financial instrument ISIN LU1234567890 or Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05 Investment Funds - Maintenance 2025 - 2026 3487 May 2026

**File p3488, usage.**

> Unit: the number of units of the financial instrument to be subscribed to, for example, the subscription of 10 units of financial instrument ISIN LU1234567890 or

**File p3488, usage.**

> Percentage of the total redemption amount: when the switch transaction is redemption driven, it is the part of the redemption amount that must be switched to a specific financial instrument, for example, the subscription quantity of financial instrument ISIN LU1234567890 represents 50% of the redemption amount of the financial instrument ISIN LU4444444444.

**File p3488, usage.**

> The redemption quantity can be expressed in one of the following ways:

**File p3488, usage.**

> Amount: the monetary value (either GROSS or NET) of the financial instrument to be redeemed, for example, the redemption of EUR 1,000 of financial instrument ISIN LU1234567890, or

**File p3488, usage.**

> Unit: the number of units of financial instrument to be redeemed, for example, the redemption of 10 units of financial instrument ISIN LU1234567890, or

**File p3488, usage.**

> Rate: the part of the portfolio to be redeemed, for example, the redemption of 10% of the holdings in financial instrument ISIN LU1234567890, or

**File p3488, usage.**

> Percentage of the total subscription amount: when the switch transaction is subscription driven, it is the part of the subscription amount that must be the result of the redemption of a specific financial instrument, for example, the redemption quantity in financial instrument ABC represents 50% of the subscription amount of the financial instrument ISIN LU4444444444.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
