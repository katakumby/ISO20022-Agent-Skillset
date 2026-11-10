---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.16 Organisation Identification"]
file_pages: [1032]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.16 Organisation Identification

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1032 to 1032.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1032

```text
16.1.16 Organisation Identification
16.1.16.1  OrganisationIdentification29
Definition: Unique and unambiguous way to identify an organisation.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C1 1032
   LEI <LEI> [0..1] IdentifierSet 1032
   Other <Othr> [0..*]  1032
     Identification <Id> [1..1] Text 1033
     SchemeName <SchmeNm> [0..1]  1033
{Or       Code <Cd> [1..1] CodeSet 1033
Or}       Proprietary <Prtry> [1..1] Text 1033
     Issuer <Issr> [0..1] Text 1033
16.1.16.1.1  AnyBIC <AnyBIC>
Presence: [0..1]
Definition: Business identification code of the organisation.
Impacted by: C1 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 1244
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
16.1.16.1.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 1246
16.1.16.1.3  Other <Othr>
Presence: [0..*]
Definition: Unique identification of an organisation, as assigned by an institution, using an identification
scheme.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1032 February 2026
```

