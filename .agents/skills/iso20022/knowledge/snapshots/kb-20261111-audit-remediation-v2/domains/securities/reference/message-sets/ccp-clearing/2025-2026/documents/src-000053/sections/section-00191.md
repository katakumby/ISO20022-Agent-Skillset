---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["7 MX secl.006.001.02 DefaultFundContributionReportV02", "7.4 Message Building Blocks", "7.4.1 ReportParameters <RptParams>", "7.4.1.1 ReportIdentification <RptId>"]
file_pages: [250]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.006.001.02"]
---

# 7.4.1.1 ReportIdentification <RptId>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 250 to 250.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 250

```text
ReportParameters <RptParams> contains the following ReportParameters2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportIdentification <RptId> [1..1] Text 250
   ReportDateAndTime <RptDtAndTm> [1..1] ± 250
   Frequency <Frqcy> [1..1] CodeSet 250
   ReportCurrency <RptCcy> [1..1] CodeSet C10 250
   CalculationDate <ClctnDt> [0..1] DateTime 251
7.4.1.1  ReportIdentification <RptId>
Presence: [1..1]
Definition: Unique identification of the report.
Datatype: Max35Text on page 493
7.4.1.2  ReportDateAndTime <RptDtAndTm>
Presence: [1..1]
Definition: Date (and time) at which the report was created.
ReportDateAndTime <RptDtAndTm> contains one of the following elements (see
DateAndDateTimeChoice on page 390 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 390
Or}   DateTime <DtTm> [1..1] DateTime 390
7.4.1.3  Frequency <Frqcy>
Presence: [1..1]
Definition: Frequency of the report.
Datatype: EventFrequency6Code on page 477
CodeName Name Definition
DAIL Daily Event takes place every day.
INDA IntraDay Event takes place several times a day.
ONDE OnDemand Event takes place on demand.
7.4.1.4  ReportCurrency <RptCcy>
Presence: [1..1]
Definition: Indicates the currency used for the calculation of the guarantee fund.
Impacted by: C10 ValidationByTable
Datatype: CurrencyCode on page 476
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.006.001.02
DefaultFundContributionReportV02
March 2026 250
```

