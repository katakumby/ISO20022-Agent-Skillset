---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.16 SettlementAmount <SttlmAmt>", "3.4.16.6 ForeignExchangeDetails <FXDtls>"]
file_pages: [124, 125]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.16.6 ForeignExchangeDetails <FXDtls>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 124 to 125.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 124

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
3.4.16.6  ForeignExchangeDetails <FXDtls>
Presence: [0..1]
Definition: Information needed to process a currency exchange or conversion.
ForeignExchangeDetails <FXDtls> contains the following elements (see "ForeignExchangeTerms18"
on page 259 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 260
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 260
   ExchangeRate <XchgRate> [1..1] Rate 260
   ConvertedAmount <ConvtdAmt> [1..1] Amount C1, C9 261
3.4.16.7  ValueDate <ValDt>
Presence: [0..1]
Definition: Date and time at which the cash is at the disposal of the credit account owner, or ceases to
be at the disposal of the debit account owner.
ValueDate <ValDt> contains one of the following elements (see "DateAndDateTime1Choice" on
page 263 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 263
Or}   DateTime <DtTm> [1..1] DateTime 263
3.4.17 OtherAmounts <OthrAmts>
Presence: [0..*]
Definition: Other amounts than the settlement amount.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 124 February 2025
```

## File page 125

```text
OtherAmounts <OthrAmts> contains the following elements (see "OtherAmounts16" on page 230 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ChargesFees <ChrgsFees> [0..1] ± 232
   CountryNationalFederalTax <CtryNtlFdrlTax> [0..1] ± 232
   ExecutingBrokerAmount <ExctgBrkrAmt> [0..1] ± 233
   IssueDiscountAllowance <IsseDscntAllwnc> [0..1] ± 233
   PaymentLevyTax <PmtLevyTax> [0..1] ± 233
   LocalTax <LclTax> [0..1] ± 234
   LocalBrokerCommission <LclBrkrComssn> [0..1] ± 234
   Margin <Mrgn> [0..1] ± 234
   Other <Othr> [0..1] ± 234
   RegulatoryAmount <RgltryAmt> [0..1] ± 235
   SpecialConcession <SpclCncssn> [0..1] ± 235
   StampDuty <StmpDty> [0..1] ± 235
   StockExchangeTax <StockXchgTax> [0..1] ± 236
   TransferTax <TrfTax> [0..1] ± 236
   TransactionTax <TxTax> [0..1] ± 236
   ValueAddedTax <ValAddedTax> [0..1] ± 237
   WithholdingTax <WhldgTax> [0..1] ± 237
   NetGainLoss <NetGnLoss> [0..1] ± 237
   ConsumptionTax <CsmptnTax> [0..1] ± 238
   MatchingConfirmationFee <MtchgConfFee> [0..1] ± 238
   ConvertedAmount <ConvtdAmt> [0..1] ± 238
   OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] ± 239
   BookValue <BookVal> [0..1] ± 239
   AccruedCapitalisationAmount <AcrdCptlstnAmt> [0..1] ± 239
   LocalTaxCountrySpecific1 <LclTaxCtrySpcfc1> [0..1] ± 240
   LocalTaxCountrySpecific2 <LclTaxCtrySpcfc2> [0..1] ± 240
   LocalTaxCountrySpecific3 <LclTaxCtrySpcfc3> [0..1] ± 240
   LocalTaxCountrySpecific4 <LclTaxCtrySpcfc4> [0..1] ± 241
   SharedBrokerageAmount <ShrdBrkrgAmt> [0..1] ± 241
   MarketMemberFeeAmount <MktMmbFeeAmt> [0..1] ± 241
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 125 February 2025
```

