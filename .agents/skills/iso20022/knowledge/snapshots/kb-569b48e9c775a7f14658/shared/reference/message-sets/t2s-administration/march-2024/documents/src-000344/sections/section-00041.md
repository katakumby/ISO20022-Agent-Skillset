---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 Message Items Types", "5.1 MessageComponents", "5.1.6 Identification Information", "5.1.6.1 GenericIdentification1", "5.1.6.1.1 Identification <Id>"]
file_pages: [48]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 5.1.6.1.1 Identification <Id>

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 48 to 48.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 48

```text
5.1.6.1.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max35Text" on page 69
5.1.6.1.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 69
5.1.6.1.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 69
5.1.6.2  GenericIdentification30
Definition: Information related to an identification, for example, party identification or account
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 48
   Issuer <Issr> [1..1] Text 48
   SchemeName <SchmeNm> [0..1] Text 48
5.1.6.2.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Exact4AlphaNumericText" on page 68
5.1.6.2.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 69
5.1.6.2.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: "Max35Text" on page 69
5.1.6.3  GenericIdentification36
Definition: Identification using a proprietary scheme.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Administration - Maintenance 2023 -
2024
48 March 2024
```

