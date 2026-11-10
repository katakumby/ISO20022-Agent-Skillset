---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.22 Frequency", "66.1.22.1 StatementFrequencyReason2Choice", "66.1.22.1.1 Code <Cd>"]
file_pages: [4535]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.22.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4535 to 4535.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4535

```text
66.1.22.1.1  Code <Cd>
Presence: [1..1]
Definition: Statement frequency expressed as a code.
Datatype: "EventFrequency9Code" on page 5299
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
NONE None Event does not take place.
66.1.22.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Statement frequency expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.22.2  Frequency20Choice
Definition: Choice of formats for the frequency.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4535 May 2026
```

