---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p248-financial-instrument-transaction-report"
title: "Transaction reporting and authority exchange"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Transaction Reporting", "Financial Instrument Transaction Report"], "locator": "/w:document/w:body/w:p[248]", "paragraph_id": "P248", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Transaction Reporting", "Financial Instrument Transaction Report"], "locator": "/w:document/w:body/w:p[249]", "paragraph_id": "P249", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Transaction Reporting", "Financial Instrument Transaction Report"], "locator": "/w:document/w:body/w:p[250]", "paragraph_id": "P250", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Transaction Reporting", "Financial Instrument Transaction Report"], "locator": "/w:document/w:body/w:p[251]", "paragraph_id": "P251", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Transaction Reporting", "Financial Instrument Transaction Report"], "locator": "/w:document/w:body/w:p[252]", "paragraph_id": "P252", "table_id": null}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-relevant-ca", "participant-src-000320-reporting-entity"]
message_mapping_evidence: [{"source_id": "src-000320", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Transaction Reporting MessageDefinition"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[2]", "paragraph_id": null, "table_id": "T7"}]
message_ids: ["auth.016.001.03"]
message_families: ["auth.016"]
search_terms: ["Financial Instrument Transaction Report", "Relevant CA", "RE", "CA", "auth.016"]
limitations: ["TransactionReportingMessage and TransactionReportingMessagesStatusAdvice are literal picture labels. T7 identifies the transaction-reporting family auth.016; the generic status label is not silently equated with auth.031.", "Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.", "The described flow is scoped to this publication; it is not advice on current regulation."]
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-relevant-ca", "participant-src-000320-reporting-entity"]
manual_curated: true
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0036.md"]
---

# Transaction reporting and authority exchange

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); BusinessTransactions / Transaction Reporting / Financial Instrument Transaction Report.

## Purpose, trigger, preconditions and outcomes

Source process definition [T20](../documents/src-000320/tables/tbl-0020.md) (the overall process conditions also apply to its reporting variant):

| Item | Description |
| --- | --- |
| Definition | Any entity (IF, ARM) that has to report transanction data to CA. Reported data is related to the transactions in the instruments that are admitted to trading or their derivatives. |
| Trigger | Data is submitted daily and no later than the close of the following working day transaction was executed. |
| Pre-conditions | Transaction in the financial instrument or its derivate is executed. |
| Post-conditions | The reporting entity has received a  status advice related to the submitted transactions report message. |
| Role | Reporting entity |


Source process definition [T21](../documents/src-000320/tables/tbl-0021.md) (the overall process conditions also apply to its reporting variant):

| Item | Description |
| --- | --- |
| Definition | CA that has to exchange relevant transanction data to another CA. Relevant data must fulfill exchange conditions agreed between CAs. |
| Trigger | CA received transaction data which fulfills exchange conditions agreed between CAs. |
| Pre-conditions | Transaction in the financial instrument or its derivate is executed and reported to one of CAs. |
| Post-conditions | Sending CA has received a status advice related to the exchanged data. |
| Role | Sending CA |


## Participants and responsibilities

- [Reporting Entity](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md)
- [Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md)
- [Relevant Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-relevant-ca.md)

Initiation and responsibility follow the explicit message directions and narrative below; a participant appearing on a lifeline is not automatically a sender.

## Ordered exchanges and decision points

| Order | Sender | Receiver | Literal source message / exchange | Source condition or fragment |
| --- | --- | --- | --- | --- |
| 1 | Reporting Entity | Competent Authority | TransactionReportingMessage | Outside conditional frame |
| 2 | Competent Authority | Reporting Entity | TransactionReportingMessagesStatusAdvice | Outside conditional frame |
| 3 | Competent Authority | Relevant Competent Authority | TransactionReportingMessage | Outside conditional frame |
| 4 | Relevant Competent Authority | Competent Authority | TransactionReportingMessagesStatusAdvice | Outside conditional frame |


[Reconstructed sequence and retained original](../diagrams/fitrr-sequences/fig-0036.md)

## Source narrative and additional participants

**P249** This flow describes RE submitting Transaction Reporting Messages to CA. CA is responsible for all data checking operations on the received message and directly replies to the submitting RE. It also  exchanges relevant data with other relevant CA.

## Supplied message definitions

- [auth.016.001.03 — FinancialInstrumentReportingTransactionReportV03](../../../../messages/auth.016.001.03/index.md)

Family mappings are grounded in Part1 tables T4–T9 and the matching supplied message catalog. The figure names remain literal; a family link does not turn an unversioned diagram into evidence for a particular schema version.

## Alternative and exceptional paths

The source conditions and narrative above define the applicable alternatives. Repeated arrows and all error branches are retained; no additional cancellation or reversal route is invented.

## Limitations

- TransactionReportingMessage and TransactionReportingMessagesStatusAdvice are literal picture labels. T7 identifies the transaction-reporting family auth.016; the generic status label is not silently equated with auth.031.
- Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.
- The described flow is scoped to this publication; it is not advice on current regulation.
