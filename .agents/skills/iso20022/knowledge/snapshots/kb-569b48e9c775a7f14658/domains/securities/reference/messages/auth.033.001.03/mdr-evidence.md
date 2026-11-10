---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "auth.033.001.03"
message_family: "auth.033"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03"
source_ids: ["src-000321"]
source_locations: [{"source_id": "src-000321", "heading": "6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "file_pages": [55, 84]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["July 2025"]
---

# auth.033.001.03 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000321 — 6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03

[src-000321](../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md); file pp55–84; publication July 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000321, 6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03, Functionality, file p55.**

The FinancialInstrumentReportingNonEquityTransparencyDataReport message is sent by the trading
venue to the national competent authority to submit non equity specific details as part of classifying and
applying necessary transparency non equity computations.
Outline
The FinancialInstrumentReportingNonEquityTransparencyDataReportV03 MessageDefinition is
composed of 3 MessageBuildingBlocks:
A. ReportHeader
Header information related to the global report.
B. NonEquityTransparencyData
Details the non-equity transparency qualitative data reported by a trading venue.
C. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
55 July 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/fitrr/2025/documents/src-000321/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00044.md) | 55–55 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.2 Structure](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00045.md) | 56–57 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.3 Constraints](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00046.md) | 58–58 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00047.md) | 59–61 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.1 TechnicalRecordIdentification &lt;TechRcrdId&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00048.md) | 62–62 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.3 FullName &lt;FullNm&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00049.md) | 63–63 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.9 DerivativeContractType &lt;DerivCtrctTp&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00050.md) | 64–64 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.12 Derivative &lt;Deriv&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00051.md) | 65–67 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.12 Derivative &lt;Deriv&gt; / 6.4.2.12.1 Commodity &lt;Cmmdty&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00052.md) | 68–68 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.12 Derivative &lt;Deriv&gt; / 6.4.2.12.1 Commodity &lt;Cmmdty&gt; / 6.4.2.12.1.1 ClassSpecific &lt;ClssSpcfc&gt; / 6.4.2.12.1.1.1 Freight &lt;Frght&gt; / 6.4.2.12.1.1.1.2 AverageTimeCharter &lt;AvrgTmChrtr&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00053.md) | 69–69 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.12 Derivative &lt;Deriv&gt; / 6.4.2.12.2 InterestRate &lt;IntrstRate&gt; / 6.4.2.12.2.1 UnderlyingType &lt;UndrlygTp&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00054.md) | 70–70 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.12 Derivative &lt;Deriv&gt; / 6.4.2.12.2 InterestRate &lt;IntrstRate&gt; / 6.4.2.12.2.1 UnderlyingType &lt;UndrlygTp&gt; / 6.4.2.12.2.1.2 Other &lt;Othr&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00055.md) | 71–71 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.12 Derivative &lt;Deriv&gt; / 6.4.2.12.2 InterestRate &lt;IntrstRate&gt; / 6.4.2.12.2.2 UnderlyingBond &lt;UndrlygBd&gt; / 6.4.2.12.2.2.3 IssuanceDate &lt;IssncDt&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00056.md) | 72–72 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.12 Derivative &lt;Deriv&gt; / 6.4.2.12.2 InterestRate &lt;IntrstRate&gt; / 6.4.2.12.2.5 InflationIndex &lt;InfltnIndx&gt; / 6.4.2.12.2.5.2 Name &lt;Nm&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00057.md) | 73–73 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.12 Derivative &lt;Deriv&gt; / 6.4.2.12.4 Equity &lt;Eqty&gt; / 6.4.2.12.4.1 UnderlyingType &lt;UndrlygTp&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00058.md) | 74–74 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.12 Derivative &lt;Deriv&gt; / 6.4.2.12.4 Equity &lt;Eqty&gt; / 6.4.2.12.4.1 UnderlyingType &lt;UndrlygTp&gt; / 6.4.2.12.4.1.3 SingleName &lt;SnglNm&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00059.md) | 75–75 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.12 Derivative &lt;Deriv&gt; / 6.4.2.12.5 ContractForDifference &lt;CtrctForDiff&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00060.md) | 76–76 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.12 Derivative &lt;Deriv&gt; / 6.4.2.12.5 ContractForDifference &lt;CtrctForDiff&gt; / 6.4.2.12.5.3 NotionalCurrency2 &lt;NtnlCcy2&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00061.md) | 77–77 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.12 Derivative &lt;Deriv&gt; / 6.4.2.12.6 Credit &lt;Cdt&gt; / 6.4.2.12.6.1 SingleNameCreditDefaultSwap &lt;SnglNmCdtDfltSwp&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00062.md) | 78–78 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.12 Derivative &lt;Deriv&gt; / 6.4.2.12.6 Credit &lt;Cdt&gt; / 6.4.2.12.6.2 CreditDefaultSwapIndex &lt;CdtDfltSwpIndx&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00063.md) | 79–79 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.12 Derivative &lt;Deriv&gt; / 6.4.2.12.6 Credit &lt;Cdt&gt; / 6.4.2.12.6.2 CreditDefaultSwapIndex &lt;CdtDfltSwpIndx&gt; / 6.4.2.12.6.2.5 RollMonth &lt;RollMnth&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00064.md) | 80–80 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.12 Derivative &lt;Deriv&gt; / 6.4.2.12.6 Credit &lt;Cdt&gt; / 6.4.2.12.6.3 SingleNameCreditDefaultSwapDerivative &lt;SnglNmCdtDfltSwpDeriv&gt; / 6.4.2.12.6.3.1 UnderlyingCreditDefaultSwapIdentification &lt;UndrlygCdtDfltSwpId&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00065.md) | 81–81 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.12 Derivative &lt;Deriv&gt; / 6.4.2.12.6 Credit &lt;Cdt&gt; / 6.4.2.12.6.4 CreditDefaultSwapIndexDerivative &lt;CdtDfltSwpIndxDeriv&gt; / 6.4.2.12.6.4.1 UnderlyingCreditDefaultSwapIdentification &lt;UndrlygCdtDfltSwpId&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00066.md) | 82–82 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.12 Derivative &lt;Deriv&gt; / 6.4.2.12.6 Credit &lt;Cdt&gt; / 6.4.2.12.6.4 CreditDefaultSwapIndexDerivative &lt;CdtDfltSwpIndxDeriv&gt; / 6.4.2.12.6.4.2 UnderlyingCreditDefaultSwapIndex &lt;UndrlygCdtDfltSwpIndx&gt; / 6.4.2.12.6.4.2.2 UnderlyingIndexName &lt;UndrlygIndxNm&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00067.md) | 83–83 |
| [6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03 / 6.4 Message Building Blocks / 6.4.2 NonEquityTransparencyData &lt;NonEqtyTrnsprncyData&gt; / 6.4.2.12 Derivative &lt;Deriv&gt; / 6.4.2.12.7 EmissionAllowance &lt;EmssnAllwnc&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00068.md) | 84–84 |

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

- [Transparency data — direct reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p211-direct-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0026.md)
- [Transparency data — proxy reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p214-proxy-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0027.md)
- [Transparency data — indirect reporting](../../message-sets/fitrr/2025/flows/flow-src-000320-p217-in-direct-reporting.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0028.md)

These links use source-supported family context; exact-version applicability is separately documented in the message evidence.
