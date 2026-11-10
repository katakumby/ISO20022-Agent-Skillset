---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.4 Message Building Blocks", "6.4.9 CounterpartyTradingDetails <CtrPtyTradgDtls>"]
file_pages: [194, 195, 196]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6.4.9 CounterpartyTradingDetails <CtrPtyTradgDtls>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 194 to 196.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 194

```text
- a forex deal to fund the purchase of securities should be executed in time for the currency to be
available on the settlement date of the securities transaction.
- a bilateral agreement regarding the use of this field has been established.
If CurrencyToBuy is used, then it implies the following:
- the instruction is to delivery
- the currency received as proceeds from the sale of securities, eg, the currency to be sold, is the
currency of the settlement amount. The currency to be bought is provided by the currency to buy
message element. If proceeds are repatriated, this is in the base currency of the portfolio.
- the amount of currency to be sold is equal to the settlement amount of the transaction. This implies
a bulk forex deal must be instructed by other means.
- a forex deal to repatriate proceeds after the sale of securities should be executed for the soonest
possible value date after settlement of the securities, as permitted by market convention.
- a bilateral agreement regarding the use of this field has been established.
• PlaceOfTradeRule
If PlaceOfTrade is used and a ISO 10383 MIC exists for the market to be identified, then the ISO
10383 Market Identifier Code (MIC) must be used.
• TradeDateTimeUTCRule
If Trade Date/Time is used with a time or a time + UTC indicator, then it must be the local time of the
place of trade, eg, of the stock exchange, or of the selling broker for OTC.
6.4.9 CounterpartyTradingDetails <CtrPtyTradgDtls>
Presence: [0..1]
Definition: Details of the trading counterparty.
Impacted by: C11 "CurrencyToBuyOrSellRule", C32 "PlaceOfTradeRule", C38
"TradeDateTimeUTCRule"
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 194 February 2025
```

## File page 195

```text
CounterpartyTradingDetails <CtrPtyTradgDtls> contains the following elements (see "Order23" on
page 335 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BusinessProcessType <BizPrcTp> [0..1] ± 338
   OrderIdentification <OrdrId> [0..*] Text 338
   ClientOrderIdentification <ClntOrdrId> [0..*] Text 338
   SecondaryClientOrderIdentification <ScndryClntOrdrId> [0..*] Text 339
   ListIdentification <ListId> [0..*] Text 339
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C13,
C14,
C19,
C20,
C26
339
   Side <Sd> [1..1] CodeSet 340
   Payment <Pmt> [0..1] CodeSet 341
   TradeTransactionType <TradTxTp> [0..1] ± 342
   TradeTransactionCondition <TradTxCond> [0..*] ± 342
   PreAdvice <PreAdvc> [0..1] Indicator 342
   PlaceOfTrade <PlcOfTrad> [0..1] ± C16,
C23,
C33
342
   OrderBookingDate <OrdrBookgDt> [0..1] Date 343
   TradeOriginationDate <TradOrgtnDt> [0..1] DateTime 343
   TradeDate <TradDt> [1..1] ± 343
   ProcessingDate <PrcgDt> [0..1] ± 344
   SettlementDate <SttlmDt> [1..1] ± 344
   NAVDate <NAVDt> [0..1] ± 344
   PartialFillDetails <PrtlFillDtls> [0..*] ± C27 345
   ConfirmationQuantity <ConfQty> [1..1] ± 345
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 346
   GrossTradeAmount <GrssTradAmt> [0..1] ± 346
   DealPrice <DealPric> [1..1] ± 346
   TypeOfPrice <TpOfPric> [0..1] ± 347
   CashMargin <CshMrgn> [0..1] CodeSet 347
   Commission <Comssn> [0..1] ± 347
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C25 348
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 195 February 2025
```

## File page 196

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   GiveUpNumberOfDays <GvUpNbOfDays> [0..1] Quantity C25 348
   InterestType <IntrstTp> [0..1] CodeSet 349
   AccruedInterestPercentage <AcrdIntrstPctg> [0..1] Rate 349
   TradeRegulatoryConditionsType <TradRgltryCondsTp> [0..1] CodeSet 349
   CurrencyToBuyOrSell <CcyToBuyOrSell> [0..1] ± 349
   OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 350
   PositionEffect <PosFct> [0..1] CodeSet 350
   DerivativeCovered <DerivCvrd> [0..1] Indicator 350
   ChargeTaxBasisType <ChrgTaxBsisTp> [0..1] ± 351
   CapitalGainType <CptlGnTp> [0..1] ± 351
   MatchStatus <MtchSts> [0..1] ± 351
   CallInType <CallInTp> [0..1] CodeSet 351
   YieldType <YldTp> [0..1] ± 352
   Reporting <Rptg> [0..*] ± 352
   AdditionalPhysicalOrRegistrationDetails
<AddtlPhysOrRegnDtls>
[0..1] ± 352
   AdditionalTradeInstructionProcessingInformation
<AddtlTradInstrPrcgInf>
[0..1] Text 353
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 353
Constraints
• CurrencyToBuyOrSellRule
CurrencyToBuyOrSell in the TradeDetails message component, provides an instruction to the
account servicer to execute a foreign exchange deal on behalf of the account owner. The purpose of
the forex deal is to fund the purchase of securities. This field is not to be used when standing
instructions have been established.
If CurrencyToSell is used, then it implies the following:
- the instruction is to receive.
- the currency required for funding a purchase of securities, eg, the currency to be purchased, is the
currency of the settlement amount. The currency to be sold to obtain settlement currency is provided
by the currency to sell message element. Normally, this is the base currency of the portfolio.
- the amount of currency to be bought is equal to the settlement amount of the transaction. This
implies the forex will not be used for other transactions and that a bulk forex deal must be instructed
by other means.
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 196 February 2025
```

