---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.1 Financial Instrument", "10.1.1.1 SecurityIdentification19", "10.1.1.1.3 Description <Desc>"]
file_pages: [65]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.1.1.3 Description <Desc>

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 65 to 65.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 65

```text
Type <Tp> contains one of the following elements (see "IdentificationSource3Choice" on page 66 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 66
Or}   Proprietary <Prtry> [1..1] Text 66
10.1.1.1.3  Description <Desc>
Presence: [0..1]
Definition: Textual description of a security instrument.
Datatype: "Max140Text" on page 83
10.1.2 Identification Information
10.1.2.1  GenericIdentification1
Definition: Information related to an identification, for example party identification or account
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 65
   SchemeName <SchmeNm> [0..1] Text 65
   Issuer <Issr> [0..1] Text 65
10.1.2.1.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max35Text" on page 83
10.1.2.1.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 83
10.1.2.1.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 83
10.1.2.2  GenericIdentification36
Definition: Identification using a proprietary scheme.
Approved by the Securities SEG on 17 April 2025. Message Items Types
Target2-Securities - Collateral Management Reference Data 65 May 2025
```

