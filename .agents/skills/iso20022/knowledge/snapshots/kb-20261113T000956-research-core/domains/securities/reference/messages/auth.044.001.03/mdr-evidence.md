---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "auth.044.001.03"
message_family: "auth.044"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.044.001.03"
source_ids: ["src-000321"]
source_locations: [{"source_id": "src-000321", "heading": "14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03", "file_pages": [217, 226]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["July 2025"]
---

# auth.044.001.03 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000321 — 14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03

[src-000321](../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md); file pp217–226; publication July 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000321, 14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03, Functionality, file p217.**

The FinancialInstrumentReportingEquityTradingActivityResult message is used by an entity or an
authority to provide information on computed results data of an equity specific trading activity.
Outline
The FinancialInstrumentReportingEquityTradingActivityResultV03 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. ReportHeader
Header to provide details on when and from whom the message originates.
B. EquityTransparencyData
Details the transparency data reported by a trading venue.
C. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 17 July 2025 auth.044.001.03
FinancialInstrumentReportingEquityTradingActivityR
esultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
217 July 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/fitrr/2025/documents/src-000321/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00177.md) | 217–217 |
| [14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03 / 14.2 Structure](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00178.md) | 218–218 |
| [14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03 / 14.4 Message Building Blocks](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00179.md) | 219–220 |
| [14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03 / 14.4 Message Building Blocks / 14.4.2 EquityTransparencyData &lt;EqtyTrnsprncyData&gt; / 14.4.2.1 TechnicalRecordIdentification &lt;TechRcrdId&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00180.md) | 221–221 |
| [14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03 / 14.4 Message Building Blocks / 14.4.2 EquityTransparencyData &lt;EqtyTrnsprncyData&gt; / 14.4.2.7 ApplicationPeriod &lt;ApplPrd&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00181.md) | 222–222 |
| [14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03 / 14.4 Message Building Blocks / 14.4.2 EquityTransparencyData &lt;EqtyTrnsprncyData&gt; / 14.4.2.10 Statistics &lt;Sttstcs&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00182.md) | 223–223 |
| [14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03 / 14.4 Message Building Blocks / 14.4.2 EquityTransparencyData &lt;EqtyTrnsprncyData&gt; / 14.4.2.10 Statistics &lt;Sttstcs&gt; / 14.4.2.10.2 AverageTransactionValue &lt;AvrgTxVal&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00183.md) | 224–224 |
| [14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03 / 14.4 Message Building Blocks / 14.4.2 EquityTransparencyData &lt;EqtyTrnsprncyData&gt; / 14.4.2.10 Statistics &lt;Sttstcs&gt; / 14.4.2.10.7 TotalVolumeOfTransactionsExecuted &lt;TtlVolOfTxsExctd&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00184.md) | 225–226 |

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

- [Trading activity results — authority reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p234-in-direct-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0032.md)

These links use source-supported family context; exact-version applicability is separately documented in the message evidence.
