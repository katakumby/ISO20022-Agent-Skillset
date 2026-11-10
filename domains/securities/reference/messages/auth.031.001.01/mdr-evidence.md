---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "auth.031.001.01"
message_family: "auth.031"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01"
source_ids: ["src-000321"]
source_locations: [{"source_id": "src-000321", "heading": "4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01", "file_pages": [39, 47]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["July 2025"]
---

# auth.031.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000321 — 4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01

[src-000321](../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf); file pp39–47; publication July 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000321, 4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01, Functionality, file p39.**

The FinancialInstrumentReportingStatusAdvice message is sent by the national competent authority to
the reporting agent to provide a status advice for the correctness, issues or errors that arise from the
submitted report.
Outline
The FinancialInstrumentReportingStatusAdviceV01 MessageDefinition is composed of 2
MessageBuildingBlocks:
A. StatusAdvice
Status advice report.
B. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 17 July 2025 auth.031.001.01
FinancialInstrumentReportingStatusAdviceV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
39 July 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/fitrr/2025/documents/src-000321/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00030.md) | 39–39 |
| [4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01 / 4.2 Structure](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00031.md) | 40–40 |
| [4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.1 StatusAdvice &lt;StsAdvc&gt; / 4.4.1.1 MessageReportIdentifier &lt;MsgRptIdr&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00032.md) | 41–41 |
| [4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.1 StatusAdvice &lt;StsAdvc&gt; / 4.4.1.2 MessageStatus &lt;MsgSts&gt; / 4.4.1.2.1 Status &lt;Sts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00033.md) | 42–42 |
| [4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.1 StatusAdvice &lt;StsAdvc&gt; / 4.4.1.2 MessageStatus &lt;MsgSts&gt; / 4.4.1.2.3 MessageDate &lt;MsgDt&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00034.md) | 43–43 |
| [4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.1 StatusAdvice &lt;StsAdvc&gt; / 4.4.1.2 MessageStatus &lt;MsgSts&gt; / 4.4.1.2.4 Statistics &lt;Sttstcs&gt; / 4.4.1.2.4.2 NumberOfRecordsPerStatus &lt;NbOfRcrdsPerSts&gt; / 4.4.1.2.4.2.1 DetailedNumberOfRecords &lt;DtldNbOfRcrds&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00035.md) | 44–44 |
| [4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.1 StatusAdvice &lt;StsAdvc&gt; / 4.4.1.3 RecordStatus &lt;RcrdSts&gt; / 4.4.1.3.2 Status &lt;Sts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00036.md) | 45–45 |
| [4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.1 StatusAdvice &lt;StsAdvc&gt; / 4.4.1.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00037.md) | 46–47 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [APA](../../../../../shared/reference/participants/participant-src-000320-apa.md) | participant | src-000320 |
| [ARM](../../../../../shared/reference/participants/participant-src-000320-arm.md) | participant | src-000320 |
| [CA](../../../../../shared/reference/participants/participant-src-000320-ca.md) | participant | src-000320 |
| [Competent Authority](../../../../../shared/reference/participants/participant-src-000320-competent-authority.md) | participant | src-000320 |
| [CTP](../../../../../shared/reference/participants/participant-src-000320-ctp.md) | participant | src-000320 |
| [ESMA](../../../../../shared/reference/participants/participant-src-000320-esma.md) | participant | src-000320 |
| [IF](../../../../../shared/reference/participants/participant-src-000320-if.md) | participant | src-000320 |
| [MTF](../../../../../shared/reference/participants/participant-src-000320-mtf.md) | participant | src-000320 |
| [NCA](../../../../../shared/reference/participants/participant-src-000320-nca.md) | participant | src-000320 |
| [OTF](../../../../../shared/reference/participants/participant-src-000320-otf.md) | participant | src-000320 |
| [RE](../../../../../shared/reference/participants/participant-src-000320-re.md) | participant | src-000320 |
| [Relevant CA](../../../../../shared/reference/participants/participant-src-000320-relevant-ca.md) | participant | src-000320 |
| [Reporting Entity](../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md) | participant | src-000320 |
| [RM](../../../../../shared/reference/participants/participant-src-000320-rm.md) | participant | src-000320 |
| [SA](../../../../../shared/reference/participants/participant-src-000320-sa.md) | participant | src-000320 |
| [SI](../../../../../shared/reference/participants/participant-src-000320-si.md) | participant | src-000320 |
| [Supervisory Authority](../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md) | participant | src-000320 |
| [Reference Data](../../message-sets/fitrr/2025/flows/flow-src-000320-p127-reference-data.md) | business-flow | src-000320 |
| [Transparency Data](../../message-sets/fitrr/2025/flows/flow-src-000320-p131-transparency-data.md) | business-flow | src-000320 |
| [Trading Volume Cap](../../message-sets/fitrr/2025/flows/flow-src-000320-p135-trading-volume-cap.md) | business-flow | src-000320 |
| [Transaction Reporting Messages](../../message-sets/fitrr/2025/flows/flow-src-000320-p137-transaction-reporting-messages.md) | business-flow | src-000320 |
| [Reference Data Submission](../../message-sets/fitrr/2025/flows/flow-src-000320-p144-reference-data-submission.md) | business-flow | src-000320 |
| [Reference Data Distribution](../../message-sets/fitrr/2025/flows/flow-src-000320-p146-reference-data-distribution.md) | business-flow | src-000320 |
| [Non-Working Days](../../message-sets/fitrr/2025/flows/flow-src-000320-p148-non-working-days.md) | business-flow | src-000320 |
| [Missing / Incomplete Data Submission](../../message-sets/fitrr/2025/flows/flow-src-000320-p150-missing-incomplete-data-submission.md) | business-flow | src-000320 |
| [MiFIR specific additional Reference Data](../../message-sets/fitrr/2025/flows/flow-src-000320-p153-mi-fir-specific-additional-reference-data.md) | business-flow | src-000320 |
| [Transparency Trading Activity](../../message-sets/fitrr/2025/flows/flow-src-000320-p155-transparency-trading-activity.md) | business-flow | src-000320 |
| [Transparency Result Data](../../message-sets/fitrr/2025/flows/flow-src-000320-p157-transparency-result-data.md) | business-flow | src-000320 |
| [Trading Volume Cap](../../message-sets/fitrr/2025/flows/flow-src-000320-p159-trading-volume-cap.md) | business-flow | src-000320 |
| [Financial Instrument Transaction Report](../../message-sets/fitrr/2025/flows/flow-src-000320-p162-financial-instrument-transaction-report.md) | business-flow | src-000320 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)



