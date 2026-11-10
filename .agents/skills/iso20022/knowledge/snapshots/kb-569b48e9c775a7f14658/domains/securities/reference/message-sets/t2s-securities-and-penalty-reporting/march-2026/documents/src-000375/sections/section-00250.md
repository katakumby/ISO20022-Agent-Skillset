---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.12 Financial Instrument", "7.1.12.1 FinancialInstrumentAttributes138", "7.1.12.1.1 PlaceOfListing <PlcOfListg>"]
file_pages: [327]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.12.1.1 PlaceOfListing <PlcOfListg>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 327 to 327.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 327

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MarketOrIndicativePrice <MktOrIndctvPric> [0..1] ± 333
   ExercisePrice <ExrcPric> [0..1] ± 333
   SubscriptionPrice <SbcptPric> [0..1] ± 334
   ConversionPrice <ConvsPric> [0..1] ± 334
   StrikePrice <StrkPric> [0..1] ± 334
   MinimumNominalQuantity <MinNmnlQty> [0..1] ± 334
   ContractSize <CtrctSz> [0..1] ± 335
   UnderlyingFinancialInstrumentIdentification
<UndrlygFinInstrmId>
[0..*] ± C4, C5,
C7, C8,
C9
335
   FinancialInstrumentAttributeAdditionalDetails
<FinInstrmAttrAddtlDtls>
[0..1] Text 336
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
• PlaceOfListingRule
If PlaceOfListing is used and a ISO 10383 MIC exists for the market to be identified, the ISO 10383
Market Identifier Code (MIC) must be used.
7.1.12.1.1  PlaceOfListing <PlcOfListg>
Presence: [0..1]
Definition: Market(s) on which the security is listed.
PlaceOfListing <PlcOfListg> contains one of the following elements (see
"MarketIdentification3Choice" on page 357 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 357
Or}   Description <Desc> [1..1] Text 357
7.1.12.1.2  DayCountBasis <DayCntBsis>
Presence: [0..1]
Definition: Specifies the computation method of (accrued) interest of the security.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 327 March 2026
```

