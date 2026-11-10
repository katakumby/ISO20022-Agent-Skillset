---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["8 Message Items Types", "8.1 MessageComponents", "8.1.4 Financial Instrument", "8.1.4.1 SecurityIdentification19", "8.1.4.1.2 OtherIdentification <OthrId>", "8.1.4.1.2.3 Type <Tp>"]
file_pages: [63]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 8.1.4.1.2.3 Type <Tp>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 63 to 63.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 63

```text
Datatype: "Max16Text" on page 78
8.1.4.1.2.3  Type <Tp>
Presence: [1..1]
Definition: Type of the identification.
Type <Tp> contains one of the following elements (see "IdentificationSource3Choice" on page 64 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 64
Or}   Proprietary <Prtry> [1..1] Text 64
8.1.4.1.3  Description <Desc>
Presence: [0..1]
Definition: Textual description of a security instrument.
Datatype: "Max140Text" on page 77
8.1.5 Identification Information
8.1.5.1  GenericIdentification30
Definition: Information related to an identification, for example, party identification or account
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 63
   Issuer <Issr> [1..1] Text 63
   SchemeName <SchmeNm> [0..1] Text 63
8.1.5.1.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Exact4AlphaNumericText" on page 77
8.1.5.1.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 78
8.1.5.1.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Approved by the Securities SEG on 21 November 2024. Message Items Types
Target2-Securities - Link Reference Data 63 December 2024
```

