---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01", "64.4 Message Building Blocks", "64.4.3 SecurityCSDLinkIdentification <SctyCSDLkId>", "64.4.3.2 IssuerInvestorCSD <IssrInvstrCSD>", "64.4.3.2.1 IssuerCSD <IssrCSD>"]
file_pages: [2366]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.047.001.01"]
---

# 64.4.3.2.1 IssuerCSD <IssrCSD>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2366 to 2366.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2366

```text
IssuerInvestorCSD <IssrInvstrCSD> contains one of the following IssuerOrInvestor2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IssuerCSD <IssrCSD> [1..1]  2366
{Or     OrganisationIdentification <OrgId> [1..1] ± 2366
Or}     CombinedIdentification <CmbndId> [1..1] ± 2366
Or}   InvestorCSD <InvstrCSD> [1..1]  2367
{Or     OrganisationIdentification <OrgId> [1..1] ± 2367
Or}     CombinedIdentification <CmbndId> [1..1] ± 2367
64.4.3.2.1  IssuerCSD <IssrCSD>
Presence: [1..1]
Definition: CSD Issuer of a security.
IssuerCSD <IssrCSD> contains one of the following SystemPartyIdentification2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 2366
Or}   CombinedIdentification <CmbndId> [1..1] ± 2366
64.4.3.2.1.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Provides the identification of a party.
OrganisationIdentification <OrgId> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
64.4.3.2.1.2  CombinedIdentification <CmbndId>
Presence: [1..1]
Definition: Identifies the party with the combined identification of both the responsible entity and the
party itself.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.047.001.01 SecurityCSDLinkStatusAdviceV01
Target2-Securities 2366 August 2026
```

