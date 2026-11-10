---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "auth.017.001.02"
message_family: "auth.017"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.017.001.02"
source_ids: ["src-000321"]
source_locations: [{"source_id": "src-000321", "heading": "3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02", "file_pages": [15, 38]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["July 2025"]
---

# auth.017.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000321 — 3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02

[src-000321](../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md); file pp15–38; publication July 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000321, 3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02, Functionality, file p15.**

This FinancialInstrumentReportingReferenceDataReport message is sent by the trading venue to the
national competent authority to report on the reference data used in the securities transactions.
Outline
The FinancialInstrumentReportingReferenceDataReportV02 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. ReportHeader
Header information related to the global report.
B. ReferenceData
Details of the reference data reported by the trading venue.
C. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 17 July 2025 auth.017.001.02
FinancialInstrumentReportingReferenceDataReport
V02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
15 July 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/fitrr/2025/documents/src-000321/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00009.md) | 15–15 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.2 Structure](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00010.md) | 16–16 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.3 Constraints](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00011.md) | 17–18 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.4 Message Building Blocks](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00012.md) | 19–20 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.4 Message Building Blocks / 3.4.2 ReferenceData &lt;RefData&gt; / 3.4.2.1 TechnicalRecordIdentification &lt;TechRcrdId&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00013.md) | 21–21 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.4 Message Building Blocks / 3.4.2 ReferenceData &lt;RefData&gt; / 3.4.2.2 FinancialInstrumentGeneralAttributes &lt;FinInstrmGnlAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00014.md) | 22–22 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.4 Message Building Blocks / 3.4.2 ReferenceData &lt;RefData&gt; / 3.4.2.2 FinancialInstrumentGeneralAttributes &lt;FinInstrmGnlAttrbts&gt; / 3.4.2.2.4 ClassificationType &lt;ClssfctnTp&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00015.md) | 23–23 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.4 Message Building Blocks / 3.4.2 ReferenceData &lt;RefData&gt; / 3.4.2.5 DebtInstrumentAttributes &lt;DebtInstrmAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00016.md) | 24–24 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.4 Message Building Blocks / 3.4.2 ReferenceData &lt;RefData&gt; / 3.4.2.5 DebtInstrumentAttributes &lt;DebtInstrmAttrbts&gt; / 3.4.2.5.2 MaturityDate &lt;MtrtyDt&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00017.md) | 25–25 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.4 Message Building Blocks / 3.4.2 ReferenceData &lt;RefData&gt; / 3.4.2.5 DebtInstrumentAttributes &lt;DebtInstrmAttrbts&gt; / 3.4.2.5.5 DebtSeniority &lt;DebtSnrty&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00018.md) | 26–27 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.4 Message Building Blocks / 3.4.2 ReferenceData &lt;RefData&gt; / 3.4.2.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 3.4.2.6.1 ExpiryDate &lt;XpryDt&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00019.md) | 28–28 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.4 Message Building Blocks / 3.4.2 ReferenceData &lt;RefData&gt; / 3.4.2.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 3.4.2.6.3 UnderlyingInstrument &lt;UndrlygInstrm&gt; / 3.4.2.6.3.2 Basket &lt;Bskt&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00020.md) | 29–29 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.4 Message Building Blocks / 3.4.2 ReferenceData &lt;RefData&gt; / 3.4.2.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 3.4.2.6.6 OptionExerciseStyle &lt;OptnExrcStyle&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00021.md) | 30–30 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.4 Message Building Blocks / 3.4.2 ReferenceData &lt;RefData&gt; / 3.4.2.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 3.4.2.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00022.md) | 31–31 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.4 Message Building Blocks / 3.4.2 ReferenceData &lt;RefData&gt; / 3.4.2.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 3.4.2.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 3.4.2.6.8.1 Commodity &lt;Cmmdty&gt; / 3.4.2.6.8.1.1 Product &lt;Pdct&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00023.md) | 32–32 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.4 Message Building Blocks / 3.4.2 ReferenceData &lt;RefData&gt; / 3.4.2.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 3.4.2.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 3.4.2.6.8.1 Commodity &lt;Cmmdty&gt; / 3.4.2.6.8.1.3 FinalPriceType &lt;FnlPricTp&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00024.md) | 33–33 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.4 Message Building Blocks / 3.4.2 ReferenceData &lt;RefData&gt; / 3.4.2.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 3.4.2.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 3.4.2.6.8.2 Interest &lt;Intrst&gt; / 3.4.2.6.8.2.2 FirstLegInterestRate &lt;FrstLegIntrstRate&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00025.md) | 34–34 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.4 Message Building Blocks / 3.4.2 ReferenceData &lt;RefData&gt; / 3.4.2.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 3.4.2.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 3.4.2.6.8.3 ForeignExchange &lt;FX&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00026.md) | 35–35 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.4 Message Building Blocks / 3.4.2 ReferenceData &lt;RefData&gt; / 3.4.2.7 TechnicalAttributes &lt;TechAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00027.md) | 36–36 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.4 Message Building Blocks / 3.4.2 ReferenceData &lt;RefData&gt; / 3.4.2.7 TechnicalAttributes &lt;TechAttrbts&gt; / 3.4.2.7.3 SubmissionDateTime &lt;SubmissnDtTm&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00028.md) | 37–37 |
| [3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02 / 3.4 Message Building Blocks / 3.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00029.md) | 38–38 |

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
- [Reference data distribution](../../message-sets/fitrr/2025/flows/flow-src-000320-p198-data-distribution-business-transaction.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0023.md)

These links use source-supported family context; exact-version applicability is separately documented in the message evidence.
