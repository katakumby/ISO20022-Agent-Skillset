---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.8 Frequency", "10.1.8.1 Frequency36Choice", "10.1.8.1.1 Type <Tp>"]
file_pages: [1179]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.8.1.1 Type <Tp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1179 to 1179.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1179

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Type <Tp> [1..1] CodeSet 1179
Or   Period <Prd> [1..1]  1179
     Type <Tp> [1..1] CodeSet 1180
     CountPerPeriod <CntPerPrd> [1..1] Quantity 1180
Or}   PointInTime <PtInTm> [1..1]  1180
     Type <Tp> [1..1] CodeSet 1180
     PointInTime <PtInTm> [1..1] Text 1181
10.1.8.1.1  Type <Tp>
Presence: [1..1]
Definition: Specifies a frequency in terms of a specified period type.
Datatype: "Frequency6Code" on page 1234
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
10.1.8.1.2  Period <Prd>
Presence: [1..1]
Definition: Specifies a frequency in terms of a count per period within a specified period type.
Period <Prd> contains the following FrequencyPeriod1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 1180
   CountPerPeriod <CntPerPrd> [1..1] Quantity 1180
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1179 March 2026
```

