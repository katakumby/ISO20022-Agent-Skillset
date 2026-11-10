---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["6 MX secl.005.001.02 MarginReportV02", "6.4 Message Building Blocks", "6.4.1 ReportParameters <RptParams>", "6.4.1.1 ReportIdentification <RptId>"]
file_pages: [238]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.005.001.02"]
---

# 6.4.1.1 ReportIdentification <RptId>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 238 to 238.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 238

```text
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different ReportNumbers. For example, a daily report sent on day 1
would have ReportNumber 001, on day 2, 002, etc.
6.4.1.1  ReportIdentification <RptId>
Presence: [1..1]
Definition: Unique identification of the report.
Datatype: Max35Text on page 493
6.4.1.2  ReportDateAndTime <RptDtAndTm>
Presence: [1..1]
Definition: Date (and time) and time of the report.
ReportDateAndTime <RptDtAndTm> contains one of the following elements (see
DateAndDateTimeChoice on page 390 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 390
Or}   DateTime <DtTm> [1..1] DateTime 390
6.4.1.3  ReportCurrency <RptCcy>
Presence: [1..1]
Definition: Currency used for the calculation of the margin.
Impacted by: C16 ValidationByTable
Datatype: CurrencyCode on page 476
Constraints
• ValidationByTable
(Rule)
Must be a valid currency code which is registered with the ISO 4217 Maintenance Agency, and
consist of three contiguous letters.
6.4.1.4  CalculationDateAndTime <ClctnDtAndTm>
Presence: [1..1]
Definition: Date of calculation of the margin.
Datatype: ISODateTime on page 487
6.4.1.5  Frequency <Frqcy>
Presence: [1..1]
Definition: Frequency of the report.
Datatype: EventFrequency6Code on page 477
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.005.001.02 MarginReportV02
March 2026 238
```

