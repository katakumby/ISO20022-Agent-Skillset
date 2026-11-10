---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.2 NumberCount <NbCnt>"]
file_pages: [46, 47, 48]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.2 NumberCount <NbCnt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 46 to 48.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 46

```text
Definition: Unambiguous identification of the transaction as known by the instructing party.
Datatype: "Max35Text" on page 669
3.4.2 NumberCount <NbCnt>
Presence: [0..1]
Definition: Count of the number of transactions linked.
Impacted by: C16 "CurrentInstructionNumberRule"
NumberCount <NbCnt> contains one of the following elements (see "NumberCount1Choice" on
page 376 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrentInstructionNumber <CurInstrNb> [1..1] Text 376
Or}   TotalNumber <TtlNb> [1..1]  C17,
C10
377
     CurrentInstructionNumber <CurInstrNb> [1..1] Text 377
     TotalOfLinkedInstructions <TtlOfLkdInstrs> [1..1] Text 377
Constraints
• CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement instruction,
then the CurrentInstructionNumber must be specified.
3.4.3 References <Refs>
Presence: [0..*]
Definition: Reference to the transaction identifier issued by a business party and/or market
infrastructure. It may also be used to reference a previous transaction, for example, a block/allocation
instruction, or tie a set of messages together.
References <Refs> contains the following elements (see "Linkages76" on page 285 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageNumber <MsgNb> [0..1] ± C9 285
   Reference <Ref> [1..1] ± C7 286
3.4.4 TradeDetails <TradDtls>
Presence: [1..1]
Definition: Details of the trade.
Impacted by: C15 "CurrencyToBuyOrSellRule", C41 "PlaceOfTradeRule", C50
"TradeDateTimeUTCRule"
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 46 February 2025
```

## File page 47

```text
TradeDetails <TradDtls> contains the following Order24 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BusinessProcessType <BizPrcTp> [0..1] ± 49
   OrderIdentification <OrdrId> [0..*] Text 49
   ClientOrderIdentification <ClntOrdrId> [0..*] Text 49
   SecondaryClientOrderIdentification
<ScndryClntOrdrId>
[0..*] Text 50
   ListIdentification <ListId> [0..*] Text 50
   Side <Sd> [1..1] CodeSet 50
   Payment <Pmt> [0..1] CodeSet 51
   TradeTransactionType <TradTxTp> [0..1] ± 52
   TradeTransactionCondition <TradTxCond> [0..*] ± 52
   PreAdvice <PreAdvc> [0..1] Indicator 52
   PlaceOfTrade <PlcOfTrad> [0..1] ± C23,
C31,
C42
52
   OrderBookingDate <OrdrBookgDt> [0..1] Date 53
   TradeOriginationDate <TradOrgtnDt> [0..1] DateTime 53
   TradeDate <TradDt> [1..1] ± 53
   ProcessingDate <PrcgDt> [0..1] ± 54
   SettlementDate <SttlmDt> [1..1] ± 54
   NAVDate <NAVDt> [0..1] ± 54
   PartialFillDetails <PrtlFillDtls> [0..*] ± C35 55
   ConfirmationQuantity <ConfQty> [1..1] ± 55
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 56
   GrossTradeAmount <GrssTradAmt> [0..1] ± 56
   DealPrice <DealPric> [1..1] ± 56
   TypeOfPrice <TpOfPric> [0..1] ± 57
   CashMargin <CshMrgn> [0..1] CodeSet 57
   Commission <Comssn> [0..1] ± 57
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C33 58
   GiveUpNumberOfDays <GvUpNbOfDays> [0..1] Quantity C33 58
   InterestType <IntrstTp> [0..1] CodeSet 58
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 59
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 47 February 2025
```

## File page 48

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccruedInterestPercentage <AcrdIntrstPctg> [0..1] Rate 59
   TradeRegulatoryConditionsType
<TradRgltryCondsTp>
[0..1] CodeSet 59
   CurrencyToBuyOrSell <CcyToBuyOrSell> [0..1] ± 59
   OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 60
   PositionEffect <PosFct> [0..1] CodeSet 60
   DerivativeCovered <DerivCvrd> [0..1] Indicator 60
   ChargeTaxBasisType <ChrgTaxBsisTp> [0..1] ± 61
   CapitalGainType <CptlGnTp> [0..1] ± 61
   MatchStatus <MtchSts> [0..1] ± 61
   CallInType <CallInTp> [0..1] CodeSet 61
   YieldType <YldTp> [0..1] ± 62
   Reporting <Rptg> [0..*] ± 62
   AdditionalPhysicalOrRegistrationDetails
<AddtlPhysOrRegnDtls>
[0..1] ± 62
   AdditionalTradeInstructionProcessingInformation
<AddtlTradInstrPrcgInf>
[0..1] Text 63
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
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 48 February 2025
```

