---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.6 Date Time Period", "16.1.6.5 Period11", "16.1.6.5.2 EndDate <EndDt>", "16.1.6.5.2.2 NotSpecifiedDate <NotSpcfdDt>"]
file_pages: [857]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.6.5.2.2 NotSpecifiedDate <NotSpcfdDt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 857 to 857.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 857

```text
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 848 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 848
Or}   DateTime <DtTm> [1..1] DateTime 849
16.1.6.5.2.2  NotSpecifiedDate <NotSpcfdDt>
Presence: [1..1]
Definition: Date not specified, for example, the date is unknown.
Datatype: "DateType8Code" on page 1206
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
ONGO Ongoing Ongoing basis, which indicates that the
date is determined by "ongoing basis"
process, for example "au fil de l'eau".
16.1.6.6  Period12Choice
Definition: Choice between a period or a period code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
16.1.6.6.1  Period <Prd>
Presence: [1..1]
Definition: Time span defined by a start date and time, and an end date and time.
Period <Prd> contains the following elements (see "Period18" on page 851 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StartDate <StartDt> [1..1]  852
{Or     Date <Dt> [1..1] Date 852
Or}     NotSpecifiedDate <NotSpcfdDt> [1..1] CodeSet 852
   EndDate <EndDt> [1..1]  852
{Or     Date <Dt> [1..1] Date 853
Or}     NotSpecifiedDate <NotSpcfdDt> [1..1] CodeSet 853
16.1.6.6.2  PeriodCode <PrdCd>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 857 February 2026
```

