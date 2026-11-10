---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.8 Frequency", "6.1.8.1 Frequency36Choice", "6.1.8.1.2 Period <Prd>", "6.1.8.1.2.1 Type <Tp>"]
file_pages: [546]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.8.1.2.1 Type <Tp>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 546 to 546.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 546

```text
6.1.8.1.2.1  Type <Tp>
Presence: [1..1]
Definition: Period for which the number of instructions are to be created and processed.
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
6.1.8.1.2.2  CountPerPeriod <CntPerPrd>
Presence: [1..1]
Definition: Number of instructions to be created and processed during the specified period.
Datatype: "DecimalNumber" on page 606
6.1.8.1.3  PointInTime <PtInTm>
Presence: [1..1]
Definition: Specifies a frequency in terms of an exact point in time or moment within a specified period
type.
PointInTime <PtInTm> contains the following FrequencyAndMoment1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 546
   PointInTime <PtInTm> [1..1] Text 547
6.1.8.1.3.1  Type <Tp>
Presence: [1..1]
Definition: Period for which the number of instructions are to be created and processed.
Datatype: "Frequency6Code" on page 598
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 546 March 2026
```

