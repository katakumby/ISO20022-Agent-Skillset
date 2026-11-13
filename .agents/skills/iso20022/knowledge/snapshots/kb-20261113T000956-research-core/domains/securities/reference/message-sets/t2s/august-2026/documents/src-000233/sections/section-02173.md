---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.13 Financial Instrument", "82.1.13.2 FinancialInstrumentAttributes92", "82.1.13.2.1 PlaceOfListing <PlcOfListg>"]
file_pages: [2936]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.13.2.1 PlaceOfListing <PlcOfListg>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2936 to 2936.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2936

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PutableIndicator <PutblInd> [0..1] Indicator 2942
   MarketOrIndicativePrice <MktOrIndctvPric> [0..1] ± 2942
   ExercisePrice <ExrcPric> [0..1] ± 2943
   SubscriptionPrice <SbcptPric> [0..1] ± 2943
   ConversionPrice <ConvsPric> [0..1] ± 2943
   StrikePrice <StrkPric> [0..1] ± 2943
   MinimumNominalQuantity <MinNmnlQty> [0..1] ± 2944
   ContractSize <CtrctSz> [0..1] ± 2944
   UnderlyingFinancialInstrumentIdentification
<UndrlygFinInstrmId>
[0..*] ± C3, C4,
C5, C6,
C7
2944
   FinancialInstrumentAttributeAdditionalDetails
<FinInstrmAttrAddtlDtls>
[0..1] Text 2945
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
• PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO 10383
Market Identifier Code (MIC) must be used.
82.1.13.2.1  PlaceOfListing <PlcOfListg>
Presence: [0..1]
Definition: Market(s) on which the security is listed.
PlaceOfListing <PlcOfListg> contains one of the following elements (see
"MarketIdentification3Choice" on page 2972 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 2972
Or}   Description <Desc> [1..1] Text 2972
82.1.13.2.2  DayCountBasis <DayCntBsis>
Presence: [0..1]
Definition: Specifies the computation method of (accrued) interest of the security.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2936 August 2026
```

