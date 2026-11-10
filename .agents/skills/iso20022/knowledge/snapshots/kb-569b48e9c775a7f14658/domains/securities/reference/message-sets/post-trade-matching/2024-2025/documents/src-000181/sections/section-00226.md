---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.17 Identification Information", "7.1.17.7 IdentificationSource3Choice", "7.1.17.7.2 Proprietary <Prtry>"]
file_pages: [280]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.17.7.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 280 to 280.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 280

```text
Definition: Unique and unambiguous identification source, as assigned via a pre-determined code list.
Datatype: "ExternalFinancialInstrumentIdentificationType1Code" on page 627
7.1.17.7.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Unique and unambiguous identification source using a proprietary identification scheme.
Datatype: "Max35Text" on page 669
7.1.17.8  GenericIdentification37
Definition: Identification expressed as a proprietary type and narrative description.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 280
   Issuer <Issr> [0..1] Text 280
7.1.17.8.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Max35Text" on page 669
7.1.17.8.2  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 669
7.1.17.9  GenericIdentification1
Definition: Information related to an identification, for example party identification or account
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 280
   SchemeName <SchmeNm> [0..1] Text 280
   Issuer <Issr> [0..1] Text 281
7.1.17.9.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max35Text" on page 669
7.1.17.9.2  SchemeName <SchmeNm>
Presence: [0..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 280 February 2025
```

