---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01", "3.4 Message Building Blocks", "3.4.2 SecurityCSDLinkIdentification <SctyCSDLkId>", "3.4.2.2 IssuerInvestorCSD <IssrInvstrCSD>", "3.4.2.2.2 InvestorCSD <InvstrCSD>", "3.4.2.2.2.2 CombinedIdentification <CmbndId>"]
file_pages: [23]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.046.001.01"]
---

# 3.4.2.2.2.2 CombinedIdentification <CmbndId>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 23 to 23.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 23

```text
OrganisationIdentification <OrgId> contains the following elements (see "PartyIdentification136" on
page 68 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 69
   LEI <LEI> [0..1] IdentifierSet 69
3.4.2.2.2.2  CombinedIdentification <CmbndId>
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
3.4.2.3  ValidFrom <VldFr>
Presence: [1..1]
Definition: Defines the date since when the CSD is linked to the security.
ValidFrom <VldFr> contains one of the following elements (see "DateAndDateTime2Choice" on
page 60 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 61
Or}   DateTime <DtTm> [1..1] DateTime 61
3.4.3 Update <Upd>
Presence: [1..1]
Definition: Provides data that needs to be maintained.
Update <Upd> contains the following SecurityCSDLinkUpdate3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DefaultLink <DfltLk> [0..1] Indicator 23
   ValidTo <VldTo> [1..1] ± 24
3.4.3.1  DefaultLink <DfltLk>
Presence: [0..1]
Definition: Specifies whether the security CSD link is the default link.
Approved by the Securities SEG on 21 November 2024. reda.046.001.01
SecurityCSDLinkMaintenanceRequestV01
Target2-Securities - Link Reference Data 23 December 2024
```

