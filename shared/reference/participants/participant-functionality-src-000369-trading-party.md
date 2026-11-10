---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["securities"]
participant_id: "participant-functionality-src-000369-trading-party"
title: "trading party — T2S PartyReferenceData Functionality"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
source_labels: ["trading party"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["t2s-party-reference-data"]
message_ids: ["reda.015.001.01", "reda.017.001.02"]
message_families: ["reda.015", "reda.017"]
source_locations: [{"source_id": "src-000369", "heading": "3 reda.015.001.01 PartyQueryV01", "file_pages": [18], "evidence_id": "src-000369-reda.015.001.01-p18-c001"}, {"source_id": "src-000369", "heading": "5 reda.017.001.02 PartyReportV02", "file_pages": [41], "evidence_id": "src-000369-reda.017.001.02-p41-c001"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# trading party — T2S PartyReferenceData Functionality

[src-000369](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`

## Definition and business context

Participant explicitly allowed to query and receive party reference data in PartyQuery and PartyReport.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000369-reda.015.001.01-p18-c001

src-000369, file page 18; 3 reda.015.001.01 PartyQueryV01.

> The PartyQuery message is sent by a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange to the executing party to query for the party reference data of a party defined in the system.

### src-000369-reda.017.001.02-p41-c001

src-000369, file page 41; 5 reda.017.001.02 PartyReportV02.

> The PartyReport message is sent by the executing party to a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange to provide detailed information on the requested party reference data of the party defined in the system.

## Applicable exact messages


- [reda.015.001.01](../../../domains/securities/reference/messages/reda.015.001.01/roles.md)
- [reda.017.001.02](../../../domains/securities/reference/messages/reda.017.001.02/roles.md)

## Identity and unresolved scope

Source labels: trading party. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
