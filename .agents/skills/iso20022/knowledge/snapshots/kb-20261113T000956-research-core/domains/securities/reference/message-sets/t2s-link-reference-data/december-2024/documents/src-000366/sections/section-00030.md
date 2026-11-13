---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01", "4.4 Message Building Blocks", "4.4.3 SecurityCSDLinkIdentification <SctyCSDLkId>", "4.4.3.2 IssuerInvestorCSD <IssrInvstrCSD>", "4.4.3.2.1 IssuerCSD <IssrCSD>"]
file_pages: [32]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.047.001.01"]
---

# 4.4.3.2.1 IssuerCSD <IssrCSD>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 32 to 32.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 32

```text
IssuerInvestorCSD <IssrInvstrCSD> contains one of the following IssuerOrInvestor2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IssuerCSD <IssrCSD> [1..1]  32
{Or     OrganisationIdentification <OrgId> [1..1] ± 32
Or}     CombinedIdentification <CmbndId> [1..1] ± 32
Or}   InvestorCSD <InvstrCSD> [1..1]  33
{Or     OrganisationIdentification <OrgId> [1..1] ± 33
Or}     CombinedIdentification <CmbndId> [1..1] ± 33
4.4.3.2.1  IssuerCSD <IssrCSD>
Presence: [1..1]
Definition: CSD Issuer of a security.
IssuerCSD <IssrCSD> contains one of the following SystemPartyIdentification2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 32
Or}   CombinedIdentification <CmbndId> [1..1] ± 32
4.4.3.2.1.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Provides the identification of a party.
OrganisationIdentification <OrgId> contains the following elements (see "PartyIdentification136" on
page 68 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 69
   LEI <LEI> [0..1] IdentifierSet 69
4.4.3.2.1.2  CombinedIdentification <CmbndId>
Presence: [1..1]
Definition: Identifies the party with the combined identification of both the responsible entity and the
party itself.
Approved by the Securities SEG on 21 November 2024. reda.047.001.01 SecurityCSDLinkStatusAdviceV01
Target2-Securities - Link Reference Data 32 December 2024
```

