---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["11 auth.041.001.01 FinancialInstrumentReportingNonEquityTradingActivityReportV01", "11.4 Message Building Blocks"]
file_pages: [180]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.041.001.01"]
---

# 11.4 Message Building Blocks

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 180 to 180.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 180

```text
11.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
11.4.1 ReportHeader <RptHdr>
Presence: [1..1]
Definition: Header information related to the global report.
ReportHeader <RptHdr> contains the following elements (see "SecuritiesMarketReportHeader1" on
page 411 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportingEntity <RptgNtty> [1..1] ± C19 411
   ReportingPeriod <RptgPrd> [1..1] ± 411
   SubmissionDateTime <SubmissnDtTm> [0..1] DateTime 411
11.4.2 NonEquityTransparencyData
<NonEqtyTrnsprncyData>
Presence: [1..*]
Definition: Details the transparency data reported by a trading venue.
Impacted by: C3 "ValidISINRule", C5 "ValidMICRule"
NonEquityTransparencyData <NonEqtyTrnsprncyData> contains the following
TransparencyDataReport15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TechnicalRecordIdentification <TechRcrdId> [0..1] Text 181
   Identification <Id> [1..1] IdentifierSet 181
   ReportingDate <RptgDt> [0..1] Date 181
   TradingVenue <TradgVn> [0..1] IdentifierSet 181
   Suspension <Sspnsn> [1..1] Indicator 181
   NumberTransactions <NbTxs> [0..1] Quantity 182
   AggregatedQuantitativeData <AggtdQttvData> [0..*]  182
     NumberOfTransactions <NbOfTxs> [1..1] Quantity 182
     TotalNotionalAmount <TtlNtnlAmt> [1..1] Quantity 182
     Range <Rg> [1..1]  182
       FromQuantity <FrQty> [1..1] Quantity 183
       ToQuantity <ToQty> [1..1] Quantity 183
Approved by the Securities SEG on 17 July 2025 auth.041.001.01
FinancialInstrumentReportingNonEquityTradingActi
vityReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
180 July 2025
```

