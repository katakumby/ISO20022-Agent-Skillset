---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.23 Identification Information", "66.1.23.9 AdditionalReference10", "66.1.23.9.2 ReferenceIssuer <RefIssr>"]
file_pages: [4546]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.23.9.2 ReferenceIssuer <RefIssr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4546 to 4546.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4546

```text
Definition: Reference issued by a party to identify an instruction, transaction or a message.
Datatype: "Max35Text" on page 5403
66.1.23.9.2  ReferenceIssuer <RefIssr>
Presence: [0..1]
Definition: Issuer of the reference.
ReferenceIssuer <RefIssr> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
66.1.23.9.3  MessageName <MsgNm>
Presence: [0..1]
Definition: Name of the message.
Datatype: "Max35Text" on page 5403
66.1.23.10  AdditionalReference13
Definition: Reference to a related message or transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4546
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4547
66.1.23.10.1  Reference <Ref>
Presence: [1..1]
Definition: Message identification of a message. This reference was assigned by the party issuing the
message.
Datatype: "Max35Text" on page 5403
66.1.23.10.2  ReferenceIssuer <RefIssr>
Presence: [0..1]
Definition: Issuer of the reference.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4546 May 2026
```

