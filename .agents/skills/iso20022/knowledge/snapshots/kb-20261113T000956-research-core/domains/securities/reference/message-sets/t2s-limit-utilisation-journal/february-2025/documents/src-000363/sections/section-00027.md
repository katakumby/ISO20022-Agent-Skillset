---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["4 Message Items Types"]
file_pages: [29]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4 Message Items Types

Source: [src-000363](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 29 to 29.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 29

```text
4 Message Items Types
4.1 MessageComponents
4.1.1 Account
4.1.1.1  GenericAccountIdentification1
Definition: Information related to a generic account identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 29
   SchemeName <SchmeNm> [0..1]  29
{Or     Code <Cd> [1..1] CodeSet 29
Or}     Proprietary <Prtry> [1..1] Text 29
   Issuer <Issr> [0..1] Text 30
4.1.1.1.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max34Text" on page 45
4.1.1.1.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
SchemeName <SchmeNm> contains one of the following AccountSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 29
Or}   Proprietary <Prtry> [1..1] Text 29
4.1.1.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalAccountIdentification1Code" on page 42
4.1.1.1.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 46
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
Message Items Types
Target2-Securities - Limit Utilisation Journal 29 February 2025
```

