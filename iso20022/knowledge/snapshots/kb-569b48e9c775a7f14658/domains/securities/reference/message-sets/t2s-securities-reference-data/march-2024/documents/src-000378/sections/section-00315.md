---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.3 CommonFinancialInstrumentAttributes11", "13.1.6.3.52 SecurityCSDLink <SctyCSDLk>", "13.1.6.3.52.4 IssuerCSD <IssrCSD>"]
file_pages: [400]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.3.52.4 IssuerCSD <IssrCSD>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 400 to 400.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 400

```text
• Meaning When True: Yes
• Meaning When False: No
13.1.6.3.52.4  IssuerCSD <IssrCSD>
Presence: [0..1]
Definition: CSD Issuer of a security.
IssuerCSD <IssrCSD> contains one of the following elements (see "SystemPartyIdentification2Choice"
on page 488 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 489
Or}   CombinedIdentification <CmbndId> [1..1] ± 489
13.1.6.3.52.5  InvestorCSD <InvstrCSD>
Presence: [0..1]
Definition: CSD Investor of a security.
InvestorCSD <InvstrCSD> contains one of the following elements (see
"SystemPartyIdentification2Choice" on page 488 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 489
Or}   CombinedIdentification <CmbndId> [1..1] ± 489
13.1.6.3.52.6  TechnicalIssuerCSD <TechIssrCSD>
Presence: [0..1]
Definition: Technical issuer of a security.
TechnicalIssuerCSD <TechIssrCSD> contains one of the following elements (see
"SystemPartyIdentification2Choice" on page 488 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 489
Or}   CombinedIdentification <CmbndId> [1..1] ± 489
13.1.6.3.52.7  IssuanceAccount <IssncAcct>
Presence: [0..*]
Definition: Account to or from which a securities entry is made.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 400 March 2024
```

