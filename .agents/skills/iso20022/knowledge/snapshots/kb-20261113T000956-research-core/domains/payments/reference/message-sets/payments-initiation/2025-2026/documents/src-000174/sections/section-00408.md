---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.12 Party Identification", "6.1.12.1 PartyIdentification272", "6.1.12.1.3 Identification <Id>", "6.1.12.1.3.1 OrganisationIdentification <OrgId>", "6.1.12.1.3.1.3 Other <Othr>", "6.1.12.1.3.1.3.1 Identification <Id>"]
file_pages: [559]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.12.1.3.1.3.1 Identification <Id>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 559 to 559.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 559

```text
Other <Othr> contains the following GenericOrganisationIdentification3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 559
   SchemeName <SchmeNm> [0..1]  559
{Or     Code <Cd> [1..1] CodeSet 559
Or}     Proprietary <Prtry> [1..1] Text 559
   Issuer <Issr> [0..1] Text 559
6.1.12.1.3.1.3.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max256Text" on page 609
6.1.12.1.3.1.3.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
SchemeName <SchmeNm> contains one of the following
OrganisationIdentificationSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 559
Or}   Proprietary <Prtry> [1..1] Text 559
6.1.12.1.3.1.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalOrganisationIdentification1Code" on page 595
6.1.12.1.3.1.3.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 609
6.1.12.1.3.1.3.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 609
6.1.12.1.3.2  PrivateIdentification <PrvtId>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 559 March 2026
```

