---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.7 InvestmentAccountOwnershipInformation16", "66.1.24.7.15 CRSReportingDate <CRSRptgDt>"]
file_pages: [4609]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.7.15 CRSReportingDate <CRSRptgDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4609 to 4609.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4609

```text
Definition: Common Reporting Standard (CRS) status of the investor or account owner.
CRSStatus <CRSSts> contains the following elements (see "CRSStatus4" on page 5034 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  5035
{Or     Code <Cd> [1..1] CodeSet 5035
Or}     Proprietary <Prtry> [1..1] ± 5036
   Source <Src> [0..1]  5036
{Or     Code <Cd> [1..1] CodeSet 5037
Or}     Proprietary <Prtry> [1..1] ± 5037
   ExceptionalReportingCountry <XcptnlRptgCtry> [0..1] CodeSet C12 5037
66.1.24.7.15  CRSReportingDate <CRSRptgDt>
Presence: [0..1]
Definition: Date provided by the account owner to inform the account servicer of the date on which the
holdings must be reported before the account is subsequently closed.
Datatype: "ISODate" on page 5388
66.1.24.7.16  OtherIdentification <OthrId>
Presence: [0..*]
Definition: Alternative identification, for example, national registration identification number, passport
number, tax identification number. This may be an account number used to further identify the
beneficial owner, for example, a Central Provident Fund (CFP) account as required for Singapore.
OtherIdentification <OthrId> contains the following elements (see "GenericIdentification82" on
page 4541 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4541
   Type <Tp> [1..1]  4541
{Or     Code <Cd> [1..1] CodeSet 4541
Or}     Proprietary <Prtry> [1..1] ± 4542
   Issuer <Issr> [0..1] Text 4543
   IssueDate <IsseDt> [0..1] Date 4543
   ExpiryDate <XpryDt> [0..1] Date 4543
   State <Stat> [0..1] Text 4543
   IssuerCountry <IssrCtry> [0..1] CodeSet C12 4543
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4609 May 2026
```

