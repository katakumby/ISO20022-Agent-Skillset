---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368", "src-000369"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
participant_id: "participant-src-000368-national-central-bank-ncb"
title: "National Central Bank (NCB)"
source_labels: ["National Central Bank (NCB)", "national central bank"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000368", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[3]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000369", "heading": "3 reda.015.001.01 PartyQueryV01", "file_pages": [18], "evidence_id": "src-000369-reda.015.001.01-p18-c001"}, {"source_id": "src-000369", "heading": "5 reda.017.001.02 PartyReportV02", "file_pages": [41], "evidence_id": "src-000369-reda.017.001.02-p41-c001"}]
flows: []
process_sections: []
message_ids: ["reda.015.001.01", "reda.017.001.02"]
message_families: ["reda.015", "reda.017"]
search_terms: ["National Central Bank (NCB)"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---









# National Central Bank (NCB)

Business context: T2S PartyReferenceData. Source classification: business role.

## Definition

The principal monetary authority of a nation, a central bank performs several key functions, including issuing currency and regulating the supply of credit in the economy. 

Evidence: [T6](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0006.md), source row 3.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `National Central Bank (NCB)`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000368](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`.




<!-- FUNCTIONALITY-ALIASES-src-000369 -->
## Additional literal publication labels

The unabbreviated name is explicitly the same business-role label as National Central Bank (NCB); source context remains PartyQuery/PartyReport.

| Source label | Source context |
| --- | --- |
| national central bank | src-000369-reda.015.001.01-p18-c001; src-000369-reda.017.001.02-p41-c001 |


> The PartyQuery message is sent by a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange to the executing party to query for the party reference data of a party defined in the system.

src-000369, file pages18; 3 reda.015.001.01 PartyQueryV01.

> The PartyReport message is sent by the executing party to a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange to provide detailed information on the requested party reference data of the party defined in the system.

src-000369, file pages41; 5 reda.017.001.02 PartyReportV02.

<!-- /FUNCTIONALITY-ALIASES-src-000369 -->
