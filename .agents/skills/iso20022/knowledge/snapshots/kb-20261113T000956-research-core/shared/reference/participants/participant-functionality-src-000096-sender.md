---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["securities"]
participant_id: "participant-functionality-src-000096-sender"
title: "Sender — Investment Funds Functionality"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
source_labels: ["Sender"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["investment-funds"]
message_ids: ["camt.040.001.04", "camt.041.001.04", "semt.001.001.03"]
message_families: ["camt.040", "camt.041", "semt.001"]
source_locations: [{"source_id": "src-000096", "heading": "7 camt.040.001.04 FundEstimatedCashForecastReportV04", "file_pages": [94], "evidence_id": "src-000096-camt.040.001.04-p94-c003"}, {"source_id": "src-000096", "heading": "8 camt.041.001.04 FundConfirmedCashForecastReportV04", "file_pages": [105], "evidence_id": "src-000096-camt.041.001.04-p105-c003"}, {"source_id": "src-000096", "heading": "17 semt.001.001.03 SecuritiesMessageRejectionV03", "file_pages": [371], "evidence_id": "src-000096-semt.001.001.03-p371-c005"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# Sender — Investment Funds Functionality

[src-000096](../../../evidence/omitted/fffd4ab68b421d059524ec38.md)

## Definition and business context

Generic sender function explicitly named in this publication’s quoted message Functionality. Its precise capacity and counterparties are retained per clause rather than being inferred from the generic label.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000096-camt.040.001.04-p94-c003

src-000096, file page 94; 7 camt.040.001.04 FundEstimatedCashForecastReportV04.

> This message allows the report provider to report estimated cash movements in or out of a fund, but does not allow the Sender to categorise these movements, for example by country, or to give details of the underlying orders, commission or charges.

### src-000096-camt.041.001.04-p105-c003

src-000096, file page 105; 8 camt.041.001.04 FundConfirmedCashForecastReportV04.

> This message allows the report provider to report cash movements in or out of a fund, but does not allow the Sender to categorise these movements, for example by country, or to give details of the underlying orders, commission or charges.

### src-000096-semt.001.001.03-p371-c005

src-000096, file page 371; 17 semt.001.001.03 SecuritiesMessageRejectionV03.

> Reasons that a receiver does not expect a message include no SLA in place between the Sender and the Receiver.

## Applicable exact messages


- [camt.040.001.04](../../../domains/securities/reference/messages/camt.040.001.04/roles.md)
- [camt.041.001.04](../../../domains/securities/reference/messages/camt.041.001.04/roles.md)
- [semt.001.001.03](../../../domains/securities/reference/messages/semt.001.001.03/roles.md)

## Identity and unresolved scope

Source labels: Sender. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
