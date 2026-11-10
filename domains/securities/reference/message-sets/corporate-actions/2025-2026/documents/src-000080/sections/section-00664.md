---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.6 Date Time Period", "16.1.6.4 Period6Choice", "16.1.6.4.2 PeriodCode <PrdCd>"]
file_pages: [855]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.6.4.2 PeriodCode <PrdCd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 855 to 855.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 855

```text
Period <Prd> contains the following elements (see "Period11" on page 855 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StartDate <StartDt> [1..1]  855
{Or     Date <Dt> [1..1] ± 856
Or}     NotSpecifiedDate <NotSpcfdDt> [1..1] CodeSet 856
   EndDate <EndDt> [1..1]  856
{Or     Date <Dt> [1..1] ± 856
Or}     NotSpecifiedDate <NotSpcfdDt> [1..1] CodeSet 857
16.1.6.4.2  PeriodCode <PrdCd>
Presence: [1..1]
Definition: Standard code to specify the type of period.
Datatype: "DateType8Code" on page 1206
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
ONGO Ongoing Ongoing basis, which indicates that the
date is determined by "ongoing basis"
process, for example "au fil de l'eau".
16.1.6.5  Period11
Definition: Time span defined by a start date and time, and an end date and time.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StartDate <StartDt> [1..1]  855
{Or     Date <Dt> [1..1] ± 856
Or}     NotSpecifiedDate <NotSpcfdDt> [1..1] CodeSet 856
   EndDate <EndDt> [1..1]  856
{Or     Date <Dt> [1..1] ± 856
Or}     NotSpecifiedDate <NotSpcfdDt> [1..1] CodeSet 857
16.1.6.5.1  StartDate <StartDt>
Presence: [1..1]
Definition: Date and time at which the range starts.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 855 February 2026
```

