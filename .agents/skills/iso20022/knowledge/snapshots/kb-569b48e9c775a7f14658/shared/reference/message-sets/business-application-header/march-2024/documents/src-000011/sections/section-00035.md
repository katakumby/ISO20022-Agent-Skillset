---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["3 Message Items Types", "3.1 MessageComponents", "3.1.3 Party Identification", "3.1.3.1 PartyIdentification272", "3.1.3.1.3 Identification <Id>", "3.1.3.1.3.1 OrganisationIdentification <OrgId>", "3.1.3.1.3.1.1 AnyBIC <AnyBIC>"]
file_pages: [37]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3.1.3.1.3.1.1 AnyBIC <AnyBIC>

Source: [src-000011](../../../../../../../../evidence/omitted/b1a725a8c57af20c03e238c2.md). Locator: one-based file pages 37 to 37.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 37

```text
OrganisationIdentification <OrgId> contains the following OrganisationIdentification39 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C1 37
   LEI <LEI> [0..1] IdentifierSet 37
   Other <Othr> [0..*]  37
     Identification <Id> [1..1] Text 38
     SchemeName <SchmeNm> [0..1]  38
{Or       Code <Cd> [1..1] CodeSet 38
Or}       Proprietary <Prtry> [1..1] Text 38
     Issuer <Issr> [0..1] Text 38
3.1.3.1.3.1.1  AnyBIC <AnyBIC>
Presence: [0..1]
Definition: Business identification code of the organisation.
Impacted by: C1 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 54
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
3.1.3.1.3.1.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 55
3.1.3.1.3.1.3  Other <Othr>
Presence: [0..*]
Definition: Unique identification of an organisation, as assigned by an institution, using an identification
scheme.
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 Message Items Types
Business Application Header - Version 4 37 March 2024
```

