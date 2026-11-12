---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.9 Identification Information", "13.1.9.3 GenericIdentification36", "13.1.9.3.3 SchemeName <SchmeNm>"]
file_pages: [480]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.9.3.3 SchemeName <SchmeNm>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 480 to 480.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 480

```text
13.1.9.3.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: "Max35Text" on page 534
13.1.9.4  IdentificationSource3Choice
Definition: Choice between source of identification of a financial instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 480
Or}   Proprietary <Prtry> [1..1] Text 480
13.1.9.4.1  Code <Cd>
Presence: [1..1]
Definition: Unique and unambiguous identification source, as assigned via a pre-determined code list.
Datatype: "ExternalFinancialInstrumentIdentificationType1Code" on page 513
13.1.9.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Unique and unambiguous identification source using a proprietary identification scheme.
Datatype: "Max35Text" on page 534
13.1.9.5  GenericIdentification13
Definition: Information related to an identification, for example, party identification or account
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 480
   SchemeName <SchmeNm> [0..1] Text 480
   Issuer <Issr> [1..1] Text 481
13.1.9.5.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max4AlphaNumericText" on page 534
13.1.9.5.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 534
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 480 March 2024
```

