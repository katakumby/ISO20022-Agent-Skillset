---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.12 Date Period", "66.1.12.3 Tax36", "66.1.12.3.1 DateOrPeriod <DtOrPrd>"]
file_pages: [4465]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.12.3.1 DateOrPeriod <DtOrPrd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4465 to 4465.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4465

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateOrPeriod <DtOrPrd> [1..1]  4465
{Or     Date <Dt> [1..1] Date 4465
Or}     Period <Prd> [1..1] Text 4465
   AdditionalInformation <AddtlInf> [0..*] ± 4465
66.1.12.3.1  DateOrPeriod <DtOrPrd>
Presence: [1..1]
Definition: Date or quarter of the tax year on which tax for the financial instrument is based or
calculated.
DateOrPeriod <DtOrPrd> contains one of the following DateQuarter1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4465
Or}   Period <Prd> [1..1] Text 4465
66.1.12.3.1.1  Date <Dt>
Presence: [1..1]
Definition: Date as year, month and day.
Datatype: "ISODate" on page 5388
66.1.12.3.1.2  Period <Prd>
Presence: [1..1]
Definition: Proprietary description of the timeframe.
Datatype: "Max35Text" on page 5403
66.1.12.3.2  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about tax.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.12.4  DateTimePeriod2
Definition: Time span defined by a start date and time, and an end date and time.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4465 May 2026
```

