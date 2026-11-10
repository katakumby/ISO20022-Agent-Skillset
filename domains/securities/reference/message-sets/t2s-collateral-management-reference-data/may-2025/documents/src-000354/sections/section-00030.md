---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["5 reda.027.001.01 CloseLinkCreationRequestV01", "5.4 Message Building Blocks", "5.4.2 CloseLink <ClsLk>", "5.4.2.2 PartyIdentification <PtyId>", "5.4.2.2.1 OrganisationIdentification <OrgId>"]
file_pages: [34]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.027.001.01"]
---

# 5.4.2.2.1 OrganisationIdentification <OrgId>

Source: [src-000354](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 34 to 34.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 34

```text
Definition: Identifies the party for which the close link is defined.
PartyIdentification <PtyId> contains one of the following SystemPartyIdentification2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 34
Or}   CombinedIdentification <CmbndId> [1..1] ± 34
5.4.2.2.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Provides the identification of a party.
OrganisationIdentification <OrgId> contains the following elements (see "PartyIdentification136" on
page 71 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 71
   LEI <LEI> [0..1] IdentifierSet 71
5.4.2.2.2  CombinedIdentification <CmbndId>
Presence: [1..1]
Definition: Identifies the party with the combined identification of both the responsible entity and the
party itself.
CombinedIdentification <CmbndId> contains the following elements (see
"SystemPartyIdentification8" on page 72 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 72
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 72
5.4.2.3  CreditProviderIdentification <CdtPrvdrId>
Presence: [0..1]
Definition: Identifies the credit provider party for which the close link information is provided.
CreditProviderIdentification <CdtPrvdrId> contains one of the following
SystemPartyIdentification2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 35
Or}   CombinedIdentification <CmbndId> [1..1] ± 35
Approved by the Securities SEG on 17 April 2025. reda.027.001.01 CloseLinkCreationRequestV01
Target2-Securities - Collateral Management Reference Data 34 May 2025
```

