---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.13 Document"]
file_pages: [269]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.13 Document

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 269 to 269.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 269

```text
7.1.13 Document
7.1.13.1  DocumentNumber17Choice
Definition: Choice between a short document number, a long document number or a proprietary
document number.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 269
Or   LongNumber <LngNb> [1..1] Text 269
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 269
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
7.1.13.1.1  ShortNumber <ShrtNb>
Presence: [1..1]
Definition: Message type number of the document referenced.
Datatype: "Exact3NumericText" on page 667
7.1.13.1.2  LongNumber <LngNb>
Presence: [1..1]
Definition: MX Message identifier of the referenced document.
Datatype: "ISO20022MessageIdentificationText" on page 667
7.1.13.1.3  ProprietaryNumber <PrtryNb>
Presence: [1..1]
Definition: Proprietary document identification.
ProprietaryNumber <PrtryNb> contains the following elements (see "GenericIdentification30" on
page 276 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 269 February 2025
```

