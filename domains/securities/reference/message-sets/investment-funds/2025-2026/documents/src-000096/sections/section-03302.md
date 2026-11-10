---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.23 Identification Information", "66.1.23.3 GenericIdentification7", "66.1.23.3.1 Issuer <Issr>"]
file_pages: [4539]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.23.3.1 Issuer <Issr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4539 to 4539.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4539

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [1..1] Text 4539
   Information <Inf> [1..1] Text 4539
66.1.23.3.1  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max8Text" on page 5404
66.1.23.3.2  Information <Inf>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Max35Text" on page 5403
66.1.23.4  GenericIdentification27
Definition: Information related to an identification, eg, party identification or account identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4539
   SchemeName <SchmeNm> [0..1] Text 4539
   Issuer <Issr> [1..1] Text 4539
66.1.23.4.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max4AlphaNumericText" on page 5404
66.1.23.4.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max4AlphaNumericText" on page 5404
66.1.23.4.3  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max4AlphaNumericText" on page 5404
66.1.23.5  GenericIdentification47
Definition: Information related to an identification, for example, party identification or account
identification.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4539 May 2026
```

