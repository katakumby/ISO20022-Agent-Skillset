---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.20 Party Identification", "82.1.20.8 PartyIdentification272", "82.1.20.8.3 Identification <Id>", "82.1.20.8.3.1 OrganisationIdentification <OrgId>", "82.1.20.8.3.1.1 AnyBIC <AnyBIC>"]
file_pages: [3071]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.20.8.3.1.1 AnyBIC <AnyBIC>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3071 to 3071.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3071

```text
OrganisationIdentification <OrgId> contains the following OrganisationIdentification39 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C2 3071
   LEI <LEI> [0..1] IdentifierSet 3071
   Other <Othr> [0..*]  3071
     Identification <Id> [1..1] Text 3072
     SchemeName <SchmeNm> [0..1]  3072
{Or       Code <Cd> [1..1] CodeSet 3072
Or}       Proprietary <Prtry> [1..1] Text 3072
     Issuer <Issr> [0..1] Text 3072
82.1.20.8.3.1.1  AnyBIC <AnyBIC>
Presence: [0..1]
Definition: Business identification code of the organisation.
Impacted by: C2 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 3320
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
82.1.20.8.3.1.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 3322
82.1.20.8.3.1.3  Other <Othr>
Presence: [0..*]
Definition: Unique identification of an organisation, as assigned by an institution, using an identification
scheme.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3071 August 2026
```

