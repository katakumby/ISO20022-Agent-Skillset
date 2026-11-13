---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.18 System Identification", "37.1.18.2 ClearingSystemIdentification2Choice"]
file_pages: [847]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.18.2 ClearingSystemIdentification2Choice

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 847 to 847.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 847

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
37.1.18.2  ClearingSystemIdentification2Choice
Definition: Choice of a clearing system identifier.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 847
Or}   Proprietary <Prtry> [1..1] Text 847
37.1.18.2.1  Code <Cd>
Presence: [1..1]
Definition: Identification of a clearing system, in a coded form as published in an external list.
Datatype: "ExternalClearingSystemIdentification1Code" on page 853
37.1.18.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Identification code for a clearing system, that has not yet been identified in the list of clearing
systems.
Datatype: "Max35Text" on page 889
37.2 Message Datatypes
37.2.1 Amount
37.2.1.1  ActiveCurrencyAndAmount
Definition: A number of monetary units specified in an active currency where the unit of currency is
explicit and compliant with ISO 4217.
Type: Amount
This data type contains the following XML attribute:
Name Attribute XML Name Datatype
Currency Ccy "ActiveCurrencyCode" on page 849
Format
minInclusive 0
totalDigits 18
fractionDigits 5
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 847 February 2025
```

