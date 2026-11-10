---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "auth.045.001.03"
message_family: "auth.045"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03"
source_ids: ["src-000321"]
source_locations: [{"source_id": "src-000321", "heading": "15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03", "file_pages": [227, 243]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["July 2025"]
---

# auth.045.001.03 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000321 — 15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03

[src-000321](../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf); file pp227–243; publication July 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000321, 15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03, Functionality, file p227.**

The FinancialInstrumentReportingNonEquityTradingActivityResult message is sent by the trading venue
to the national competent authority to report on computed results data of non-equity specific trading
activity.
Outline
The FinancialInstrumentReportingNonEquityTradingActivityResultV03 MessageDefinition is composed
of 3 MessageBuildingBlocks:
A. ReportHeader
Header information related to the global report.
B. NonEquityTransparencyData
Details the transparency data reported by a trading venue.
C. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 17 July 2025 auth.045.001.03
FinancialInstrumentReportingNonEquityTradingActi
vityResultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
227 July 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/fitrr/2025/documents/src-000321/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00185.md) | 227–227 |
| [15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03 / 15.2 Structure](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00186.md) | 228–228 |
| [15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03 / 15.3 Constraints](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00187.md) | 229–229 |
| [15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03 / 15.4 Message Building Blocks / 15.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00188.md) | 230–231 |
| [15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03 / 15.4 Message Building Blocks / 15.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 15.4.2.1 TechnicalRecordIdentification &lt;TechRcrdId&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00189.md) | 232–232 |
| [15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03 / 15.4 Message Building Blocks / 15.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 15.4.2.2 Identification &lt;Id&gt; / 15.4.2.2.1 ISINAndSubClass &lt;ISINAndSubClss&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00190.md) | 233–233 |
| [15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03 / 15.4 Message Building Blocks / 15.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 15.4.2.2 Identification &lt;Id&gt; / 15.4.2.2.1 ISINAndSubClass &lt;ISINAndSubClss&gt; / 15.4.2.2.1.1 ISIN &lt;ISIN&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00191.md) | 234–234 |
| [15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03 / 15.4 Message Building Blocks / 15.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 15.4.2.2 Identification &lt;Id&gt; / 15.4.2.2.1 ISINAndSubClass &lt;ISINAndSubClss&gt; / 15.4.2.2.1.2 DerivativeSubClass &lt;DerivSubClss&gt; / 15.4.2.2.1.2.2 SegmentationCriteria &lt;SgmttnCrit&gt; / 15.4.2.2.1.2.2.1 CriteriaName &lt;CritNm&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00192.md) | 235–235 |
| [15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03 / 15.4 Message Building Blocks / 15.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 15.4.2.2 Identification &lt;Id&gt; / 15.4.2.2.1 ISINAndSubClass &lt;ISINAndSubClss&gt; / 15.4.2.2.1.2 DerivativeSubClass &lt;DerivSubClss&gt; / 15.4.2.2.1.2.2 SegmentationCriteria &lt;SgmttnCrit&gt; / 15.4.2.2.1.2.2.2 CriteriaValue &lt;CritVal&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00193.md) | 236–236 |
| [15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03 / 15.4 Message Building Blocks / 15.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 15.4.2.2 Identification &lt;Id&gt; / 15.4.2.2.2 AssetClassAndSubClass &lt;AsstClssAndSubClss&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00194.md) | 237–237 |
| [15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03 / 15.4 Message Building Blocks / 15.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 15.4.2.2 Identification &lt;Id&gt; / 15.4.2.2.2 AssetClassAndSubClass &lt;AsstClssAndSubClss&gt; / 15.4.2.2.2.2 DerivativeSubClass &lt;DerivSubClss&gt; / 15.4.2.2.2.2.1 Description &lt;Desc&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00195.md) | 238–239 |
| [15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03 / 15.4 Message Building Blocks / 15.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 15.4.2.2 Identification &lt;Id&gt; / 15.4.2.2.2 AssetClassAndSubClass &lt;AsstClssAndSubClss&gt; / 15.4.2.2.2.2 DerivativeSubClass &lt;DerivSubClss&gt; / 15.4.2.2.2.2.2 SegmentationCriteria &lt;SgmttnCrit&gt; / 15.4.2.2.2.2.2.2 CriteriaValue &lt;CritVal&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00196.md) | 240–240 |
| [15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03 / 15.4 Message Building Blocks / 15.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 15.4.2.6 Liquidity &lt;Lqdty&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00197.md) | 241–241 |
| [15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03 / 15.4 Message Building Blocks / 15.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 15.4.2.9 PreTradeInstrumentSizeSpecificThreshold &lt;PreTradInstrmSzSpcfcThrshld&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00198.md) | 242–242 |
| [15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03 / 15.4 Message Building Blocks / 15.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00199.md) | 243–243 |

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
