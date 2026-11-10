---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.9 InvestmentAccount73", "66.1.24.9.30 PowerOfAttorneyLevelOfControl <PwrOfAttnyLvlOfCtrl>"]
file_pages: [4630]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.9.30 PowerOfAttorneyLevelOfControl <PwrOfAttnyLvlOfCtrl>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4630 to 4630.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4630

```text
66.1.24.9.30  PowerOfAttorneyLevelOfControl <PwrOfAttnyLvlOfCtrl>
Presence: [0..1]
Definition: Functionality permitted to a third party in the actions that may be taken on an account on
behalf of the investor.
PowerOfAttorneyLevelOfControl <PwrOfAttnyLvlOfCtrl> contains one of the following elements
(see "LevelOfControl1Choice" on page 4832 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4833
Or}   Proprietary <Prtry> [1..1] ± 4833
66.1.24.9.31  AccountingStatus <AcctgSts>
Presence: [0..1]
Definition: Specifies if the account is regarded as domestic or non-domestic for reporting purposes.
AccountingStatus <AcctgSts> contains one of the following elements (see
"AccountingStatus1Choice" on page 5184 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5184
Or}   Proprietary <Prtry> [1..1] ± 5185
66.1.24.9.32  OpeningDate <OpngDt>
Presence: [0..1]
Definition: Legal opening date for the account.
OpeningDate <OpngDt> contains one of the following elements (see "DateAndDateTime1Choice" on
page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4467
Or}   DateTime <DtTm> [1..1] DateTime 4467
66.1.24.9.33  ClosingDate <ClsgDt>
Presence: [0..1]
Definition: Legal closing date for the account.
ClosingDate <ClsgDt> contains one of the following elements (see "DateAndDateTime1Choice" on
page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4467
Or}   DateTime <DtTm> [1..1] DateTime 4467
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4630 May 2026
```

