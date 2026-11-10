---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.33 DutchAuctionType <DtchAuctnTp>", "3.4.10.33.1 Code <Cd>"]
file_pages: [127]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.33.1 Code <Cd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 127 to 127.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 127

```text
DutchAuctionType <DtchAuctnTp> contains one of the following
DutchAuctionTypeFormat1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 127
Or}   Proprietary <Prtry> [1..1] ± 127
3.4.10.33.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the Dutch auction type required.
Datatype: "DutchAuctionType1Code" on page 1207
CodeName Name Definition
MDFD Modified All instructions are accepted at the same
price (issuer bid).
UNMD Unmodified All instructions are accepted at the
instructed price (offering bid).
3.4.10.33.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the Dutch auction type.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
3.4.10.34  ReverseDutchAuctionIndicator <RvsDtchAuctnInd>
Presence: [0..1]
Definition: Indicates that the Dutch Auction event is a Reverse Dutch Auction.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
3.4.10.35  NewPlaceOfIncorporation <NewPlcOfIncorprtn>
Presence: [0..1]
Definition: New company's place of incorporation.
Datatype: "Max350Text" on page 1250
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 127 February 2026
```

