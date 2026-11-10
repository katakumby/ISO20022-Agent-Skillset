---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.18 Person Identification", "16.1.18.1 PersonIdentification13", "16.1.18.1.2 Other <Othr>", "16.1.18.1.2.2 SchemeName <SchmeNm>", "16.1.18.1.2.2.1 Code <Cd>"]
file_pages: [1055]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.18.1.2.2.1 Code <Cd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1055 to 1055.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1055

```text
16.1.18.1.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalPersonIdentification1Code" on page 1210
16.1.18.1.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 1251
16.1.18.1.2.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 1251
16.1.18.2  Contact4
Definition: Specifies the details of the contact person.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 1055
   Name <Nm> [0..1] Text 1056
   PhoneNumber <PhneNb> [0..1] Text 1056
   MobileNumber <MobNb> [0..1] Text 1056
   FaxNumber <FaxNb> [0..1] Text 1056
   EmailAddress <EmailAdr> [0..1] Text 1056
   EmailPurpose <EmailPurp> [0..1] Text 1056
   JobTitle <JobTitl> [0..1] Text 1056
   Responsibility <Rspnsblty> [0..1] Text 1057
   Department <Dept> [0..1] Text 1057
   Other <Othr> [0..*]  1057
     ChannelType <ChanlTp> [1..1] Text 1057
     Identification <Id> [0..1] Text 1057
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 1057
16.1.18.2.1  NamePrefix <NmPrfx>
Presence: [0..1]
Definition: Specifies the terms used to formally address a person.
Datatype: "NamePrefix2Code" on page 1219
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1055 February 2026
```

