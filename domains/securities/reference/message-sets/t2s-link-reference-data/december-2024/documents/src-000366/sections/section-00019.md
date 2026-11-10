---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01", "3.4 Message Building Blocks", "3.4.2 SecurityCSDLinkIdentification <SctyCSDLkId>", "3.4.2.2 IssuerInvestorCSD <IssrInvstrCSD>"]
file_pages: [21]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.046.001.01"]
---

# 3.4.2.2 IssuerInvestorCSD <IssrInvstrCSD>

Source: [src-000366](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 21 to 21.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 21

```text
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
3.4.2.2  IssuerInvestorCSD <IssrInvstrCSD>
Presence: [1..1]
Definition: CSD Issuer of a security.
IssuerInvestorCSD <IssrInvstrCSD> contains one of the following IssuerOrInvestor2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IssuerCSD <IssrCSD> [1..1]  21
{Or     OrganisationIdentification <OrgId> [1..1] ± 22
Or}     CombinedIdentification <CmbndId> [1..1] ± 22
Or}   InvestorCSD <InvstrCSD> [1..1]  22
{Or     OrganisationIdentification <OrgId> [1..1] ± 22
Or}     CombinedIdentification <CmbndId> [1..1] ± 23
3.4.2.2.1  IssuerCSD <IssrCSD>
Presence: [1..1]
Definition: CSD Issuer of a security.
Approved by the Securities SEG on 21 November 2024. reda.046.001.01
SecurityCSDLinkMaintenanceRequestV01
Target2-Securities - Link Reference Data 21 December 2024
```

