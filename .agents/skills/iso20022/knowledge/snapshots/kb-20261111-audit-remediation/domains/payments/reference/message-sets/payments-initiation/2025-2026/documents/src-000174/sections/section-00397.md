---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.9 Identification Information", "6.1.9.1 GenericIdentification30", "6.1.9.1.3 SchemeName <SchmeNm>"]
file_pages: [548]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.9.1.3 SchemeName <SchmeNm>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 548 to 548.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 548

```text
6.1.9.1.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: "Max35Text" on page 609
6.1.9.2  GenericIdentification3
Definition: Information related to an identification, for example, party identification or account
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 548
   Issuer <Issr> [0..1] Text 548
6.1.9.2.1  Identification <Id>
Presence: [1..1]
Definition: Name or number assigned by an entity to enable recognition of that entity, for example,
account identifier.
Datatype: "Max35Text" on page 609
6.1.9.2.2  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 609
6.1.9.3  PaymentIdentification6
Definition: Provides further means of referencing a payment transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionIdentification <InstrId> [0..1] Text 548
   EndToEndIdentification <EndToEndId> [1..1] Text 549
   UETR <UETR> [0..1] IdentifierSet 549
6.1.9.3.1  InstructionIdentification <InstrId>
Presence: [0..1]
Definition: Unique identification as assigned by an instructing party for an instructed party to
unambiguously identify the instruction.
Usage: The instruction identification is a point to point reference that can be used between the
instructing party and the instructed party to refer to the individual instruction. It can be included in
several messages related to the instruction.
Datatype: "Max35Text" on page 609
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 548 March 2026
```

