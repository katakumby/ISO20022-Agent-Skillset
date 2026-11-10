---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "2.4 Message Building Blocks", "2.4.7 MarketPractice <MktPrctc>", "2.4.7.1 Registry <Regy>"]
file_pages: [15]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.02"]
---

# 2.4.7.1 Registry <Regy>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 15 to 15.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 15

```text
MarketPractice <MktPrctc> contains the following ImplementationSpecification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Registry <Regy> [1..1] Text 15
   Identification <Id> [1..1] Text 15
2.4.7.1  Registry <Regy>
Presence: [1..1]
Definition: Name of the implementation specification registry in which the implementation specification
of the ISO 20022 message is maintained.
For example, "MyStandards".
Datatype: "Max350Text" on page 1250
2.4.7.2  Identification <Id>
Presence: [1..1]
Definition: Identifier which unambiguously identifies, within the implementation specification registry, the
implementation specification to which the ISO 20022 message is compliant. This can be done via a
URN. It can also contain a version number or date.
For instance, "2018-01-01 - Version 2" or "urn:uuid:6e8bc430-9c3a-11d9-9669-0800200c9a66".
Datatype: "Max2048Text" on page 1249
2.4.8 CreationDate <CreDt>
Presence: [1..1]
Definition: Date and time when this Business Message (header) was created.
Datatype: "ISODateTime" on page 1243
2.4.9 BusinessProcessingDate <BizPrcgDt>
Presence: [0..1]
Definition: Processing date and time indicated by the sender for the receiver of the business message.
This date may be different from the date and time provided in the CreationDate.
Usage: Market practice or bilateral agreement should specify how this element should be used.
Datatype: "ISODateTime" on page 1243
2.4.10 CopyDuplicate <CpyDplct>
Presence: [0..1]
Definition: Indicates whether the message is a Copy, a Duplicate or a copy of a duplicate of a previously
sent ISO 20022 Message.
Datatype: "CopyDuplicate1Code" on page 1166
Approved by the Securities SEG on 27 January 2026 head.001.001.02 BusinessApplicationHeaderV02
Corporate Actions - Maintenance 2025 - 2026 15 February 2026
```

