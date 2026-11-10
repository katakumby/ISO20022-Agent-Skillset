---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "auth.042.001.02"
message_family: "auth.042"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02"
source_ids: ["src-000321"]
source_locations: [{"source_id": "src-000321", "heading": "12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02", "file_pages": [184, 210]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["July 2025"]
---

# auth.042.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000321 — 12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02

[src-000321](../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf); file pp184–210; publication July 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000321, 12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02, Functionality, file p184.**

The FinancialInstrumentReportingInvalidReferenceDataReport message is sent by the trading venue to
the national competent authority to report on all records that have become invalid based on updates
that have been received or that have passed the termination date original set for the instrument.
Outline
The FinancialInstrumentReportingInvalidReferenceDataReportV02 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. DatePeriod
Date period capturing when instruments in the report have been invalidated
Usage:
Within MiFIR, only the From Date To Date field will be used with the From Date corresponding to
the date the first instrument was added to this report while the To Date is the date the last
instrument was added to the file.
B. NumberOfRecords
Number of invalid records in this message.
C. FinancialInstruments
Provides the details of the financial instruments.
D. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 17 July 2025 auth.042.001.02
FinancialInstrumentReportingInvalidReferenceData
ReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
184 July 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/fitrr/2025/documents/src-000321/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00149.md) | 184–184 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.2 Structure](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00150.md) | 185–185 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.3 Constraints](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00151.md) | 186–187 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00152.md) | 188–188 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.2 NumberOfRecords &lt;NbOfRcrds&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00153.md) | 189–190 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.3 FinancialInstruments &lt;FinInstrms&gt; / 12.4.3.1 FinancialInstrument &lt;FinInstrm&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00154.md) | 191–192 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.3 FinancialInstruments &lt;FinInstrms&gt; / 12.4.3.1 FinancialInstrument &lt;FinInstrm&gt; / 12.4.3.1.1 TechnicalRecordIdentification &lt;TechRcrdId&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00155.md) | 193–193 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.3 FinancialInstruments &lt;FinInstrms&gt; / 12.4.3.1 FinancialInstrument &lt;FinInstrm&gt; / 12.4.3.1.2 FinancialInstrumentGeneralAttributes &lt;FinInstrmGnlAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00156.md) | 194–194 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.3 FinancialInstruments &lt;FinInstrms&gt; / 12.4.3.1 FinancialInstrument &lt;FinInstrm&gt; / 12.4.3.1.2 FinancialInstrumentGeneralAttributes &lt;FinInstrmGnlAttrbts&gt; / 12.4.3.1.2.4 ClassificationType &lt;ClssfctnTp&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00157.md) | 195–195 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.3 FinancialInstruments &lt;FinInstrms&gt; / 12.4.3.1 FinancialInstrument &lt;FinInstrm&gt; / 12.4.3.1.5 DebtInstrumentAttributes &lt;DebtInstrmAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00158.md) | 196–196 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.3 FinancialInstruments &lt;FinInstrms&gt; / 12.4.3.1 FinancialInstrument &lt;FinInstrm&gt; / 12.4.3.1.5 DebtInstrumentAttributes &lt;DebtInstrmAttrbts&gt; / 12.4.3.1.5.2 MaturityDate &lt;MtrtyDt&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00159.md) | 197–197 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.3 FinancialInstruments &lt;FinInstrms&gt; / 12.4.3.1 FinancialInstrument &lt;FinInstrm&gt; / 12.4.3.1.5 DebtInstrumentAttributes &lt;DebtInstrmAttrbts&gt; / 12.4.3.1.5.5 DebtSeniority &lt;DebtSnrty&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00160.md) | 198–199 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.3 FinancialInstruments &lt;FinInstrms&gt; / 12.4.3.1 FinancialInstrument &lt;FinInstrm&gt; / 12.4.3.1.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 12.4.3.1.6.1 ExpiryDate &lt;XpryDt&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00161.md) | 200–200 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.3 FinancialInstruments &lt;FinInstrms&gt; / 12.4.3.1 FinancialInstrument &lt;FinInstrm&gt; / 12.4.3.1.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 12.4.3.1.6.3 UnderlyingInstrument &lt;UndrlygInstrm&gt; / 12.4.3.1.6.3.2 Basket &lt;Bskt&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00162.md) | 201–201 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.3 FinancialInstruments &lt;FinInstrms&gt; / 12.4.3.1 FinancialInstrument &lt;FinInstrm&gt; / 12.4.3.1.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 12.4.3.1.6.6 OptionExerciseStyle &lt;OptnExrcStyle&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00163.md) | 202–202 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.3 FinancialInstruments &lt;FinInstrms&gt; / 12.4.3.1 FinancialInstrument &lt;FinInstrm&gt; / 12.4.3.1.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 12.4.3.1.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00164.md) | 203–203 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.3 FinancialInstruments &lt;FinInstrms&gt; / 12.4.3.1 FinancialInstrument &lt;FinInstrm&gt; / 12.4.3.1.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 12.4.3.1.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 12.4.3.1.6.8.1 Commodity &lt;Cmmdty&gt; / 12.4.3.1.6.8.1.1 Product &lt;Pdct&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00165.md) | 204–204 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.3 FinancialInstruments &lt;FinInstrms&gt; / 12.4.3.1 FinancialInstrument &lt;FinInstrm&gt; / 12.4.3.1.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 12.4.3.1.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 12.4.3.1.6.8.1 Commodity &lt;Cmmdty&gt; / 12.4.3.1.6.8.1.3 FinalPriceType &lt;FnlPricTp&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00166.md) | 205–205 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.3 FinancialInstruments &lt;FinInstrms&gt; / 12.4.3.1 FinancialInstrument &lt;FinInstrm&gt; / 12.4.3.1.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 12.4.3.1.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 12.4.3.1.6.8.2 Interest &lt;Intrst&gt; / 12.4.3.1.6.8.2.2 FirstLegInterestRate &lt;FrstLegIntrstRate&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00167.md) | 206–206 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.3 FinancialInstruments &lt;FinInstrms&gt; / 12.4.3.1 FinancialInstrument &lt;FinInstrm&gt; / 12.4.3.1.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 12.4.3.1.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 12.4.3.1.6.8.3 ForeignExchange &lt;FX&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00168.md) | 207–207 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.3 FinancialInstruments &lt;FinInstrms&gt; / 12.4.3.1 FinancialInstrument &lt;FinInstrm&gt; / 12.4.3.1.7 TechnicalAttributes &lt;TechAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00169.md) | 208–208 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.3 FinancialInstruments &lt;FinInstrms&gt; / 12.4.3.1 FinancialInstrument &lt;FinInstrm&gt; / 12.4.3.1.7 TechnicalAttributes &lt;TechAttrbts&gt; / 12.4.3.1.7.4 RelevantCompetentAuthority &lt;RlvntCmptntAuthrty&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00170.md) | 209–209 |
| [12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02 / 12.4 Message Building Blocks / 12.4.3 FinancialInstruments &lt;FinInstrms&gt; / 12.4.3.2 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00171.md) | 210–210 |

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

- [Reference data distribution](../../message-sets/fitrr/2025/flows/flow-src-000320-p198-data-distribution-business-transaction.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0023.md)

These links use source-supported family context; exact-version applicability is separately documented in the message evidence.
