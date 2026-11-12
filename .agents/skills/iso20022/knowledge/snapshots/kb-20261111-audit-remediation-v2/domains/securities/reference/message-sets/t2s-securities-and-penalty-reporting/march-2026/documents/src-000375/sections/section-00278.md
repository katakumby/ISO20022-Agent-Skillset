---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.17 Market", "7.1.17.1 MarketIdentification89", "7.1.17.1.2 Type <Tp>"]
file_pages: [355]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.17.1.2 Type <Tp>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 355 to 355.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 355

```text
Identification <Id> contains one of the following elements (see "MarketIdentification1Choice" on
page 356 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 356
Or}   Description <Desc> [1..1] Text 356
7.1.17.1.2  Type <Tp>
Presence: [1..1]
Definition: Nature of a market in which transactions take place.
Type <Tp> contains one of the following MarketType15Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 355
Or}   Proprietary <Prtry> [1..1] ± 355
7.1.17.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Market type expressed as an ISO 20022 code.
Datatype: "MarketType4Code" on page 515
CodeName Name Definition
FUND Fund The place is a fund (transfer agent, fund
itself, etc.).
LMAR LocalMarket The place is a local market.
THEO Theoretical The place is theoretical.
VEND Vendor The place is a vendor.
7.1.17.1.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Market type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.17.2  MarketClientSide6Choice
Definition: Choice of format for the market/client side information.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 355 March 2026
```

