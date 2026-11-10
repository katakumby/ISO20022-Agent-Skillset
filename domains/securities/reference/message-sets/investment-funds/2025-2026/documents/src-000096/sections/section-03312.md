---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.23 Identification Information", "66.1.23.13 MessageIdentification1", "66.1.23.13.2 CreationDateTime <CreDtTm>"]
file_pages: [4549]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.23.13.2 CreationDateTime <CreDtTm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4549 to 4549.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4549

```text
66.1.23.13.2  CreationDateTime <CreDtTm>
Presence: [1..1]
Definition: Date of creation of the message.
Datatype: "ISODateTime" on page 5388
66.1.23.14  GenericIdentification5
Definition: Information expressed in a proprietary manner.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [1..1] Text 4549
   Information <Inf> [1..1] Text 4549
   Narrative <Nrrtv> [0..1] Text 4549
66.1.23.14.1  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max8Text" on page 5404
66.1.23.14.2  Information <Inf>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Exact4AlphaNumericText" on page 5402
66.1.23.14.3  Narrative <Nrrtv>
Presence: [0..1]
Definition: Additional information.
Datatype: "Max35Text" on page 5403
66.1.23.15  GenericIdentification36
Definition: Identification using a proprietary scheme.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.23.15.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4549 May 2026
```

