---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.11 Financial Instrument", "35.1.11.4 FinancialInstrumentAttributes112", "35.1.11.4.1 PlaceOfListing <PlcOfListg>"]
file_pages: [1463]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.11.4.1 PlaceOfListing <PlcOfListg>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1463 to 1463.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1463

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
35.1.11.4.1  PlaceOfListing <PlcOfListg>
Presence: [0..1]
Definition: Market(s) on which the security is listed.
PlaceOfListing <PlcOfListg> contains one of the following elements (see
"MarketIdentification3Choice" on page 1526 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 1526
Or}   Description <Desc> [1..1] Text 1526
35.1.11.4.2  DayCountBasis <DayCntBsis>
Presence: [0..1]
Definition: Specifies the computation method of (accrued) interest of the security.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1463 March 2026
```

