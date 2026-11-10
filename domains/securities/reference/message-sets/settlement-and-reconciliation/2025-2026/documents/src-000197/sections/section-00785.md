---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.1 Addition <Addtn>", "32.4.2.1.2 Linkages <Lnkgs>", "32.4.2.1.2.4 LinkedQuantity <LkdQty>", "32.4.2.1.2.4.2 TurnedQuantity <TrndQty>"]
file_pages: [1182, 1183, 1184]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.1.2.4.2 TurnedQuantity <TrndQty>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1182 to 1184.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1182

```text
Definition: Quantity of financial instruments of the linked transaction to be paired-off.
Impacted by: C23 "DigitalTokenUnitUsageRule"
PairedOffQuantity <PairdOffQty> contains one of the following elements (see
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
32.4.2.1.2.4.2  TurnedQuantity <TrndQty>
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
32.4.2.1.3  TradeDetails <TradDtls>
Presence: [0..1]
Definition: Details of the trade.
Impacted by: C3 "AdditionalDetailsRule", C16 "CurrencyToBuyOrSellRule", C26
"InvestorCapacityRule", C32 "LateDeliveryDateRule", C54 "PlaceOfTradeRule", C79
"TradeDateGuideline", C81 "TradeDateTimeUTCRule"
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1182 March 2026
```

## File page 1183

```text
TradeDetails <TradDtls> contains the following SecuritiesTradeDetails146 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeIdentification <TradId> [0..1] Text 1185
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 1185
   CollateralTransactionIdentification <CollTxId> [0..*] Text 1185
   PlaceOfTrade <PlcOfTrad> [0..1] ± 1185
   PlaceOfClearing <PlcOfClr> [0..1] ± 1185
   TradeDate <TradDt> [0..1] ± 1186
   LateDeliveryDate <LateDlvryDt> [0..1] ± 1186
   DealPrice <DealPric> [0..1] ± 1186
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C38 1187
   OpeningClosing <OpngClsg> [0..1] ± 1187
   Reporting <Rptg> [0..*] ± 1187
   TradeTransactionCondition <TradTxCond> [0..*] ± 1187
   InvestorCapacity <InvstrCpcty> [0..1] ± 1188
   TradeOriginatorRole <TradOrgtrRole> [0..1] ± 1188
   TypeOfPrice <TpOfPric> [0..1] ± 1188
   CurrencyToBuyOrSell <CcyToBuyOrSell> [0..1] ± 1188
   MatchingStatus <MtchgSts> [0..1] ± 1189
   AffirmationStatus <AffirmSts> [0..1] ± 1189
   FXAdditionalDetails <FxAddtlDtls> [0..1] Text 1189
   SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 1189
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
If CurrencyToSell is used, then it implies the following:
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1183 March 2026
```

## File page 1184

```text
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
Settlement And Reconciliation - Maintenance 2025 - 2026 1184 March 2026
```

