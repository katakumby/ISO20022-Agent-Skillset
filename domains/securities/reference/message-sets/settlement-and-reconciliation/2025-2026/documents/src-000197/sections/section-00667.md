---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks", "29.4.3 TradeDetails <TradDtls>"]
file_pages: [1010]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4.3 TradeDetails <TradDtls>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1010 to 1010.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1010

```text
For more details, see the relevant market practice document on www.smpg.info.
29.4.3 TradeDetails <TradDtls>
Presence: [1..1]
Definition: Details of the securities financing deal.
Impacted by: C3 "AdditionalDetailsRule", C15 "CurrencyToBuyOrSellRule", C23
"InvestorCapacityRule", C36 "PlaceOfTradeRule", C55 "TradeDateTimeUTCRule"
TradeDetails <TradDtls> contains the following SecuritiesTradeDetails115 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceOfTrade <PlcOfTrad> [0..1] ± 1011
   PlaceOfClearing <PlcOfClr> [0..1] ± 1012
   TradeDate <TradDt> [0..1] ± 1012
   SettlementDate <SttlmDt> [0..1] ± 1012
   EffectiveSettlementDate <FctvSttlmDt> [1..1] ± 1012
   DealPrice <DealPric> [0..1] ± 1013
   Reporting <Rptg> [0..*] ± 1013
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C28 1013
   TradeTransactionCondition <TradTxCond> [0..*] ± 1014
   InvestorCapacity <InvstrCpcty> [0..1] ± 1014
   TradeOriginatorRole <TradOrgtrRole> [0..1] ± 1014
   SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 1014
   FXAdditionalDetails <FxAddtlDtls> [0..1] Text 1015
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
- the instruction is a receive.
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1010 March 2026
```

