---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.12 Rate", "22.1.12.1 BenchmarkCurveName6Choice", "22.1.12.1.3 Name <Nm>"]
file_pages: [358]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.12.1.3 Name <Nm>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 358 to 358.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 358

```text
CodeName Name Definition
EUCH EuroSwiss Swiss Franc LIBOR rate.
EUUS EURODOLLAR Rate for the eurodollars, time deposits
denominated in U.S. dollars at banks
outside the United States, and thus are
not under the jurisdiction of the Federal
Reserve.
EURI Euribor Euro Interbank Offer Rate is the rate at
which Euro inter-bank term deposits
within the Euro zone are offered by one
prime bank to another prime bank.
EONS EONIASwaps Euro OverNight Index Average swap
rate.
EONA EONIA Euro OverNight Index Average rate.
CIBO CIBOR Copenhagen Interbank Offered Rate.
CDOR CDOR Canadian Dollar Offered Rate.
BUBO BUBOR Budapest Interbank Offered Rate.
BBSW BBSW Australian Financial Markets Association
(AFMA) Bank-Bill Reference Rate
(BBSW).
22.1.12.1.3  Name <Nm>
Presence: [1..1]
Definition: Provides the name that should be used where no ISIN or standardized name of the index
exists, including its term (such as 'EURIBOR6M', 'LIBOR3M').
Datatype: "Max25Text" on page 455
22.1.12.2  InterestRateContractTerm2
Definition: Describes how interest rates are reported.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] CodeSet 358
   Value <Val> [1..1] Quantity C7 359
22.1.12.2.1  Unit <Unit>
Presence: [1..1]
Definition: Unit for the rate basis.
Datatype: "RateBasis1Code" on page 443
CodeName Name Definition
DAYS Days Rate is reported in days.
MNTH Months Rate is reported in months.
WEEK Weeks Rate is reported in weeks.
YEAR Years Rate is reported in years.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
358 July 2025
```

