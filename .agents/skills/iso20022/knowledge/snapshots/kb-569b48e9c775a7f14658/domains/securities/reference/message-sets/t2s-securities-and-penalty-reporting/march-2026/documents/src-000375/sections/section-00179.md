---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.1 Account", "7.1.1.2 GenericAccountIdentification1", "7.1.1.2.1 Identification <Id>"]
file_pages: [247]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.1.2.1 Identification <Id>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 247 to 247.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 247

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 247
   SchemeName <SchmeNm> [0..1]  247
{Or     Code <Cd> [1..1] CodeSet 247
Or}     Proprietary <Prtry> [1..1] Text 247
   Issuer <Issr> [0..1] Text 247
7.1.1.2.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max34Text" on page 557
7.1.1.2.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
SchemeName <SchmeNm> contains one of the following AccountSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 247
Or}   Proprietary <Prtry> [1..1] Text 247
7.1.1.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalAccountIdentification1Code" on page 505
7.1.1.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 557
7.1.1.2.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 557
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 247 March 2026
```

