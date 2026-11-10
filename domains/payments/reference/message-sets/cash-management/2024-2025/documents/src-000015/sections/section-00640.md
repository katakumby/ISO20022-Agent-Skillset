---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.11 Miscellaneous", "37.1.11.7 ErrorHandling3", "37.1.11.7.1 Error <Err>", "37.1.11.7.1.1 Code <Cd>"]
file_pages: [817]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.11.7.1.1 Code <Cd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 817 to 817.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 817

```text
Error <Err> contains one of the following ErrorHandling1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 817
Or}   Proprietary <Prtry> [1..1] Text 817
37.1.11.7.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ErrorHandling1Code" on page 852
CodeName Name Definition
X020 DataNotYetAvailable Specifies the error code when the data
requested are not yet available.
X030 MessageSizeLimitExceeded Specifies the error code when the data
requested generates a message size
that exceed the processing capacity.
X050 DataNotAvailable Specifies the error code when the data
requested have not been found.
37.1.11.7.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max4AlphaNumericText" on page 890
37.1.11.7.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Datatype: "Max140Text" on page 888
37.1.11.8  MessageHeader8
Definition: Set of characteristics, such as the identification or the creation date and time, specific to the
message.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 817 February 2025
```

