---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.12 Party Identification", "37.1.12.1 PartyIdentification272", "37.1.12.1.3 Identification <Id>", "37.1.12.1.3.1 OrganisationIdentification <OrgId>", "37.1.12.1.3.1.3 Other <Othr>", "37.1.12.1.3.1.3.1 Identification <Id>"]
file_pages: [828]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.12.1.3.1.3.1 Identification <Id>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 828 to 828.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 828

```text
Other <Othr> contains the following GenericOrganisationIdentification3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 828
   SchemeName <SchmeNm> [0..1]  828
{Or     Code <Cd> [1..1] CodeSet 828
Or}     Proprietary <Prtry> [1..1] Text 828
   Issuer <Issr> [0..1] Text 828
37.1.12.1.3.1.3.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max256Text" on page 889
37.1.12.1.3.1.3.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
SchemeName <SchmeNm> contains one of the following
OrganisationIdentificationSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 828
Or}   Proprietary <Prtry> [1..1] Text 828
37.1.12.1.3.1.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalOrganisationIdentification1Code" on page 854
37.1.12.1.3.1.3.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 889
37.1.12.1.3.1.3.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 889
37.1.12.1.3.2  PrivateIdentification <PrvtId>
Presence: [1..1]
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 828 February 2025
```

