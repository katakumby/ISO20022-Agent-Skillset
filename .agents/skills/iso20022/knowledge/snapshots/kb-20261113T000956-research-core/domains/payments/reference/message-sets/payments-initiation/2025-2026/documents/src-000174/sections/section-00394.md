---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.8 Frequency", "6.1.8.1 Frequency36Choice", "6.1.8.1.1 Type <Tp>"]
file_pages: [545]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.8.1.1 Type <Tp>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 545 to 545.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 545

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Type <Tp> [1..1] CodeSet 545
Or   Period <Prd> [1..1]  545
     Type <Tp> [1..1] CodeSet 546
     CountPerPeriod <CntPerPrd> [1..1] Quantity 546
Or}   PointInTime <PtInTm> [1..1]  546
     Type <Tp> [1..1] CodeSet 546
     PointInTime <PtInTm> [1..1] Text 547
6.1.8.1.1  Type <Tp>
Presence: [1..1]
Definition: Specifies a frequency in terms of a specified period type.
Datatype: "Frequency6Code" on page 598
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
MNTH Monthly Event takes place every month or once a
month.
QURT Quarterly Event takes place every three months or
four times a year.
MIAN SemiAnnual Event takes place every six months or
two times a year.
WEEK Weekly Event takes place once a week.
DAIL Daily Event takes place every day.
ADHO Adhoc Event takes place on request or as
necessary.
INDA IntraDay Event takes place several times a day.
FRTN Fortnightly Event takes place every two weeks.
6.1.8.1.2  Period <Prd>
Presence: [1..1]
Definition: Specifies a frequency in terms of a count per period within a specified period type.
Period <Prd> contains the following FrequencyPeriod1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 546
   CountPerPeriod <CntPerPrd> [1..1] Quantity 546
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 545 March 2026
```

