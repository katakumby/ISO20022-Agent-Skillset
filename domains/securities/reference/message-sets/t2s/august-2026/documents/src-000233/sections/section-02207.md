---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.18 Market", "82.1.18.1 MarketIdentification89", "82.1.18.1.2 Type <Tp>"]
file_pages: [2970]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.18.1.2 Type <Tp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2970 to 2970.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2970

```text
Identification <Id> contains one of the following elements (see "MarketIdentification1Choice" on
page 2971 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 2971
Or}   Description <Desc> [1..1] Text 2971
82.1.18.1.2  Type <Tp>
Presence: [1..1]
Definition: Nature of a market in which transactions take place.
Type <Tp> contains one of the following MarketType15Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2970
Or}   Proprietary <Prtry> [1..1] ± 2970
82.1.18.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Market type expressed as an ISO 20022 code.
Datatype: "MarketType4Code" on page 3263
CodeName Name Definition
FUND Fund The place is a fund (transfer agent, fund
itself, etc.).
LMAR LocalMarket The place is a local market.
THEO Theoretical The place is theoretical.
VEND Vendor The place is a vendor.
82.1.18.1.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Market type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.18.2  MarketClientSide6Choice
Definition: Choice of format for the market/client side information.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2970 August 2026
```

