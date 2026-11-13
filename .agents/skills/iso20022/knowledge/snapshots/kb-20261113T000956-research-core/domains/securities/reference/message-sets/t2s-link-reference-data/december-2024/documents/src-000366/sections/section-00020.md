---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01", "3.4 Message Building Blocks", "3.4.2 SecurityCSDLinkIdentification <SctyCSDLkId>", "3.4.2.2 IssuerInvestorCSD <IssrInvstrCSD>", "3.4.2.2.1 IssuerCSD <IssrCSD>", "3.4.2.2.1.1 OrganisationIdentification <OrgId>"]
file_pages: [22]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.046.001.01"]
---

# 3.4.2.2.1.1 OrganisationIdentification <OrgId>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 22 to 22.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 22

```text
IssuerCSD <IssrCSD> contains one of the following SystemPartyIdentification2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 22
Or}   CombinedIdentification <CmbndId> [1..1] ± 22
3.4.2.2.1.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Provides the identification of a party.
OrganisationIdentification <OrgId> contains the following elements (see "PartyIdentification136" on
page 68 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 69
   LEI <LEI> [0..1] IdentifierSet 69
3.4.2.2.1.2  CombinedIdentification <CmbndId>
Presence: [1..1]
Definition: Identifies the party with the combined identification of both the responsible entity and the
party itself.
CombinedIdentification <CmbndId> contains the following elements (see
"SystemPartyIdentification8" on page 69 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 69
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 69
3.4.2.2.2  InvestorCSD <InvstrCSD>
Presence: [1..1]
Definition: CSD Investor of a security.
InvestorCSD <InvstrCSD> contains one of the following SystemPartyIdentification2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 22
Or}   CombinedIdentification <CmbndId> [1..1] ± 23
3.4.2.2.2.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Provides the identification of a party.
Approved by the Securities SEG on 21 November 2024. reda.046.001.01
SecurityCSDLinkMaintenanceRequestV01
Target2-Securities - Link Reference Data 22 December 2024
```

