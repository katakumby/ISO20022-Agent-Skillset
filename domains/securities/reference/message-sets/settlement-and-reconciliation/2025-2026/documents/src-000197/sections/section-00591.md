---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["27 sese.033.001.13 SecuritiesFinancingInstructionV13", "27.4 Message Building Blocks", "27.4.4 Linkages <Lnkgs>", "27.4.4.4 LinkedQuantity <LkdQty>", "27.4.4.4.2 TurnedQuantity <TrndQty>"]
file_pages: [899, 900]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.033.001.13"]
---

# 27.4.4.4.2 TurnedQuantity <TrndQty>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 899 to 900.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 899

```text
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
27.4.4.4.2  TurnedQuantity <TrndQty>
Presence: [1..1]
Definition: Quantity of financial instruments of the linked transaction to be turned.
Impacted by: C26 "DigitalTokenUnitUsageRule"
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
27.4.4.5  ReferenceOwner <RefOwnr>
Presence: [0..1]
Definition: Party that generates the reference.
ReferenceOwner <RefOwnr> contains one of the following elements (see
"PartyIdentification127Choice" on page 1664 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1664
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 1665
27.4.5 TradeDetails <TradDtls>
Presence: [1..1]
Definition: Details of the securities financing deal.
Impacted by: C3 "AdditionalDetailsRule", C17 "CurrencyToBuyOrSellRule", C30
"InvestorCapacityRule", C43 "PlaceOfTradeRule", C68 "TradeDateTimeUTCRule"
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 899 March 2026
```

## File page 900

```text
TradeDetails <TradDtls> contains the following SecuritiesTradeDetails116 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceOfTrade <PlcOfTrad> [0..1] ± 901
   PlaceOfClearing <PlcOfClr> [0..1] ± 901
   TradeDate <TradDt> [0..1] ± 902
   OpeningSettlementDate <OpngSttlmDt> [1..1] ± 902
   DealPrice <DealPric> [0..1] ± 902
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C36 903
   Reporting <Rptg> [0..*] ± 903
   TradeTransactionCondition <TradTxCond> [0..*] ± 903
   InvestorCapacity <InvstrCpcty> [0..1] ± 904
   TradeOriginatorRole <TradOrgtrRole> [0..1] ± 904
   CurrencyToBuyOrSell <CcyToBuyOrSell> [0..1] ± 904
   AffirmationStatus <AffirmSts> [0..1] ± 904
   MatchingStatus <MtchgSts> [0..1] ± 905
   SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 905
   FXAdditionalDetails <FxAddtlDtls> [0..1] Text 905
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if FXAdditionalDetails and/or
SettlementInstructionProcessingAdditionalDetails are present, then they must not contain information
that can be provided in a structured element.
• CurrencyToBuyOrSellRule
CurrencyToBuy and CurrencyToSell in the TradeDetails message component, provides an
instruction to the account servicer to execute a foreign exchange deal on behalf of the account
owner. The purpose of the forex deal is to fund the purchase of securities. This field is not to be used
when standing instructions have been established.
If CurrencyToSell is used, then it implies the following:
- the instruction is a receive.
- the currency required for funding a purchase of securities, for example, the currency to be
purchased, is the currency of the settlement amount. The currency to be sold to obtain settlement
currency is provided by the currency to sell message element. Normally, this is the base currency of
the portfolio.
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 900 March 2026
```

