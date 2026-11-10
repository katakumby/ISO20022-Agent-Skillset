---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.52 SecurityCSDLink <SctyCSDLk>", "32.4.3.1.1.3.52.6 TechnicalIssuerCSD <TechIssrCSD>", "32.4.3.1.1.3.52.6.1 OrganisationIdentification <OrgId>"]
file_pages: [2033]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.52.6.1 OrganisationIdentification <OrgId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2033 to 2033.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2033

```text
TechnicalIssuerCSD <TechIssrCSD> contains one of the following
SystemPartyIdentification2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 2033
Or}   CombinedIdentification <CmbndId> [1..1] ± 2033
32.4.3.1.1.3.52.6.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Provides the identification of a party.
OrganisationIdentification <OrgId> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
32.4.3.1.1.3.52.6.2  CombinedIdentification <CmbndId>
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
32.4.3.1.1.3.52.7  IssuanceAccount <IssncAcct>
Presence: [0..*]
Definition: Account to or from which a securities entry is made.
IssuanceAccount <IssncAcct> contains the following IssuanceAccount2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IssuanceAccount <IssncAcct> [1..1] ± 2033
   PrimaryAccountIndicator <PmryAcctInd> [1..1] Indicator 2034
32.4.3.1.1.3.52.7.1  IssuanceAccount <IssncAcct>
Presence: [1..1]
Definition: Account to or from which a securities entry is made.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 2033 August 2026
```

