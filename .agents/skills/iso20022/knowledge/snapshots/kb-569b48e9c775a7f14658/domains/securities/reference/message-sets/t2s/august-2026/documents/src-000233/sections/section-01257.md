---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["31 reda.010.001.01 SecurityQueryV01", "31.4 Message Building Blocks", "31.4.3 SearchCriteria <SchCrit>", "31.4.3.8 MaintainingCSD <MntngCSD>", "31.4.3.8.1 OrganisationIdentification <OrgId>"]
file_pages: [1775]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.010.001.01"]
---

# 31.4.3.8.1 OrganisationIdentification <OrgId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1775 to 1775.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1775

```text
MaintainingCSD <MntngCSD> contains one of the following SystemPartyIdentification2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 1775
Or}   CombinedIdentification <CmbndId> [1..1] ± 1775
31.4.3.8.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Provides the identification of a party.
OrganisationIdentification <OrgId> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
31.4.3.8.2  CombinedIdentification <CmbndId>
Presence: [1..1]
Definition: Identifies the party with the combined identification of both the responsible entity and the
party itself.
CombinedIdentification <CmbndId> contains the following elements (see
"SystemPartyIdentification8" on page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
31.4.3.9  InvestorCSD <InvstrCSD>
Presence: [0..1]
Definition: Entity involved in an activity.
InvestorCSD <InvstrCSD> contains one of the following SystemPartyIdentification2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 1775
Or}   CombinedIdentification <CmbndId> [1..1] ± 1776
31.4.3.9.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.010.001.01 SecurityQueryV01
Target2-Securities 1775 August 2026
```

