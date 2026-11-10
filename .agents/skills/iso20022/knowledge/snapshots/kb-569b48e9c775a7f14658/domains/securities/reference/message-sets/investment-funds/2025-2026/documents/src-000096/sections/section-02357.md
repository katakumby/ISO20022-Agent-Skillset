---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.23 IncomePreference <IncmPref>"]
file_pages: [3318, 3319, 3320]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.23 IncomePreference <IncmPref>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3318 to 3320.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3318

```text
ForeignExchangeDetails <FXDtls> contains the following elements (see "ForeignExchangeTerms37"
on page 4532 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ToAmount <ToAmt> [0..1] Amount C1, C13 4532
   FromAmount <FrAmt> [0..1] Amount C1, C13 4532
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 4533
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 4533
   ExchangeRate <XchgRate> [1..1] Rate 4534
   QuotationDate <QtnDt> [0..1] DateTime 4534
   QuotingInstitution <QtgInstn> [0..1] ± 4534
52.4.5.10.23  IncomePreference <IncmPref>
Presence: [0..1]
Definition: Dividend option chosen by the account owner based on the options offered in the
prospectus.
Datatype: "IncomePreference1Code" on page 5310
CodeName Name Definition
CASH Cash Distribution in cash.
DRIP DividendReinvestment Reinvestment of proceeds into
securities.
52.4.5.10.24  LetterIntentReference <LttrInttRef>
Presence: [0..1]
Definition: Reference of a letter of intent program, in which sales commissions are reduced based on
the aggregate of a customer's actual purchase and anticipated purchases, over a specific period of
time, and as agreed by the customer. A letter of intent program is mainly used in the US market.
Datatype: "Max35Text" on page 5403
52.4.5.10.25  AccumulationRightReference <AcmltnRghtRef>
Presence: [0..1]
Definition: Reference of an accumulation right program, in which sales commissions are based on a
customer's present purchases of shares and the aggregate quantity previously purchased by the
customer. An accumulation rights program is mainly used in the US market.
Datatype: "Max35Text" on page 5403
52.4.5.10.26  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees (charges/commission) and taxes that are taken into consideration for the transaction,
so that the total difference between the net amount and gross amount is known, without taking into
account equalisation.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3318 May 2026
```

## File page 3319

```text
Impacted by: C26 "NonStandardsSLAReferenceRule", C43 "TransactionOverheadElementRule"
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3319 May 2026
```

## File page 3320

```text
TransactionOverhead <TxOvrhd> contains the following TotalFeesAndTaxes45 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C3, C11 3321
   TotalFees <TtlFees> [0..1] Amount C3, C11 3322
   TotalTaxes <TtlTaxs> [0..1] Amount C3, C11 3322
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 3322
   IndividualFee <IndvFee> [0..*]  C6 3323
     Type <Tp> [1..1]  3323
{Or       Code <Cd> [1..1] CodeSet 3324
Or}       Proprietary <Prtry> [1..1] ± 3325
     Basis <Bsis> [0..1]  3325
{Or       Code <Cd> [1..1] CodeSet 3325
Or}       Proprietary <Prtry> [1..1] ± 3326
     StandardAmount <StdAmt> [0..1] Amount C3, C11 3326
     StandardRate <StdRate> [0..1] Rate 3326
     DiscountDetails <DscntDtls> [0..1]  C19 3327
       Amount <Amt> [0..1] Amount C3, C11 3327
       Rate <Rate> [0..1] Rate 3328
       Basis <Bsis> [0..1]  3328
{Or         Code <Cd> [1..1] CodeSet 3328
Or}         Proprietary <Prtry> [1..1] ± 3328
     AppliedAmount <ApldAmt> [0..1] Amount C3, C11 3329
     AppliedRate <ApldRate> [0..1] Rate 3329
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 3329
     RecipientIdentification <RcptId> [0..1] ± 3329
     InformativeIndicator <InftvInd> [1..1] Indicator 3330
   IndividualTax <IndvTax> [0..*] ± 3330
   DigitalNetworkFee <DgtlNtwkFee> [0..*]  3330
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C16,
C17,
C24,
C25,
C31
3331
       ISIN <ISIN> [0..1] IdentifierSet 3333
       OtherIdentification <OthrId> [0..*]  3333
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3320 May 2026
```

