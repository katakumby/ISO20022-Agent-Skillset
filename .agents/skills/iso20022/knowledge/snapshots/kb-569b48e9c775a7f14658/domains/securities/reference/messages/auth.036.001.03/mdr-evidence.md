---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "auth.036.001.03"
message_family: "auth.036"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03"
source_ids: ["src-000321"]
source_locations: [{"source_id": "src-000321", "heading": "8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "file_pages": [91, 165]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["July 2025"]
---

# auth.036.001.03 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000321 — 8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03

[src-000321](../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md); file pp91–165; publication July 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000321, 8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03, Functionality, file p91.**

The FinancialInstrumentReportingReferenceDataDeltaReport message is sent by the trading venues to
the national competent authority to report on changes that have occurred in the base data between
reference data file generation.
Outline
The FinancialInstrumentReportingReferenceDataDeltaReportV03 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. ReportHeader
Header information related to the global report.
B. FinancialInstrument
Provides the details of the reference data that have been updated (since the last report).
C. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
91 July 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/fitrr/2025/documents/src-000321/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00075.md) | 91–91 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.2 Structure](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00076.md) | 92–96 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.3 Constraints](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00077.md) | 97–98 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00078.md) | 99–104 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.1 ModifiedRecord &lt;ModfdRcrd&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00079.md) | 105–106 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.1 ModifiedRecord &lt;ModfdRcrd&gt; / 8.4.2.1.1 TechnicalRecordIdentification &lt;TechRcrdId&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00080.md) | 107–107 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.1 ModifiedRecord &lt;ModfdRcrd&gt; / 8.4.2.1.2 FinancialInstrumentGeneralAttributes &lt;FinInstrmGnlAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00081.md) | 108–108 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.1 ModifiedRecord &lt;ModfdRcrd&gt; / 8.4.2.1.2 FinancialInstrumentGeneralAttributes &lt;FinInstrmGnlAttrbts&gt; / 8.4.2.1.2.4 ClassificationType &lt;ClssfctnTp&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00082.md) | 109–109 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.1 ModifiedRecord &lt;ModfdRcrd&gt; / 8.4.2.1.5 DebtInstrumentAttributes &lt;DebtInstrmAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00083.md) | 110–110 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.1 ModifiedRecord &lt;ModfdRcrd&gt; / 8.4.2.1.5 DebtInstrumentAttributes &lt;DebtInstrmAttrbts&gt; / 8.4.2.1.5.2 MaturityDate &lt;MtrtyDt&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00084.md) | 111–111 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.1 ModifiedRecord &lt;ModfdRcrd&gt; / 8.4.2.1.5 DebtInstrumentAttributes &lt;DebtInstrmAttrbts&gt; / 8.4.2.1.5.5 DebtSeniority &lt;DebtSnrty&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00085.md) | 112–113 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.1 ModifiedRecord &lt;ModfdRcrd&gt; / 8.4.2.1.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.1.6.1 ExpiryDate &lt;XpryDt&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00086.md) | 114–114 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.1 ModifiedRecord &lt;ModfdRcrd&gt; / 8.4.2.1.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.1.6.3 UnderlyingInstrument &lt;UndrlygInstrm&gt; / 8.4.2.1.6.3.2 Basket &lt;Bskt&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00087.md) | 115–115 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.1 ModifiedRecord &lt;ModfdRcrd&gt; / 8.4.2.1.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.1.6.6 OptionExerciseStyle &lt;OptnExrcStyle&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00088.md) | 116–116 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.1 ModifiedRecord &lt;ModfdRcrd&gt; / 8.4.2.1.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.1.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00089.md) | 117–117 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.1 ModifiedRecord &lt;ModfdRcrd&gt; / 8.4.2.1.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.1.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 8.4.2.1.6.8.1 Commodity &lt;Cmmdty&gt; / 8.4.2.1.6.8.1.1 Product &lt;Pdct&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00090.md) | 118–118 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.1 ModifiedRecord &lt;ModfdRcrd&gt; / 8.4.2.1.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.1.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 8.4.2.1.6.8.1 Commodity &lt;Cmmdty&gt; / 8.4.2.1.6.8.1.3 FinalPriceType &lt;FnlPricTp&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00091.md) | 119–119 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.1 ModifiedRecord &lt;ModfdRcrd&gt; / 8.4.2.1.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.1.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 8.4.2.1.6.8.2 Interest &lt;Intrst&gt; / 8.4.2.1.6.8.2.2 FirstLegInterestRate &lt;FrstLegIntrstRate&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00092.md) | 120–120 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.1 ModifiedRecord &lt;ModfdRcrd&gt; / 8.4.2.1.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.1.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 8.4.2.1.6.8.3 ForeignExchange &lt;FX&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00093.md) | 121–121 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.1 ModifiedRecord &lt;ModfdRcrd&gt; / 8.4.2.1.7 TechnicalAttributes &lt;TechAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00094.md) | 122–122 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.1 ModifiedRecord &lt;ModfdRcrd&gt; / 8.4.2.1.7 TechnicalAttributes &lt;TechAttrbts&gt; / 8.4.2.1.7.4 RelevantCompetentAuthority &lt;RlvntCmptntAuthrty&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00095.md) | 123–123 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.2 NewRecord &lt;NewRcrd&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00096.md) | 124–125 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.2 NewRecord &lt;NewRcrd&gt; / 8.4.2.2.1 TechnicalRecordIdentification &lt;TechRcrdId&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00097.md) | 126–126 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.2 NewRecord &lt;NewRcrd&gt; / 8.4.2.2.2 FinancialInstrumentGeneralAttributes &lt;FinInstrmGnlAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00098.md) | 127–127 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.2 NewRecord &lt;NewRcrd&gt; / 8.4.2.2.2 FinancialInstrumentGeneralAttributes &lt;FinInstrmGnlAttrbts&gt; / 8.4.2.2.2.4 ClassificationType &lt;ClssfctnTp&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00099.md) | 128–128 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.2 NewRecord &lt;NewRcrd&gt; / 8.4.2.2.5 DebtInstrumentAttributes &lt;DebtInstrmAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00100.md) | 129–129 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.2 NewRecord &lt;NewRcrd&gt; / 8.4.2.2.5 DebtInstrumentAttributes &lt;DebtInstrmAttrbts&gt; / 8.4.2.2.5.2 MaturityDate &lt;MtrtyDt&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00101.md) | 130–130 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.2 NewRecord &lt;NewRcrd&gt; / 8.4.2.2.5 DebtInstrumentAttributes &lt;DebtInstrmAttrbts&gt; / 8.4.2.2.5.5 DebtSeniority &lt;DebtSnrty&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00102.md) | 131–132 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.2 NewRecord &lt;NewRcrd&gt; / 8.4.2.2.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.2.6.1 ExpiryDate &lt;XpryDt&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00103.md) | 133–133 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.2 NewRecord &lt;NewRcrd&gt; / 8.4.2.2.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.2.6.3 UnderlyingInstrument &lt;UndrlygInstrm&gt; / 8.4.2.2.6.3.2 Basket &lt;Bskt&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00104.md) | 134–134 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.2 NewRecord &lt;NewRcrd&gt; / 8.4.2.2.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.2.6.6 OptionExerciseStyle &lt;OptnExrcStyle&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00105.md) | 135–135 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.2 NewRecord &lt;NewRcrd&gt; / 8.4.2.2.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.2.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00106.md) | 136–136 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.2 NewRecord &lt;NewRcrd&gt; / 8.4.2.2.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.2.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 8.4.2.2.6.8.1 Commodity &lt;Cmmdty&gt; / 8.4.2.2.6.8.1.1 Product &lt;Pdct&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00107.md) | 137–137 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.2 NewRecord &lt;NewRcrd&gt; / 8.4.2.2.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.2.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 8.4.2.2.6.8.1 Commodity &lt;Cmmdty&gt; / 8.4.2.2.6.8.1.3 FinalPriceType &lt;FnlPricTp&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00108.md) | 138–138 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.2 NewRecord &lt;NewRcrd&gt; / 8.4.2.2.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.2.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 8.4.2.2.6.8.2 Interest &lt;Intrst&gt; / 8.4.2.2.6.8.2.2 FirstLegInterestRate &lt;FrstLegIntrstRate&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00109.md) | 139–139 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.2 NewRecord &lt;NewRcrd&gt; / 8.4.2.2.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.2.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 8.4.2.2.6.8.3 ForeignExchange &lt;FX&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00110.md) | 140–140 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.2 NewRecord &lt;NewRcrd&gt; / 8.4.2.2.7 TechnicalAttributes &lt;TechAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00111.md) | 141–141 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.2 NewRecord &lt;NewRcrd&gt; / 8.4.2.2.7 TechnicalAttributes &lt;TechAttrbts&gt; / 8.4.2.2.7.4 RelevantCompetentAuthority &lt;RlvntCmptntAuthrty&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00112.md) | 142–142 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.3 TerminatedRecord &lt;TermntdRcrd&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00113.md) | 143–144 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.3 TerminatedRecord &lt;TermntdRcrd&gt; / 8.4.2.3.1 TechnicalRecordIdentification &lt;TechRcrdId&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00114.md) | 145–145 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.3 TerminatedRecord &lt;TermntdRcrd&gt; / 8.4.2.3.2 FinancialInstrumentGeneralAttributes &lt;FinInstrmGnlAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00115.md) | 146–146 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.3 TerminatedRecord &lt;TermntdRcrd&gt; / 8.4.2.3.2 FinancialInstrumentGeneralAttributes &lt;FinInstrmGnlAttrbts&gt; / 8.4.2.3.2.4 ClassificationType &lt;ClssfctnTp&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00116.md) | 147–147 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.3 TerminatedRecord &lt;TermntdRcrd&gt; / 8.4.2.3.5 DebtInstrumentAttributes &lt;DebtInstrmAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00117.md) | 148–148 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.3 TerminatedRecord &lt;TermntdRcrd&gt; / 8.4.2.3.5 DebtInstrumentAttributes &lt;DebtInstrmAttrbts&gt; / 8.4.2.3.5.2 MaturityDate &lt;MtrtyDt&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00118.md) | 149–149 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.3 TerminatedRecord &lt;TermntdRcrd&gt; / 8.4.2.3.5 DebtInstrumentAttributes &lt;DebtInstrmAttrbts&gt; / 8.4.2.3.5.5 DebtSeniority &lt;DebtSnrty&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00119.md) | 150–151 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.3 TerminatedRecord &lt;TermntdRcrd&gt; / 8.4.2.3.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.3.6.1 ExpiryDate &lt;XpryDt&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00120.md) | 152–152 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.3 TerminatedRecord &lt;TermntdRcrd&gt; / 8.4.2.3.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.3.6.3 UnderlyingInstrument &lt;UndrlygInstrm&gt; / 8.4.2.3.6.3.2 Basket &lt;Bskt&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00121.md) | 153–153 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.3 TerminatedRecord &lt;TermntdRcrd&gt; / 8.4.2.3.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.3.6.6 OptionExerciseStyle &lt;OptnExrcStyle&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00122.md) | 154–154 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.3 TerminatedRecord &lt;TermntdRcrd&gt; / 8.4.2.3.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.3.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00123.md) | 155–155 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.3 TerminatedRecord &lt;TermntdRcrd&gt; / 8.4.2.3.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.3.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 8.4.2.3.6.8.1 Commodity &lt;Cmmdty&gt; / 8.4.2.3.6.8.1.1 Product &lt;Pdct&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00124.md) | 156–156 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.3 TerminatedRecord &lt;TermntdRcrd&gt; / 8.4.2.3.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.3.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 8.4.2.3.6.8.1 Commodity &lt;Cmmdty&gt; / 8.4.2.3.6.8.1.3 FinalPriceType &lt;FnlPricTp&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00125.md) | 157–157 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.3 TerminatedRecord &lt;TermntdRcrd&gt; / 8.4.2.3.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.3.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 8.4.2.3.6.8.2 Interest &lt;Intrst&gt; / 8.4.2.3.6.8.2.2 FirstLegInterestRate &lt;FrstLegIntrstRate&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00126.md) | 158–158 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.3 TerminatedRecord &lt;TermntdRcrd&gt; / 8.4.2.3.6 DerivativeInstrumentAttributes &lt;DerivInstrmAttrbts&gt; / 8.4.2.3.6.8 AssetClassSpecificAttributes &lt;AsstClssSpcfcAttrbts&gt; / 8.4.2.3.6.8.3 ForeignExchange &lt;FX&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00127.md) | 159–159 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.3 TerminatedRecord &lt;TermntdRcrd&gt; / 8.4.2.3.7 TechnicalAttributes &lt;TechAttrbts&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00128.md) | 160–160 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.3 TerminatedRecord &lt;TermntdRcrd&gt; / 8.4.2.3.7 TechnicalAttributes &lt;TechAttrbts&gt; / 8.4.2.3.7.4 RelevantCompetentAuthority &lt;RlvntCmptntAuthrty&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00129.md) | 161–161 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrument &lt;FinInstrm&gt; / 8.4.2.4 CancelledRecord &lt;CancRcrd&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00130.md) | 162–163 |
| [8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03 / 8.4 Message Building Blocks / 8.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00131.md) | 164–165 |

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
