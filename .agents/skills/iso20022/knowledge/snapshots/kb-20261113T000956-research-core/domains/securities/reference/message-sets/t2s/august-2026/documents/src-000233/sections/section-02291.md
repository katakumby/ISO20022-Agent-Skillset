---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.20 Party Identification", "82.1.20.8 PartyIdentification272", "82.1.20.8.3 Identification <Id>", "82.1.20.8.3.1 OrganisationIdentification <OrgId>", "82.1.20.8.3.1.3 Other <Othr>", "82.1.20.8.3.1.3.1 Identification <Id>"]
file_pages: [3072]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.20.8.3.1.3.1 Identification <Id>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3072 to 3072.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3072

```text
Other <Othr> contains the following GenericOrganisationIdentification3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 3072
   SchemeName <SchmeNm> [0..1]  3072
{Or     Code <Cd> [1..1] CodeSet 3072
Or}     Proprietary <Prtry> [1..1] Text 3072
   Issuer <Issr> [0..1] Text 3072
82.1.20.8.3.1.3.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max256Text" on page 3327
82.1.20.8.3.1.3.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
SchemeName <SchmeNm> contains one of the following
OrganisationIdentificationSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3072
Or}   Proprietary <Prtry> [1..1] Text 3072
82.1.20.8.3.1.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalOrganisationIdentification1Code" on page 3243
82.1.20.8.3.1.3.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 3328
82.1.20.8.3.1.3.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 3328
82.1.20.8.3.2  PrivateIdentification <PrvtId>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3072 August 2026
```

