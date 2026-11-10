---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["8 Message Items Types", "8.1 MessageComponents", "8.1.1 Account", "8.1.1.3 CashAccountType2Choice", "8.1.1.3.2 Proprietary <Prtry>"]
file_pages: [58]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 8.1.1.3.2 Proprietary <Prtry>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 58 to 58.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 58

```text
Definition: Account type, in a coded form.
Datatype: "ExternalCashAccountType1Code" on page 74
8.1.1.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Nature or use of the account in a proprietary form.
Datatype: "Max35Text" on page 78
8.1.1.4  GenericAccountIdentification1
Definition: Information related to a generic account identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 58
   SchemeName <SchmeNm> [0..1]  58
{Or     Code <Cd> [1..1] CodeSet 58
Or}     Proprietary <Prtry> [1..1] Text 58
   Issuer <Issr> [0..1] Text 59
8.1.1.4.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max34Text" on page 78
8.1.1.4.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
SchemeName <SchmeNm> contains one of the following AccountSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 58
Or}   Proprietary <Prtry> [1..1] Text 58
8.1.1.4.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalAccountIdentification1Code" on page 73
8.1.1.4.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Approved by the Securities SEG on 21 November 2024. Message Items Types
Target2-Securities - Link Reference Data 58 December 2024
```

