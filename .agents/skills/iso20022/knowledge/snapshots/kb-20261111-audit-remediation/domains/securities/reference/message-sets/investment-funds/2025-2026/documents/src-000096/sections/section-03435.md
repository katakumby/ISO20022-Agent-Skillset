---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.3 Fund1", "66.1.25.3.1 Name <Nm>"]
file_pages: [4683]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.3.1 Name <Nm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4683 to 4683.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4683

```text
Following Must be True
    /Identification Must be present
 Or    /LegalEntityIdentifier Must be absent
• FundIdentification3Rule
If Legal Entity Identifier is not present, then Identification or Name must be present. Identification,
Name and Legal Entity Identifier may all be present.
On Condition
    /LegalEntityIdentifier is absent
Following Must be True
    /Identification Must be present
 Or    /Name Must be present
66.1.25.3.1  Name <Nm>
Presence: [0..1]
Definition: Name of the fund/sub fund.
Datatype: "Max350Text" on page 5403
66.1.25.3.2  LegalEntityIdentifier <LglNttyIdr>
Presence: [0..1]
Definition: Identification of the fund/sub fund with a Legal Entity Identifier. This is a code allocated to a
party as described in ISO 17442 "Financial Services - Legal Entity Identifier (LEI)".
Datatype: "LEIIdentifier" on page 5395
66.1.25.3.3  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the fund/sub fund, assigned under a formal or
proprietary identification scheme.
Identification <Id> contains the following OtherIdentification4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4683
   Type <Tp> [1..1] ± 4683
66.1.25.3.3.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the fund/sub fund.
Datatype: "Max35Text" on page 5403
66.1.25.3.3.2  Type <Tp>
Presence: [1..1]
Definition: Identification source.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4683 May 2026
```

