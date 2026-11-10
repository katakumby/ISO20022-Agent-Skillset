---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.8 Document"]
file_pages: [399]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.8 Document

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 399 to 399.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 399

```text
17.1.8 Document
17.1.8.1  DocumentNumber5Choice
Definition: Choice between a short document number, a long document number or a proprietary
document number.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 399
Or   LongNumber <LngNb> [1..1] Text 399
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 399
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
17.1.8.1.1  ShortNumber <ShrtNb>
Presence: [1..1]
Definition: Message type number of the document referenced.
Datatype: "Exact3NumericText" on page 495
17.1.8.1.2  LongNumber <LngNb>
Presence: [1..1]
Definition: MX Message identifier of the referenced document.
Datatype: "ISO20022MessageIdentificationText" on page 496
17.1.8.1.3  ProprietaryNumber <PrtryNb>
Presence: [1..1]
Definition: Proprietary document identification.
ProprietaryNumber <PrtryNb> contains the following elements (see "GenericIdentification36" on
page 409 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 409
   Issuer <Issr> [1..1] Text 409
   SchemeName <SchmeNm> [0..1] Text 410
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
399 March 2024
```

