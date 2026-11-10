---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.5 ComputedAmount <CmptdAmt>"]
file_pages: [2798, 2799]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.5 ComputedAmount <CmptdAmt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2798 to 2799.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2798

```text
81.4.6.11.4.5  ComputedAmount <CmptdAmt>
Presence: [1..1]
Definition: Amount computed for this penalty.
ComputedAmount <CmptdAmt> contains the following elements (see "AmountAndDirection5" on
page 2841 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C4 2841
   CreditDebit <CdtDbt> [0..1] CodeSet 2842
81.4.6.11.4.6  CalculationMethod <ClctnMtd>
Presence: [0..1]
Definition: Provides the calculation rule used to compute the penalty.
Datatype: "PenaltyCalculationMethod1Code" on page 3268
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
81.4.6.11.4.7  NumberOfDays <NbOfDays>
Presence: [0..1]
Definition: Number of business days from/to the intended settlement date.
Datatype: "Number" on page 3324
81.4.6.11.4.8  CalculationData <ClctnData>
Presence: [0..*]
Definition: Further details for the calculation of the penalty.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2798 August 2026
```

## File page 2799

```text
CalculationData <ClctnData> contains the following PenaltyCalculationRecord1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [1..1] Date 2800
   MissingReferenceData <MssngRefData> [0..1] Indicator 2800
   FinancialInstrumentAttributes <FinInstrmAttrbts> [1..1]  2800
     Identification <Id> [1..1] ± C6, C7,
C10,
C11,
C13
2801
     SubjectToPenalties <SbjtToPnlties> [0..1] Indicator 2802
     ClassificationType <ClssfctnTp> [0..1] ± 2803
     Liquidity <Lqdty> [0..1] Indicator 2803
     PriceData <PricData> [0..1]  2803
       Value <Val> [1..1]  2803
{Or         Rate <Rate> [1..1] Rate 2804
Or}         Amount <Amt> [1..1] Amount C1, C5 2804
       SourceOfPrice <SrcOfPric> [0..1] ± 2804
       QuotationDate <QtnDt> [0..1] ± 2805
     ForeignExchangeData <FXData> [0..*]  2805
       ExchangeRate <XchgRate> [1..1] Rate 2805
       UnitCurrency <UnitCcy> [0..1] CodeSet C1 2805
       QuotedCurrency <QtdCcy> [0..1] CodeSet C1 2806
       QuotationDate <QtnDt> [0..1] ± 2806
     SecuritiesPenaltyRateData <SctiesPnltyRateData> [0..1]  2806
       MarketIdentification <MktId> [0..1] ± 2806
       SMEGrowthMarket <SMEGrwthMkt> [0..1] Indicator 2807
       Rate <Rate> [1..1] Rate 2807
   DiscountRate <DscntRate> [0..1]  2807
{Or     Rate <Rate> [1..1] Rate 2807
Or}     Amount <Amt> [1..1] Amount C1, C5 2807
   ForeignExchangeData <FXData> [0..*]  2808
     ExchangeRate <XchgRate> [1..1] Rate 2808
     UnitCurrency <UnitCcy> [0..1] CodeSet C1 2808
     QuotedCurrency <QtdCcy> [0..1] CodeSet C1 2809
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2799 August 2026
```

