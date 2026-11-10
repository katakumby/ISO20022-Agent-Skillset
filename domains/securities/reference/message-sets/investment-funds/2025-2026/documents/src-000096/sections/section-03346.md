---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.4 InvestmentAccountOwnershipInformation17", "66.1.24.4.11 FATCAStatus <FATCASts>"]
file_pages: [4587]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.4.11 FATCAStatus <FATCASts>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4587 to 4587.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4587

```text
FATCAFormType <FATCAFormTp> contains one of the following elements (see
"FATCAForm1Choice" on page 4831 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4832
Or}   Proprietary <Prtry> [1..1] ± 4832
66.1.24.4.11  FATCAStatus <FATCASts>
Presence: [0..*]
Definition: Foreign Account Tax Compliance Act (FATCA) status of the investor or account owner.
FATCAStatus <FATCASts> contains the following elements (see "FATCAStatus2" on page 4960 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  4960
{Or     Code <Cd> [1..1] CodeSet 4960
Or}     Proprietary <Prtry> [1..1] ± 4961
   Source <Src> [0..1]  4961
{Or     Code <Cd> [1..1] CodeSet 4962
Or}     Proprietary <Prtry> [1..1] ± 4962
66.1.24.4.12  FATCAReportingDate <FATCARptgDt>
Presence: [0..1]
Definition: Date provided by the account owner to inform the account servicer of the date on which the
holdings must be reported before the account is subsequently closed.
Datatype: "ISODate" on page 5388
66.1.24.4.13  CRSFormType <CRSFormTp>
Presence: [0..*]
Definition: Type of Common Reporting Standard (CRS) form submitted by the investor or account
owner.
CRSFormType <CRSFormTp> contains one of the following elements (see "CRSForm1Choice" on
page 5033 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5034
Or}   Proprietary <Prtry> [1..1] ± 5034
66.1.24.4.14  CRSStatus <CRSSts>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4587 May 2026
```

