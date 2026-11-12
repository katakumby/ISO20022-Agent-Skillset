---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["4 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01", "4.4 Message Building Blocks", "4.4.2 EligibleCounterpartCSD <ElgblCntrptCSD>", "4.4.2.1 IssuerIdentification <IssrId>"]
file_pages: [25]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.026.001.01"]
---

# 4.4.2.1 IssuerIdentification <IssrId>

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 25 to 25.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 25

```text
4.4.2.1  IssuerIdentification <IssrId>
Presence: [1..1]
Definition: Unique business identifier code used to identify the party providing the eligible counterpart
information.
IssuerIdentification <IssrId> contains one of the following SystemPartyIdentification2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 25
Or}   CombinedIdentification <CmbndId> [1..1] ± 25
4.4.2.1.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Provides the identification of a party.
OrganisationIdentification <OrgId> contains the following elements (see "PartyIdentification136" on
page 71 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 71
   LEI <LEI> [0..1] IdentifierSet 71
4.4.2.1.2  CombinedIdentification <CmbndId>
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
4.4.2.2  EligibleCounterpartIdentification <ElgblCntrptId>
Presence: [1..1]
Definition: Unique business identifier code used to identify the central securities depository to be
defined as eligible.
Approved by the Securities SEG on 17 April 2025. reda.026.001.01
EligibleCounterpartCSDCreationRequestV01
Target2-Securities - Collateral Management Reference Data 25 May 2025
```

