---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["62 reda.045.001.01 SecurityCSDLinkCreationRequestV01", "62.4 Message Building Blocks", "62.4.2 SecurityCSDLink <SctyCSDLk>", "62.4.2.2 IssuerInvestorCSD <IssrInvstrCSD>", "62.4.2.2.2 InvestorCSD <InvstrCSD>"]
file_pages: [2346]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.045.001.01"]
---

# 62.4.2.2.2 InvestorCSD <InvstrCSD>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2346 to 2346.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2346

```text
CombinedIdentification <CmbndId> contains the following elements (see
"SystemPartyIdentification8" on page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
62.4.2.2.2  InvestorCSD <InvstrCSD>
Presence: [1..1]
Definition: CSD Investor of a security.
InvestorCSD <InvstrCSD> contains one of the following SystemPartyIdentification2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 2346
Or}   CombinedIdentification <CmbndId> [1..1] ± 2346
62.4.2.2.2.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Provides the identification of a party.
OrganisationIdentification <OrgId> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
62.4.2.2.2.2  CombinedIdentification <CmbndId>
Presence: [1..1]
Definition: Identifies the party with the combined identification of both the responsible entity and the
party itself.
CombinedIdentification <CmbndId> contains the following elements (see
"SystemPartyIdentification8" on page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
62.4.2.3  TechnicalIssuerCSD <TechIssrCSD>
Presence: [0..1]
Definition: Technical issuer of a security.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.045.001.01
SecurityCSDLinkCreationRequestV01
Target2-Securities 2346 August 2026
```

