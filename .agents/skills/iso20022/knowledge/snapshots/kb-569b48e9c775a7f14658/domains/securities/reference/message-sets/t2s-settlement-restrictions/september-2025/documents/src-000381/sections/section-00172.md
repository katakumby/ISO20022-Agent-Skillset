---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.9 Financial Instrument", "9.1.9.2 FinancialInstrumentAttributes92", "9.1.9.2.1 PlaceOfListing <PlcOfListg>"]
file_pages: [211]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.9.2.1 PlaceOfListing <PlcOfListg>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 211 to 211.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 211

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PutableIndicator <PutblInd> [0..1] Indicator 217
   MarketOrIndicativePrice <MktOrIndctvPric> [0..1] ± 217
   ExercisePrice <ExrcPric> [0..1] ± 218
   SubscriptionPrice <SbcptPric> [0..1] ± 218
   ConversionPrice <ConvsPric> [0..1] ± 218
   StrikePrice <StrkPric> [0..1] ± 218
   MinimumNominalQuantity <MinNmnlQty> [0..1] ± 219
   ContractSize <CtrctSz> [0..1] ± 219
   UnderlyingFinancialInstrumentIdentification
<UndrlygFinInstrmId>
[0..*] ± C8, C9,
C11,
C12,
C14
219
   FinancialInstrumentAttributeAdditionalDetails
<FinInstrmAttrAddtlDtls>
[0..1] Text 220
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
• PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO 10383
Market Identifier Code (MIC) must be used.
9.1.9.2.1  PlaceOfListing <PlcOfListg>
Presence: [0..1]
Definition: Market(s) on which the security is listed.
PlaceOfListing <PlcOfListg> contains one of the following elements (see
"MarketIdentification3Choice" on page 227 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 227
Or}   Description <Desc> [1..1] Text 227
9.1.9.2.2  DayCountBasis <DayCntBsis>
Presence: [0..1]
Definition: Specifies the computation method of (accrued) interest of the security.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 211 September 2025
```

