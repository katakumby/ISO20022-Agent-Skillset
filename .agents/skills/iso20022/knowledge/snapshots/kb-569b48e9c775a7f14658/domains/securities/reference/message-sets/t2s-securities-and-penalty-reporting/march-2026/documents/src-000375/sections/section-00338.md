---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Party Identification", "7.1.19.8 PartyIdentification272", "7.1.19.8.3 Identification <Id>", "7.1.19.8.3.1 OrganisationIdentification <OrgId>", "7.1.19.8.3.1.1 AnyBIC <AnyBIC>"]
file_pages: [425]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.8.3.1.1 AnyBIC <AnyBIC>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 425 to 425.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 425

```text
OrganisationIdentification <OrgId> contains the following OrganisationIdentification39 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C2 425
   LEI <LEI> [0..1] IdentifierSet 425
   Other <Othr> [0..*]  425
     Identification <Id> [1..1] Text 426
     SchemeName <SchmeNm> [0..1]  426
{Or       Code <Cd> [1..1] CodeSet 426
Or}       Proprietary <Prtry> [1..1] Text 426
     Issuer <Issr> [0..1] Text 426
7.1.19.8.3.1.1  AnyBIC <AnyBIC>
Presence: [0..1]
Definition: Business identification code of the organisation.
Impacted by: C2 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 551
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
7.1.19.8.3.1.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 552
7.1.19.8.3.1.3  Other <Othr>
Presence: [0..*]
Definition: Unique identification of an organisation, as assigned by an institution, using an identification
scheme.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 425 March 2026
```

