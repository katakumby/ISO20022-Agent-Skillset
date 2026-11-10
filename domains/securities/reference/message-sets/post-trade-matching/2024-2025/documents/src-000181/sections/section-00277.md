---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.41 SettlementStandingInstructionDatabase4Choice", "7.1.19.41.2 Proprietary <Prtry>"]
file_pages: [335, 336, 337]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.41.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 335 to 337.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 335

```text
7.1.19.41.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement standing instruction database expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.42  ModificationCancellationAllowed4Choice
Definition: Choice of format for the modification cancellation information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 335
Or}   Proprietary <Prtry> [1..1] ± 335
7.1.19.42.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether a third party is allowed to modify or cancel the transaction.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.42.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Modification, cancellation allowed information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.43  Order23
Definition: Intention to transfer an ownership of a financial instrument.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 335 February 2025
```

## File page 336

```text
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
   GiveUpNumberOfDays <GvUpNbOfDays> [0..1] Quantity C25 348
   InterestType <IntrstTp> [0..1] CodeSet 349
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 336 February 2025
```

## File page 337

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
- a forex deal to fund the purchase of securities should be executed in time for the currency to be
available on the settlement date of the securities transaction.
- a bilateral agreement regarding the use of this field has been established.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 337 February 2025
```

