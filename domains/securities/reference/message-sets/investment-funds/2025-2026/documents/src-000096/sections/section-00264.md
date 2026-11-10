---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["16 reda.005.001.03 InvestmentFundReportRequestV03", "16.4 Message Building Blocks", "16.4.4 ReportRequest <RptReq>", "16.4.4.2 Parameters <Params>", "16.4.4.2.3 DateFrom <DtFr>"]
file_pages: [370]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.005.001.03"]
---

# 16.4.4.2.3 DateFrom <DtFr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 370 to 370.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 370

```text
FundManagementCompany <FndMgmtCpny> contains the following elements (see
"PartyIdentification139" on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
16.4.4.2.3  DateFrom <DtFr>
Presence: [0..1]
Definition: Specifies the date on or after which the information required will have been last updated.
Only the most recent versions of the data is required.
Datatype: "ISODate" on page 5388
16.4.4.2.4  CountryOfDomicile <CtryOfDmcl>
Presence: [0..1]
Definition: Country where the fund has legal domicile.
Impacted by: C2 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
16.4.4.2.5  RegisteredDistributionCountry <RegdDstrbtnCtry>
Presence: [0..*]
Definition: Country where the fund is registered for distribution.
Impacted by: C2 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
Approved by the Securities SEG on 27 January 2026 reda.005.001.03
InvestmentFundReportRequestV03
Investment Funds - Maintenance 2025 - 2026 370 May 2026
```

