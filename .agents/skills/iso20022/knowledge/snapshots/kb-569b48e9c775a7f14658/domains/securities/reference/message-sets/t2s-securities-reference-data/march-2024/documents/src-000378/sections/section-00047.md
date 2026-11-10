---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["6 reda.010.001.01 SecurityQueryV01", "6.4 Message Building Blocks", "6.4.3 SearchCriteria <SchCrit>", "6.4.3.7 SecurityStatus <SctySts>", "6.4.3.7.2 Proprietary <Prtry>"]
file_pages: [87]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.010.001.01"]
---

# 6.4.3.7.2 Proprietary <Prtry>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 87 to 87.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 87

```text
Datatype: "SecurityStatus2Code" on page 523
CodeName Name Definition
ACTV Active The status is active.
INAC Inactive The status is inactive.
SUSP Suspended The status is suspended.
6.4.3.7.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Security status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
6.4.3.8  MaintainingCSD <MntngCSD>
Presence: [0..1]
Definition: Entity involved in an activity.
MaintainingCSD <MntngCSD> contains one of the following elements (see
"SystemPartyIdentification2Choice" on page 488 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 489
Or}   CombinedIdentification <CmbndId> [1..1] ± 489
6.4.3.9  InvestorCSD <InvstrCSD>
Presence: [0..1]
Definition: Entity involved in an activity.
InvestorCSD <InvstrCSD> contains one of the following elements (see
"SystemPartyIdentification2Choice" on page 488 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 489
Or}   CombinedIdentification <CmbndId> [1..1] ± 489
6.4.3.10  IssuerCSD <IssrCSD>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.010.001.01 SecurityQueryV01
Target2-Securities - Securities Reference Data 87 March 2024
```

