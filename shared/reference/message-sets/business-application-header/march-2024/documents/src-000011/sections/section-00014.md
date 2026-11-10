---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["2 head.001.001.04 BusinessApplicationHeaderV04", "2.4 Message Building Blocks", "2.4.12 Priority <Prty>"]
file_pages: [16]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.04"]
---

# 2.4.12 Priority <Prty>

Source: [src-000011](../../../../../../../../raw-input/business_application_header/ISO20022_MDR_bahV4_v1.pdf). Locator: one-based file pages 16 to 16.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 16

```text
2.4.12 Priority <Prty>
Presence: [0..1]
Definition: Relative indication of the processing precedence of the message over a (set of) Business
Messages with assigned priorities.
Impacted by: C7 "ValidationByTable"
Datatype: "BusinessMessagePriorityCode" on page 50
Constraints
• ValidationByTable
2.4.13 Signature <Sgntr>
Presence: [0..1]
Definition: Contains the digital signature of the Business Entity authorised to sign this Business
Message.
Type: (External Schema)
The W3C XML Schema that specifies following standard signature:
XML Signature Syntax and Processing (Second Edition) W3C Recommendation 10 June 2008
http://www.w3.org/TR/2008/REC-xmldsig-core-20080610/.
2.4.14 Related <Rltd>
Presence: [0..*]
Definition: Specifies the Business Application Header(s) of the Business Message(s) to which this
Business Message relates.
Can be used when replying to a query; can also be used when canceling or amending.
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 head.001.001.04 BusinessApplicationHeaderV04
Business Application Header - Version 4 16 March 2024
```

