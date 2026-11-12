---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "10.4 Message Building Blocks", "10.4.6 AllegementDetails <AllgmtDtls>", "10.4.6.22 TradeTransactionCondition <TradTxCond>"]
file_pages: [388]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.019.001.12"]
---

# 10.4.6.22 TradeTransactionCondition <TradTxCond>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 388 to 388.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 388

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PutableIndicator <PutblInd> [0..1] Indicator 1453
   MarketOrIndicativePrice <MktOrIndctvPric> [0..1] ± 1453
   ExercisePrice <ExrcPric> [0..1] ± 1453
   SubscriptionPrice <SbcptPric> [0..1] ± 1454
   ConversionPrice <ConvsPric> [0..1] ± 1454
   StrikePrice <StrkPric> [0..1] ± 1454
   MinimumNominalQuantity <MinNmnlQty> [0..1] ± C12 1454
   ContractSize <CtrctSz> [0..1] ± C12 1455
   UnderlyingFinancialInstrumentIdentification
<UndrlygFinInstrmId>
[0..*] ± C10,
C11,
C14,
C15,
C16
1455
   FinancialInstrumentAttributeAdditionalDetails
<FinInstrmAttrAddtlDtls>
[0..1] Text 1456
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
• PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO 10383
Market Identifier Code (MIC) must be used.
10.4.6.22  TradeTransactionCondition <TradTxCond>
Presence: [0..*]
Definition: Indicates the conditions under which the order/trade is to be/was executed.
TradeTransactionCondition <TradTxCond> contains one of the following elements (see
"TradeTransactionCondition5Choice" on page 2032 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2032
Or}   Proprietary <Prtry> [1..1] ± 2033
10.4.6.23  TypeOfPrice <TpOfPric>
Presence: [0..1]
Definition: Specifies the type of price and information about the price.
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 388 March 2026
```

