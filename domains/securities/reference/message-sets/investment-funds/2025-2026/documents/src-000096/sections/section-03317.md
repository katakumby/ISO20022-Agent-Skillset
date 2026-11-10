---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.23 Identification Information", "66.1.23.22 AdditionalReference11", "66.1.23.22.1 Reference <Ref>"]
file_pages: [4554]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.23.22.1 Reference <Ref>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4554 to 4554.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4554

```text
66.1.23.22.1  Reference <Ref>
Presence: [1..1]
Definition: Reference identifying a set of messages.
Datatype: "Max35Text" on page 5403
66.1.23.22.2  ReferenceIssuer <RefIssr>
Presence: [0..1]
Definition: Issuer of the reference.
ReferenceIssuer <RefIssr> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
66.1.23.22.3  MessageName <MsgNm>
Presence: [0..1]
Definition: Name of the message.
Datatype: "Max35Text" on page 5403
66.1.23.23  GenericIdentification78
Definition: Identification expressed as a proprietary type and narrative description.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 4554
   Identification <Id> [0..1] Text 4554
66.1.23.23.1  Type <Tp>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Type <Tp> contains the following elements (see "GenericIdentification30" on page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   Issuer <Issr> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4553
66.1.23.23.2  Identification <Id>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4554 May 2026
```

