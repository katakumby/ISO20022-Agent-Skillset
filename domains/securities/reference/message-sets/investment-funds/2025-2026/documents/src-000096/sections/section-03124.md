---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.2 StatementOfInvestmentFundTransactions2", "66.1.5.2.1 StatementGeneralDetails <StmtGnlDtls>", "66.1.5.2.1.4 Frequency <Frqcy>"]
file_pages: [4349]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.2.1.4 Frequency <Frqcy>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4349 to 4349.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4349

```text
CreationDateTime <CreDtTm> contains one of the following elements (see
"DateAndDateTimeChoice" on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
66.1.5.2.1.4  Frequency <Frqcy>
Presence: [0..1]
Definition: Frequency of the statement.
Datatype: "EventFrequency1Code" on page 5297
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
SEMI SemiAnnual Event takes place every six months or
two times a year.
QUTR Quarterly Event takes place every three months or
four times a year.
TOMN EveryTwoMonths Event takes place every two months.
MNTH Monthly Event takes place every month or once a
month.
TWMN TwiceAMonth Event takes place two times a month.
TOWK EveryTwoWeeks Event takes place every two weeks.
WEEK Weekly Event takes place once a week.
DAIL Daily Event takes place every day.
ADHO Adhoc Event takes place as necessary.
INDA IntraDay Event takes place several times a day.
OVNG Overnight Event takes place overnight.
ONDE OnDemand Event takes place on demand.
66.1.5.2.1.5  UpdateType <UpdTp>
Presence: [1..1]
Definition: Specifies if the statement is complete or only contains changes.
Datatype: "StatementUpdateTypeCode" on page 5365
CodeName Name Definition
COMP Complete Statement is complete.
DELT Delta Statement contains changes only.
66.1.5.2.1.6  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4349 May 2026
```

