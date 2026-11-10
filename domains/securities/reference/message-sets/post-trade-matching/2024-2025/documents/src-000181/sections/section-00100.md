---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.20 TwoLegTransactionDetails <TwoLegTxDtls>", "3.4.20.4 GrossTradeAmount <GrssTradAmt>"]
file_pages: [131, 132]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.20.4 GrossTradeAmount <GrssTradAmt>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 131 to 132.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 131

```text
Definition: Unambiguous identification of the second leg of the transaction as known by the account
owner (or the instructing party acting on its behalf).
Datatype: "Max35Text" on page 669
3.4.20.4  GrossTradeAmount <GrssTradAmt>
Presence: [0..1]
Definition: Principal amount of a trade (price multiplied by quantity).
GrossTradeAmount <GrssTradAmt> contains the following elements (see "AmountAndDirection29"
on page 228 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C10 228
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 229
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C10 229
   ForeignExchangeDetails <FXDtls> [0..1] ± 229
3.4.20.5  OtherAmounts <OthrAmts>
Presence: [0..*]
Definition: Identifies other amounts pertaining to the transaction.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 131 February 2025
```

## File page 132

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
Post Trade Matching - Maintenance 2024 - 2025 132 February 2025
```

