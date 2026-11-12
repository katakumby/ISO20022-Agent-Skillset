---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["2 reda.045.001.01 SecurityCSDLinkCreationRequestV01", "2.4 Message Building Blocks", "2.4.2 SecurityCSDLink <SctyCSDLk>", "2.4.2.3 TechnicalIssuerCSD <TechIssrCSD>", "2.4.2.3.1 OrganisationIdentification <OrgId>"]
file_pages: [13]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.045.001.01"]
---

# 2.4.2.3.1 OrganisationIdentification <OrgId>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 13 to 13.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 13

```text
TechnicalIssuerCSD <TechIssrCSD> contains one of the following
SystemPartyIdentification2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 13
Or}   CombinedIdentification <CmbndId> [1..1] ± 13
2.4.2.3.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Provides the identification of a party.
OrganisationIdentification <OrgId> contains the following elements (see "PartyIdentification136" on
page 68 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 69
   LEI <LEI> [0..1] IdentifierSet 69
2.4.2.3.2  CombinedIdentification <CmbndId>
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
2.4.2.4  SecurityMaintenance <SctyMntnc>
Presence: [1..1]
Definition: Specifies if the involved CSD (issuer/technical issuer/investor) is also the maintainer of
related reference data.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 77):
• Meaning When True: True
• Meaning When False: False
2.4.2.5  IssuanceAccount <IssncAcct>
Presence: [0..*]
Definition: Account to or from which a securities entry is made.
Approved by the Securities SEG on 21 November 2024. reda.045.001.01
SecurityCSDLinkCreationRequestV01
Target2-Securities - Link Reference Data 13 December 2024
```

