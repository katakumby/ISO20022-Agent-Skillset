---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.8 Document"]
file_pages: [206]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.8 Document

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 206 to 206.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 206

```text
9.1.8 Document
9.1.8.1  DocumentNumber5Choice
Definition: Choice between a short document number, a long document number or a proprietary
document number.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 206
Or   LongNumber <LngNb> [1..1] Text 206
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 206
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
9.1.8.1.1  ShortNumber <ShrtNb>
Presence: [1..1]
Definition: Message type number of the document referenced.
Datatype: "Exact3NumericText" on page 343
9.1.8.1.2  LongNumber <LngNb>
Presence: [1..1]
Definition: MX Message identifier of the referenced document.
Datatype: "ISO20022MessageIdentificationText" on page 344
9.1.8.1.3  ProprietaryNumber <PrtryNb>
Presence: [1..1]
Definition: Proprietary document identification.
ProprietaryNumber <PrtryNb> contains the following elements (see "GenericIdentification36" on
page 224 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 225
   Issuer <Issr> [1..1] Text 225
   SchemeName <SchmeNm> [0..1] Text 225
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 206 September 2025
```

