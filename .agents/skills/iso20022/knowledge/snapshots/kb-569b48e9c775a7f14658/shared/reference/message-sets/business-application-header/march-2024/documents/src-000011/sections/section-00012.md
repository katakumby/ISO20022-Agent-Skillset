---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["2 head.001.001.04 BusinessApplicationHeaderV04", "2.4 Message Building Blocks", "2.4.7 MarketPractice <MktPrctc>"]
file_pages: [14]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.04"]
---

# 2.4.7 MarketPractice <MktPrctc>

Source: [src-000011](../../../../../../../../evidence/omitted/b1a725a8c57af20c03e238c2.md). Locator: one-based file pages 14 to 14.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 14

```text
"marketx.hvps.01" and "marketx.xbdr.01" might be used to indicate that the associated messages are
subject to different processing levels for domestic high value payments versus cross-border payments
within the same market practice.
Datatype: "Max35Text" on page 57
2.4.7 MarketPractice <MktPrctc>
Presence: [0..1]
Definition: Specifies the market practice to which the message conforms. The market practices are a
set of rules agreed between parties that restricts the usage of the messages in order to achieve better
STP (Straight Through Processing) rates.
A market practice specification may also extend the underlying message specification by using
extensions or supplementary data of this underlying message.
MarketPractice <MktPrctc> contains the following ImplementationSpecification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Registry <Regy> [1..1] Text 14
   Identification <Id> [1..1] Text 14
2.4.7.1  Registry <Regy>
Presence: [1..1]
Definition: Name of the implementation specification registry in which the implementation specification
of the ISO 20022 message is maintained.
For example, "MyStandards".
Datatype: "Max350Text" on page 56
2.4.7.2  Identification <Id>
Presence: [1..1]
Definition: Identifier which unambiguously identifies, within the implementation specification registry, the
implementation specification to which the ISO 20022 message is compliant. This can be done via a
URN. It can also contain a version number or date.
For instance, "2018-01-01 - Version 2" or "urn:uuid:6e8bc430-9c3a-11d9-9669-0800200c9a66".
Datatype: "Max2048Text" on page 56
2.4.8 CreationDate <CreDt>
Presence: [1..1]
Definition: Date and time when this Business Message (header) was created.
Datatype: "ISODateTime" on page 54
2.4.9 BusinessProcessingDate <BizPrcgDt>
Presence: [0..1]
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 head.001.001.04 BusinessApplicationHeaderV04
Business Application Header - Version 4 14 March 2024
```

