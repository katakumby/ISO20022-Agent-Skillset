---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["6 reda.010.001.01 SecurityQueryV01", "6.4 Message Building Blocks", "6.4.3 SearchCriteria <SchCrit>", "6.4.3.11 TechnicalIssuerCSD <TechIssrCSD>"]
file_pages: [88]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.010.001.01"]
---

# 6.4.3.11 TechnicalIssuerCSD <TechIssrCSD>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 88 to 88.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 88

```text
Definition: Entity involved in an activity.
IssuerCSD <IssrCSD> contains one of the following elements (see "SystemPartyIdentification2Choice"
on page 488 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 489
Or}   CombinedIdentification <CmbndId> [1..1] ± 489
6.4.3.11  TechnicalIssuerCSD <TechIssrCSD>
Presence: [0..1]
Definition: Technical issuer of a security.
TechnicalIssuerCSD <TechIssrCSD> contains one of the following elements (see
"SystemPartyIdentification2Choice" on page 488 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 489
Or}   CombinedIdentification <CmbndId> [1..1] ± 489
6.4.3.12  CSD <CSD>
Presence: [0..1]
Definition: CSD of a security.
CSD <CSD> contains one of the following elements (see "SystemPartyIdentification2Choice" on
page 488 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 489
Or}   CombinedIdentification <CmbndId> [1..1] ± 489
6.4.4 SmallSetReturnCriteria <SmlSetRtrCrit>
Presence: [0..1]
Definition: Defines the expected securities reference data to be returned.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.010.001.01 SecurityQueryV01
Target2-Securities - Securities Reference Data 88 March 2024
```

