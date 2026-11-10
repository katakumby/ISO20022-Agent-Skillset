---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.7 Document", "16.1.7.2 DocumentNumber5Choice", "16.1.7.2.1 ShortNumber <ShrtNb>"]
file_pages: [860]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.7.2.1 ShortNumber <ShrtNb>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 860 to 860.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 860

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 860
Or   LongNumber <LngNb> [1..1] Text 860
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 860
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
16.1.7.2.1  ShortNumber <ShrtNb>
Presence: [1..1]
Definition: Message type number of the document referenced.
Datatype: "Exact3NumericText" on page 1248
16.1.7.2.2  LongNumber <LngNb>
Presence: [1..1]
Definition: MX Message identifier of the referenced document.
Datatype: "ISO20022MessageIdentificationText" on page 1248
16.1.7.2.3  ProprietaryNumber <PrtryNb>
Presence: [1..1]
Definition: Proprietary document identification.
ProprietaryNumber <PrtryNb> contains the following elements (see "GenericIdentification36" on
page 878 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 878
   Issuer <Issr> [1..1] Text 878
   SchemeName <SchmeNm> [0..1] Text 879
16.1.7.3  DocumentIdentification31
Definition: Identification of a document and type of link.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 861
   LinkageType <LkgTp> [0..1] ± C22 861
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 860 February 2026
```

