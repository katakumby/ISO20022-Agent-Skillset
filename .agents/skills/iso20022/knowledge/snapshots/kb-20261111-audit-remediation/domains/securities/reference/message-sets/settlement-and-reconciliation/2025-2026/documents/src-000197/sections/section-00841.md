---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.3 Modification <Mod>", "32.4.2.3.2 Linkages <Lnkgs>", "32.4.2.3.2.4 LinkedQuantity <LkdQty>", "32.4.2.3.2.4.2 TurnedQuantity <TrndQty>"]
file_pages: [1259, 1260, 1261]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.3.2.4.2 TurnedQuantity <TrndQty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1259 to 1261.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1259

```text
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
32.4.2.3.2.4.2  TurnedQuantity <TrndQty>
Presence: [1..1]
Definition: Quantity of financial instruments of the linked transaction to be turned.
Impacted by: C23 "DigitalTokenUnitUsageRule"
TurnedQuantity <TrndQty> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1726 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1726
Or   FaceAmount <FaceAmt> [1..1] Amount 1726
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1726
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1727
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
32.4.2.3.3  TradeDetails <TradDtls>
Presence: [0..1]
Definition: Details of the trade.
Impacted by: C6 "AdditionalDetailsRule", C17 "CurrencyToBuyOrSellRule", C27
"InvestorCapacityRule", C33 "LateDeliveryDateRule", C55 "PlaceOfTradeRule", C80
"TradeDateGuideline", C82 "TradeDateTimeUTCRule"
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1259 March 2026
```

## File page 1260

```text
TradeDetails <TradDtls> contains the following SecuritiesTradeDetails147 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeIdentification <TradId> [0..1] Text 1262
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 1262
   CollateralTransactionIdentification <CollTxId> [0..*] Text 1262
   PlaceOfTrade <PlcOfTrad> [0..1] ± 1262
   PlaceOfClearing <PlcOfClr> [0..1] ± 1262
   TradeDate <TradDt> [0..1] ± 1263
   SettlementDate <SttlmDt> [0..1] ± 1263
   LateDeliveryDate <LateDlvryDt> [0..1] ± 1263
   DealPrice <DealPric> [0..1] ± 1263
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C38 1264
   OpeningClosing <OpngClsg> [0..1] ± 1264
   Reporting <Rptg> [0..*] ± 1264
   TradeTransactionCondition <TradTxCond> [0..*] ± 1264
   InvestorCapacity <InvstrCpcty> [0..1] ± 1265
   TradeOriginatorRole <TradOrgtrRole> [0..1] ± 1265
   TypeOfPrice <TpOfPric> [0..1] ± 1265
   CurrencyToBuyOrSell <CcyToBuyOrSell> [0..1] ± 1265
   MatchingStatus <MtchgSts> [0..1] ± 1266
   AffirmationStatus <AffirmSts> [0..1] ± 1266
   FXAdditionalDetails <FxAddtlDtls> [0..1] Text 1266
   SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 1266
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if FXAdditionalDetails and/or
SettlementInstructionProcessingAdditionalDetails are present, then they must not contain information
that can be provided in a structured field.
• CurrencyToBuyOrSellRule
CurrencyToBuy and CurrencyToSell in the TradeDetails message component, provides an
instruction to the account servicer to execute a foreign exchange deal on behalf of the account
owner. The purpose of the forex deal is to fund the purchase of securities. This field is not to be used
when standing instructions have been established.
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1260 March 2026
```

## File page 1261

```text
If CurrencyToSell is used, then it implies the following:
- the instruction is a receive.
- the currency required for funding a purchase of securities, for example, the currency to be
purchased, is the currency of the settlement amount. The currency to be sold to obtain settlement
currency is provided by the currency to sell message element. Normally, this is the base currency of
the portfolio.
- the amount of currency to be bought is equal to the settlement amount of the transaction. This
implies the forex will not be used for other transactions and that a bulk forex deal must be instructed
by other means.
- a forex deal to fund the purchase of securities should be executed in time for the currency to be
available on the settlement date of the securities transaction.
- a bilateral agreement regarding the use of this field has been established.
If CurrencyToBuy is used, then it implies the following:
- the instruction is a delivery
- the currency received as proceeds from the sale of securities, for example, the currency to be sold,
is the currency of the settlement amount. The currency to be bought is provided by the currency to
buy message element. If proceeds are repatriated, this is in the base currency of the portfolio.
- the amount of currency to be sold is equal to the settlement amount of the transaction. This implies
a bulk forex deal must be instructed by other means.
- a forex deal to repatriate proceeds after the sale of securities should be executed for the soonest
possible value date after settlement of the securities, as permitted by market convention.
- a bilateral agreement regarding the use of this field has been established.
• InvestorCapacityRule
If InvestorCapacity is used, then the use of the codes needs to be bi-laterally agreed.
• LateDeliveryDateRule
If LateDeliveryDate is used, then the transaction must be a pool trade that results from the original
TBA (To Be Announced). The original TBA would be offset by an opposite transaction and replaced
by buys or sells of individual pools. It is a date greater than the settlement date stated in the trade,
for pools designed as settling late.
• PlaceOfTradeRule
If PlaceOfTrade is used and an ISO 10383 MIC exists for the market to be identified, then the ISO
10383 Market Identifier Code (MIC) must be used.
• TradeDateGuideline
In addition to the settlement date (ISO 20022 mandatory), trade date is one of the 10 common
elements recommended by SMPG for equities and fixed income settlement instructions.
For more details, see the relevant market practice document on www.smpg.info.
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1261 March 2026
```

