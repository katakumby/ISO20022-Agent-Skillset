---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.015.001.01 participant and direction evidence"
domain: "securities"
message_id: "reda.015.001.01"
message_family: "reda.015"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01"
source_ids: ["src-000233", "src-000270", "src-000369"]
message_sets: ["t2s", "t2s-party-reference-data"]
role_labels: ["a central counter party", "a central securities depository", "a central securities depository participant", "a national central bank", "a payment bank", "a stock exchange", "a trading party", "central counter party", "central securities depository", "central securities depository participant", "executing party", "national central bank", "payment bank", "stock exchange", "the executing party", "trading party"]
search_terms: ["a central counter party", "a central securities depository", "a central securities depository participant", "a national central bank", "a payment bank", "a stock exchange", "a trading party", "central counter party", "central securities depository", "central securities depository participant", "executing party", "national central bank", "payment bank", "stock exchange", "the executing party", "trading party"]
participant_ids: ["participant-functionality-src-000369-payment-bank", "participant-functionality-src-000369-trading-party", "participant-narrative-src-000369-central-counter-party", "participant-narrative-src-000369-central-securities-depository", "participant-narrative-src-000369-central-securities-depository-participant", "participant-narrative-src-000369-executing-party", "participant-narrative-src-000369-stock-exchange", "participant-src-000368-national-central-bank-ncb"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "35 reda.015.001.01 PartyQueryV01", "file_pages": [2055, 2071]}, {"source_id": "src-000369", "heading": "3 reda.015.001.01 PartyQueryV01", "file_pages": [18, 34]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.015.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 8 uniquely resolved participant references.

## src-000233 — 35 reda.015.001.01 PartyQueryV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp2055; publication August 2026.

### Direction and initiation clauses

#### src-000233-reda.015.001.01-p2055-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p2055, scope.

- Sender: **a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange**. [a central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000369-central-securities-depository.md); [a national central bank](../../../../../shared/reference/participants/participant-src-000368-national-central-bank-ncb.md); [a central securities depository participant](../../../../../shared/reference/participants/participant-narrative-src-000369-central-securities-depository-participant.md); [a central counter party](../../../../../shared/reference/participants/participant-narrative-src-000369-central-counter-party.md); [a payment bank](../../../../../shared/reference/participants/participant-functionality-src-000369-payment-bank.md); [a trading party](../../../../../shared/reference/participants/participant-functionality-src-000369-trading-party.md); [a stock exchange](../../../../../shared/reference/participants/participant-narrative-src-000369-stock-exchange.md).
- Receiver: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md).

> The PartyQuery message is sent by a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange to the executing party to query for the party reference data of a party defined in the system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-reda.015.001.01-p2055-c001 — file p2055, scope.**

Mentioned roles: [central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000369-central-securities-depository.md); [national central bank](../../../../../shared/reference/participants/participant-src-000368-national-central-bank-ncb.md); [central securities depository participant](../../../../../shared/reference/participants/participant-narrative-src-000369-central-securities-depository-participant.md); [central counter party](../../../../../shared/reference/participants/participant-narrative-src-000369-central-counter-party.md); [payment bank](../../../../../shared/reference/participants/participant-functionality-src-000369-payment-bank.md); [trading party](../../../../../shared/reference/participants/participant-functionality-src-000369-trading-party.md); [stock exchange](../../../../../shared/reference/participants/participant-narrative-src-000369-stock-exchange.md); [executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md).

Quoted above in src-000233-reda.015.001.01-p2055-c001-d1.

## src-000369 — 3 reda.015.001.01 PartyQueryV01

[src-000369](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`; Functionality file pp18; publication march-2024.

### Direction and initiation clauses

#### src-000369-reda.015.001.01-p18-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000369 file p18, scope.

- Sender: **a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange**. [a central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000369-central-securities-depository.md); [a national central bank](../../../../../shared/reference/participants/participant-src-000368-national-central-bank-ncb.md); [a central securities depository participant](../../../../../shared/reference/participants/participant-narrative-src-000369-central-securities-depository-participant.md); [a central counter party](../../../../../shared/reference/participants/participant-narrative-src-000369-central-counter-party.md); [a payment bank](../../../../../shared/reference/participants/participant-functionality-src-000369-payment-bank.md); [a trading party](../../../../../shared/reference/participants/participant-functionality-src-000369-trading-party.md); [a stock exchange](../../../../../shared/reference/participants/participant-narrative-src-000369-stock-exchange.md).
- Receiver: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md).

> The PartyQuery message is sent by a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange to the executing party to query for the party reference data of a party defined in the system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000369-reda.015.001.01-p18-c001 — file p18, scope.**

Mentioned roles: [central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000369-central-securities-depository.md); [national central bank](../../../../../shared/reference/participants/participant-src-000368-national-central-bank-ncb.md); [central securities depository participant](../../../../../shared/reference/participants/participant-narrative-src-000369-central-securities-depository-participant.md); [central counter party](../../../../../shared/reference/participants/participant-narrative-src-000369-central-counter-party.md); [payment bank](../../../../../shared/reference/participants/participant-functionality-src-000369-payment-bank.md); [trading party](../../../../../shared/reference/participants/participant-functionality-src-000369-trading-party.md); [stock exchange](../../../../../shared/reference/participants/participant-narrative-src-000369-stock-exchange.md); [executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md).

Quoted above in src-000369-reda.015.001.01-p18-c001-d1.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
