---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.5 GenericIdentification80", "35.1.14.5.1 Type <Tp>"]
file_pages: [1487]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.5.1 Type <Tp>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1487 to 1487.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1487

```text
35.1.14.5.1  Type <Tp>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Type <Tp> contains the following elements (see "GenericIdentification30" on page 1502 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.14.5.2  Identification <Id>
Presence: [0..1]
Definition: Name or number assigned by an entity to enable recognition of that entity.
Datatype: "Max35Text" on page 2192
35.1.14.6  AdditionalReference10
Definition: Reference and reference issuer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 1487
   ReferenceIssuer <RefIssr> [0..1] ± 1487
   MessageName <MsgNm> [0..1] Text 1488
35.1.14.6.1  Reference <Ref>
Presence: [1..1]
Definition: Reference issued by a party to identify an instruction, transaction or a message.
Datatype: "Max35Text" on page 2192
35.1.14.6.2  ReferenceIssuer <RefIssr>
Presence: [0..1]
Definition: Issuer of the reference.
ReferenceIssuer <RefIssr> contains the following elements (see "PartyIdentification139" on
page 1688 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 1689
   LEI <LEI> [0..1] IdentifierSet 1689
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1487 March 2026
```

