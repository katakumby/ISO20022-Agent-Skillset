---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["63 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01", "63.4 Message Building Blocks", "63.4.2 SecurityCSDLinkIdentification <SctyCSDLkId>", "63.4.2.2 IssuerInvestorCSD <IssrInvstrCSD>"]
file_pages: [2355]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.046.001.01"]
---

# 63.4.2.2 IssuerInvestorCSD <IssrInvstrCSD>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2355 to 2355.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2355

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
63.4.2.2  IssuerInvestorCSD <IssrInvstrCSD>
Presence: [1..1]
Definition: CSD Issuer of a security.
IssuerInvestorCSD <IssrInvstrCSD> contains one of the following IssuerOrInvestor2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IssuerCSD <IssrCSD> [1..1]  2355
{Or     OrganisationIdentification <OrgId> [1..1] ± 2356
Or}     CombinedIdentification <CmbndId> [1..1] ± 2356
Or}   InvestorCSD <InvstrCSD> [1..1]  2356
{Or     OrganisationIdentification <OrgId> [1..1] ± 2356
Or}     CombinedIdentification <CmbndId> [1..1] ± 2357
63.4.2.2.1  IssuerCSD <IssrCSD>
Presence: [1..1]
Definition: CSD Issuer of a security.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.046.001.01
SecurityCSDLinkMaintenanceRequestV01
Target2-Securities 2355 August 2026
```

