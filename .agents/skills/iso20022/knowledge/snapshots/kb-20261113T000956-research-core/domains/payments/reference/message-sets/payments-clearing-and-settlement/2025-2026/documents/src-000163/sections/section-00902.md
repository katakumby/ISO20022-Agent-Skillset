---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.12 Party Identification", "10.1.12.1 PartyIdentification272", "10.1.12.1.3 Identification <Id>", "10.1.12.1.3.1 OrganisationIdentification <OrgId>", "10.1.12.1.3.1.1 AnyBIC <AnyBIC>"]
file_pages: [1197]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.12.1.3.1.1 AnyBIC <AnyBIC>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1197 to 1197.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1197

```text
OrganisationIdentification <OrgId> contains the following OrganisationIdentification39 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 1197
   LEI <LEI> [0..1] IdentifierSet 1197
   Other <Othr> [0..*]  1197
     Identification <Id> [1..1] Text 1198
     SchemeName <SchmeNm> [0..1]  1198
{Or       Code <Cd> [1..1] CodeSet 1198
Or}       Proprietary <Prtry> [1..1] Text 1198
     Issuer <Issr> [0..1] Text 1198
10.1.12.1.3.1.1  AnyBIC <AnyBIC>
Presence: [0..1]
Definition: Business identification code of the organisation.
Impacted by: C4 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 1240
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
10.1.12.1.3.1.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 1241
10.1.12.1.3.1.3  Other <Othr>
Presence: [0..*]
Definition: Unique identification of an organisation, as assigned by an institution, using an identification
scheme.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1197 March 2026
```

