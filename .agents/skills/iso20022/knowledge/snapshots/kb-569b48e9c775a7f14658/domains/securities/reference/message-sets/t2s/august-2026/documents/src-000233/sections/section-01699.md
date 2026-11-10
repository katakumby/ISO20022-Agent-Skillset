---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["62 reda.045.001.01 SecurityCSDLinkCreationRequestV01", "62.4 Message Building Blocks", "62.4.2 SecurityCSDLink <SctyCSDLk>", "62.4.2.3 TechnicalIssuerCSD <TechIssrCSD>", "62.4.2.3.1 OrganisationIdentification <OrgId>"]
file_pages: [2347]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.045.001.01"]
---

# 62.4.2.3.1 OrganisationIdentification <OrgId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2347 to 2347.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2347

```text
TechnicalIssuerCSD <TechIssrCSD> contains one of the following
SystemPartyIdentification2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 2347
Or}   CombinedIdentification <CmbndId> [1..1] ± 2347
62.4.2.3.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Provides the identification of a party.
OrganisationIdentification <OrgId> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
62.4.2.3.2  CombinedIdentification <CmbndId>
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
62.4.2.4  SecurityMaintenance <SctyMntnc>
Presence: [1..1]
Definition: Specifies if the involved CSD (issuer/technical issuer/investor) is also the maintainer of
related reference data.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 3323):
• Meaning When True: True
• Meaning When False: False
62.4.2.5  IssuanceAccount <IssncAcct>
Presence: [0..*]
Definition: Account to or from which a securities entry is made.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.045.001.01
SecurityCSDLinkCreationRequestV01
Target2-Securities 2347 August 2026
```

