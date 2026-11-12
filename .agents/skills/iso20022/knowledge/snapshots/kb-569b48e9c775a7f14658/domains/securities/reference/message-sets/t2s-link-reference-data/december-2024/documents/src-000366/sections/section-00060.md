---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["8 Message Items Types", "8.1 MessageComponents", "8.1.5 Identification Information", "8.1.5.2 GenericIdentification36"]
file_pages: [64]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 8.1.5.2 GenericIdentification36

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 64 to 64.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 64

```text
Datatype: "Max35Text" on page 78
8.1.5.2  GenericIdentification36
Definition: Identification using a proprietary scheme.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 64
   Issuer <Issr> [1..1] Text 64
   SchemeName <SchmeNm> [0..1] Text 64
8.1.5.2.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Max35Text" on page 78
8.1.5.2.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 78
8.1.5.2.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: "Max35Text" on page 78
8.1.5.3  IdentificationSource3Choice
Definition: Choice between source of identification of a financial instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 64
Or}   Proprietary <Prtry> [1..1] Text 64
8.1.5.3.1  Code <Cd>
Presence: [1..1]
Definition: Unique and unambiguous identification source, as assigned via a pre-determined code list.
Datatype: "ExternalFinancialInstrumentIdentificationType1Code" on page 74
8.1.5.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Unique and unambiguous identification source using a proprietary identification scheme.
Approved by the Securities SEG on 21 November 2024. Message Items Types
Target2-Securities - Link Reference Data 64 December 2024
```

