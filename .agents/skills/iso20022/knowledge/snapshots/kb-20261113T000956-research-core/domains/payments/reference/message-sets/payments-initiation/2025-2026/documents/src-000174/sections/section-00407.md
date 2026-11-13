---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.12 Party Identification", "6.1.12.1 PartyIdentification272", "6.1.12.1.3 Identification <Id>", "6.1.12.1.3.1 OrganisationIdentification <OrgId>", "6.1.12.1.3.1.1 AnyBIC <AnyBIC>"]
file_pages: [558]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.12.1.3.1.1 AnyBIC <AnyBIC>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 558 to 558.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 558

```text
OrganisationIdentification <OrgId> contains the following OrganisationIdentification39 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C3 558
   LEI <LEI> [0..1] IdentifierSet 558
   Other <Othr> [0..*]  558
     Identification <Id> [1..1] Text 559
     SchemeName <SchmeNm> [0..1]  559
{Or       Code <Cd> [1..1] CodeSet 559
Or}       Proprietary <Prtry> [1..1] Text 559
     Issuer <Issr> [0..1] Text 559
6.1.12.1.3.1.1  AnyBIC <AnyBIC>
Presence: [0..1]
Definition: Business identification code of the organisation.
Impacted by: C3 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 603
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
6.1.12.1.3.1.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 604
6.1.12.1.3.1.3  Other <Othr>
Presence: [0..*]
Definition: Unique identification of an organisation, as assigned by an institution, using an identification
scheme.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 558 March 2026
```