<!-- FITRR-SEQUENCES -->
## Related FITRR business flows

- [Reference data — direct reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p175-direct-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0017.md)
- [Reference data — proxy reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p178-proxy-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0018.md)
- [Reference data — indirect reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p183-in-direct-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0019.md)
- [Non-working days — direct reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p188-direct-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0020.md)
- [Non-working days — proxy reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p191-proxy-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0021.md)
- [Non-working days — indirect reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p194-in-direct-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0022.md)
- [Incomplete reference data — direct reminder](../../message-sets/fitrr/2025/flows/flow-src-000320-p203-direct-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0024.md)
- [Incomplete reference data — indirect reminder](../../message-sets/fitrr/2025/flows/flow-src-000320-p206-proxy-and-in-direct-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0025.md)
- [Transparency data — direct reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p211-direct-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0026.md)
- [Transparency data — proxy reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p214-proxy-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0027.md)
- [Transparency data — indirect reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p217-in-direct-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0028.md)
- [Trading activity — direct reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p223-direct-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0029.md)
- [Trading activity — proxy reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p226-proxy-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0030.md)
- [Trading activity — indirect reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p229-in-direct-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0031.md)
- [Trading activity results — authority reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p234-in-direct-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0032.md)
- [Trading volume cap — direct reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p238-direct-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0033.md)
- [Trading volume cap — proxy reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p241-proxy-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0034.md)
- [Trading volume cap — indirect reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p244-in-direct-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0035.md)

These links use source-supported family context; exact-version applicability is separately documented in the message evidence.
