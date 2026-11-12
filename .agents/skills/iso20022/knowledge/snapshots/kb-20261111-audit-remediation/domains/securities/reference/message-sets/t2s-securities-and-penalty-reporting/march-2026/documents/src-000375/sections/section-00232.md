---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.15 AggregateBalancePerSafekeepingPlace44", "7.1.5.15.2 PlaceOfListing <PlcOfListg>"]
file_pages: [308]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.15.2 PlaceOfListing <PlcOfListg>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 308 to 308.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 308

```text
SafekeepingPlace <SfkpgPlc> contains the following elements (see "SafeKeepingPlace3" on
page 453 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceFormat <SfkpgPlcFrmt> [0..1] ± 453
   LEI <LEI> [0..1] IdentifierSet 453
Constraints
• SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
Following Must be True
    /SafekeepingPlaceFormat Must be present
 Or    /LEI Must be present
7.1.5.15.2  PlaceOfListing <PlcOfListg>
Presence: [0..1]
Definition: Market(s) on which the security is listed.
PlaceOfListing <PlcOfListg> contains one of the following elements (see
"MarketIdentification3Choice" on page 357 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 357
Or}   Description <Desc> [1..1] Text 357
7.1.5.15.3  Pledgee <Pldgee>
Presence: [0..1]
Definition: Specify the entity to which the financial instruments are pledged.
Impacted by: C29 "PledgeeTypeAndIdentificationOrLEIRule"
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 308 March 2026
```

