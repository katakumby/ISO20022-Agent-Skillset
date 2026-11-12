---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["securities"]
participant_id: "participant-functionality-src-000181-agent"
title: "agent — Post-Trade Matching Functionality"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
source_labels: ["agent"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["post-trade-matching"]
message_ids: ["semt.023.001.02", "setr.027.001.05", "setr.030.001.03"]
message_families: ["semt.023", "setr.027", "setr.030"]
source_locations: [{"source_id": "src-000181", "heading": "2 semt.023.001.02 SecuritiesEndOfProcessReportV02", "file_pages": [6], "evidence_id": "src-000181-semt.023.001.02-p6-c005"}, {"source_id": "src-000181", "heading": "3 setr.027.001.05 SecuritiesTradeConfirmationV05", "file_pages": [28], "evidence_id": "src-000181-setr.027.001.05-p28-c005"}, {"source_id": "src-000181", "heading": "5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03", "file_pages": [148], "evidence_id": "src-000181-setr.030.001.03-p148-c004"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# agent — Post-Trade Matching Functionality

[src-000181](../../../evidence/omitted/128c587d5e2143c7e981d2b6.md)

## Definition and business context

Generic agent function explicitly named in this publication’s quoted message Functionality. Its precise capacity and counterparties are retained per clause rather than being inferred from the generic label.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000181-semt.023.001.02-p6-c005

src-000181, file page 6; 2 semt.023.001.02 SecuritiesEndOfProcessReportV02.

> The custodian or an affirming party is typically the custodian, trustee, financial institution, intermediary system/vendor communicating on behalf of them, or their agent.

### src-000181-setr.027.001.05-p28-c005

src-000181, file page 28; 3 setr.027.001.05 SecuritiesTradeConfirmationV05.

> The custodian or the affirming party is typically the custodian, trustee, financial institution, intermediary system/vendor communicating on behalf of them, or their agent.

### src-000181-setr.030.001.03-p148-c004

src-000181, file page 148; 5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03.

> The custodian or an affirming party is typically the custodian, trustee, financial institution, intermediary system/vendor communicating on behalf of them, or their agent.

## Applicable exact messages


- [semt.023.001.02](../../../domains/securities/reference/messages/semt.023.001.02/roles.md)
- [setr.027.001.05](../../../domains/securities/reference/messages/setr.027.001.05/roles.md)
- [setr.030.001.03](../../../domains/securities/reference/messages/setr.030.001.03/roles.md)

## Identity and unresolved scope

Source labels: agent. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
