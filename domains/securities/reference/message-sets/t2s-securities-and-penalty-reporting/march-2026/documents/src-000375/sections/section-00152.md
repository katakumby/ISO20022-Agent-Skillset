---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.4 PenaltyDetails <PnltyDtls>", "6.4.6.11.4.5 ComputedAmount <CmptdAmt>"]
file_pages: [216, 217]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.4.5 ComputedAmount <CmptdAmt>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 216 to 217.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 216

```text
6.4.6.11.4.5  ComputedAmount <CmptdAmt>
Presence: [1..1]
Definition: Amount computed for this penalty.
ComputedAmount <CmptdAmt> contains the following elements (see "AmountAndDirection5" on
page 250 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 251
   CreditDebit <CdtDbt> [0..1] CodeSet 251
6.4.6.11.4.6  CalculationMethod <ClctnMtd>
Presence: [0..1]
Definition: Provides the calculation rule used to compute the penalty.
Datatype: "PenaltyCalculationMethod1Code" on page 517
CodeName Name Definition
BOTH Both Sum of the penalty based on the quantity
of securities
failed to be delivered and penalty rate of
the securities and the penalty based on
the amount of cash failed to be delivered
and the discount rate of the currency.
CASH Cash Penalty is based on the amount of cash
failed to be delivered and the penalty
rate is the discount rate of the relevant
currency.
MIXE Mixed Penalty is based on the quantity of
securities failed to be delivered and
penalty rate is the discount rate of the
relevant currency.
SECU Securities Penalty is based on the quantity of
securities failed to be delivered and
penalty rate of the securities.
6.4.6.11.4.7  NumberOfDays <NbOfDays>
Presence: [0..1]
Definition: Number of business days from/to the intended settlement date.
Datatype: "Number" on page 554
6.4.6.11.4.8  CalculationData <ClctnData>
Presence: [0..*]
Definition: Further details for the calculation of the penalty.
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 216 March 2026
```

## File page 217

```text
CalculationData <ClctnData> contains the following PenaltyCalculationRecord1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [1..1] Date 218
   MissingReferenceData <MssngRefData> [0..1] Indicator 218
   FinancialInstrumentAttributes <FinInstrmAttrbts> [1..1]  218
     Identification <Id> [1..1] ± C6, C7,
C10,
C11,
C13
219
     SubjectToPenalties <SbjtToPnlties> [0..1] Indicator 220
     ClassificationType <ClssfctnTp> [0..1] ± 221
     Liquidity <Lqdty> [0..1] Indicator 221
     PriceData <PricData> [0..1]  221
       Value <Val> [1..1]  221
{Or         Rate <Rate> [1..1] Rate 222
Or}         Amount <Amt> [1..1] Amount C1, C5 222
       SourceOfPrice <SrcOfPric> [0..1] ± 222
       QuotationDate <QtnDt> [0..1] ± 223
     ForeignExchangeData <FXData> [0..*]  223
       ExchangeRate <XchgRate> [1..1] Rate 223
       UnitCurrency <UnitCcy> [0..1] CodeSet C1 223
       QuotedCurrency <QtdCcy> [0..1] CodeSet C1 224
       QuotationDate <QtnDt> [0..1] ± 224
     SecuritiesPenaltyRateData <SctiesPnltyRateData> [0..1]  224
       MarketIdentification <MktId> [0..1] ± 224
       SMEGrowthMarket <SMEGrwthMkt> [0..1] Indicator 225
       Rate <Rate> [1..1] Rate 225
   DiscountRate <DscntRate> [0..1]  225
{Or     Rate <Rate> [1..1] Rate 225
Or}     Amount <Amt> [1..1] Amount C1, C5 225
   ForeignExchangeData <FXData> [0..*]  226
     ExchangeRate <XchgRate> [1..1] Rate 226
     UnitCurrency <UnitCcy> [0..1] CodeSet C1 226
     QuotedCurrency <QtdCcy> [0..1] CodeSet C1 227
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 217 March 2026
```

