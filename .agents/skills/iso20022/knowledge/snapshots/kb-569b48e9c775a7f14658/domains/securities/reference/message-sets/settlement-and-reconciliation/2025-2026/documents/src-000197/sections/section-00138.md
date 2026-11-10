---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "7.4 Message Building Blocks", "7.4.6 FinancialInstrument <FinInstrm>", "7.4.6.3 SubBalance <SubBal>"]
file_pages: [190]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.016.001.10"]
---

# 7.4.6.3 SubBalance <SubBal>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 190 to 190.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 190

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CallableIndicator <CllblInd> [0..1] Indicator 1469
   PutableIndicator <PutblInd> [0..1] Indicator 1469
   MarketOrIndicativePrice <MktOrIndctvPric> [0..1] ± 1469
   ExercisePrice <ExrcPric> [0..1] ± 1470
   SubscriptionPrice <SbcptPric> [0..1] ± 1470
   ConversionPrice <ConvsPric> [0..1] ± 1470
   StrikePrice <StrkPric> [0..1] ± 1470
   MinimumNominalQuantity <MinNmnlQty> [0..1] ± C12 1471
   ContractSize <CtrctSz> [0..1] ± C12 1471
   UnderlyingFinancialInstrumentIdentification
<UndrlygFinInstrmId>
[0..*] ± C10,
C11,
C14,
C15,
C16
1471
   FinancialInstrumentAttributeAdditionalDetails
<FinInstrmAttrAddtlDtls>
[0..1] Text 1472
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
• PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO 10383
Market Identifier Code (MIC) must be used.
7.4.6.3  SubBalance <SubBal>
Presence: [1..*]
Definition: Identification of the sub-balance.
Impacted by: C6 "BalanceFromToRule2"
Approved by the Securities SEG on 27 January 2026 semt.016.001.10
IntraPositionMovementPostingReportV10
Settlement And Reconciliation - Maintenance 2025 - 2026 190 March 2026
```

