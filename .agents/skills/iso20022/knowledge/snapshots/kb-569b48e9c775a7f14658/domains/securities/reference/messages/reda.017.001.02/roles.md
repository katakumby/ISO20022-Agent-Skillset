---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.017.001.02 participant and direction evidence"
domain: "securities"
message_id: "reda.017.001.02"
message_family: "reda.017"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.017.001.02"
source_ids: ["src-000233", "src-000272", "src-000369"]
message_sets: ["t2s", "t2s-party-reference-data"]
role_labels: ["a central counter party", "a central securities depository", "a central securities depository participant", "a national central bank", "a payment bank", "a stock exchange", "a trading party", "central counter party", "central securities depository", "central securities depository participant", "executing party", "national central bank", "payment bank", "stock exchange", "the executing party", "trading party"]
search_terms: ["a central counter party", "a central securities depository", "a central securities depository participant", "a national central bank", "a payment bank", "a stock exchange", "a trading party", "central counter party", "central securities depository", "central securities depository participant", "executing party", "national central bank", "payment bank", "stock exchange", "the executing party", "trading party"]
participant_ids: ["participant-functionality-src-000369-payment-bank", "participant-functionality-src-000369-trading-party", "participant-narrative-src-000369-central-counter-party", "participant-narrative-src-000369-central-securities-depository", "participant-narrative-src-000369-central-securities-depository-participant", "participant-narrative-src-000369-executing-party", "participant-narrative-src-000369-stock-exchange", "participant-src-000368-national-central-bank-ncb"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "37 reda.017.001.02 PartyReportV02", "file_pages": [2078, 2097]}, {"source_id": "src-000369", "heading": "5 reda.017.001.02 PartyReportV02", "file_pages": [41, 60]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.017.001.02 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 8 uniquely resolved participant references.

## src-000233 — 37 reda.017.001.02 PartyReportV02

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp2078; publication August 2026.

### Direction and initiation clauses

#### src-000233-reda.017.001.02-p2078-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p2078, scope.

- Sender: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md).
- Receiver: **a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange**. [a central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000369-central-securities-depository.md); [a national central bank](../../../../../shared/reference/participants/participant-src-000368-national-central-bank-ncb.md); [a central securities depository participant](../../../../../shared/reference/participants/participant-narrative-src-000369-central-securities-depository-participant.md); [a central counter party](../../../../../shared/reference/participants/participant-narrative-src-000369-central-counter-party.md); [a payment bank](../../../../../shared/reference/participants/participant-functionality-src-000369-payment-bank.md); [a trading party](../../../../../shared/reference/participants/participant-functionality-src-000369-trading-party.md); [a stock exchange](../../../../../shared/reference/participants/participant-narrative-src-000369-stock-exchange.md).

> The PartyReport message is sent by the executing party to a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange to provide detailed information on the requested party reference data of the party defined in the system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-reda.017.001.02-p2078-c001 — file p2078, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md); [central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000369-central-securities-depository.md); [national central bank](../../../../../shared/reference/participants/participant-src-000368-national-central-bank-ncb.md); [central securities depository participant](../../../../../shared/reference/participants/participant-narrative-src-000369-central-securities-depository-participant.md); [central counter party](../../../../../shared/reference/participants/participant-narrative-src-000369-central-counter-party.md); [payment bank](../../../../../shared/reference/participants/participant-functionality-src-000369-payment-bank.md); [trading party](../../../../../shared/reference/participants/participant-functionality-src-000369-trading-party.md); [stock exchange](../../../../../shared/reference/participants/participant-narrative-src-000369-stock-exchange.md).

Quoted above in src-000233-reda.017.001.02-p2078-c001-d1.

## src-000369 — 5 reda.017.001.02 PartyReportV02

[src-000369](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`; Functionality file pp41; publication march-2024.

### Direction and initiation clauses

#### src-000369-reda.017.001.02-p41-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000369 file p41, scope.

- Sender: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md).
- Receiver: **a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange**. [a central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000369-central-securities-depository.md); [a national central bank](../../../../../shared/reference/participants/participant-src-000368-national-central-bank-ncb.md); [a central securities depository participant](../../../../../shared/reference/participants/participant-narrative-src-000369-central-securities-depository-participant.md); [a central counter party](../../../../../shared/reference/participants/participant-narrative-src-000369-central-counter-party.md); [a payment bank](../../../../../shared/reference/participants/participant-functionality-src-000369-payment-bank.md); [a trading party](../../../../../shared/reference/participants/participant-functionality-src-000369-trading-party.md); [a stock exchange](../../../../../shared/reference/participants/participant-narrative-src-000369-stock-exchange.md).

> The PartyReport message is sent by the executing party to a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange to provide detailed information on the requested party reference data of the party defined in the system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000369-reda.017.001.02-p41-c001 — file p41, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md); [central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000369-central-securities-depository.md); [national central bank](../../../../../shared/reference/participants/participant-src-000368-national-central-bank-ncb.md); [central securities depository participant](../../../../../shared/reference/participants/participant-narrative-src-000369-central-securities-depository-participant.md); [central counter party](../../../../../shared/reference/participants/participant-narrative-src-000369-central-counter-party.md); [payment bank](../../../../../shared/reference/participants/participant-functionality-src-000369-payment-bank.md); [trading party](../../../../../shared/reference/participants/participant-functionality-src-000369-trading-party.md); [stock exchange](../../../../../shared/reference/participants/participant-narrative-src-000369-stock-exchange.md).

Quoted above in src-000369-reda.017.001.02-p41-c001-d1.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
