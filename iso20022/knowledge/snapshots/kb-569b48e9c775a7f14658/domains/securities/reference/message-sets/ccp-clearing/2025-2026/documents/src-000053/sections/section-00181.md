---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["6 MX secl.005.001.02 MarginReportV02", "6.4 Message Building Blocks"]
file_pages: [237]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.005.001.02"]
---

# 6.4 Message Building Blocks

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 237 to 237.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 237

```text
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C16 ValidationByTable
(Rule)
Must be a valid currency code which is registered with the ISO 4217 Maintenance Agency, and
consist of three contiguous letters. (Algorithm)
C17 VariationMarginTextualRule
(Rule)
If the margin amount calculation is to be shown in more details (with for example, the
MarkToMarketNetted or MarkToMarketGross amounts), then it is recommended to use the
element variation margin that is present at a higher level in the message.
6.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
6.4.1 ReportParameters <RptParams>
Presence: [1..1]
Definition: Provides parameters of the margin report such as the creation date and time, the report
currency or the calculation date and time.
Impacted by: C14 ReportNumberRule
ReportParameters <RptParams> contains the following ReportParameters3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportIdentification <RptId> [1..1] Text 238
   ReportDateAndTime <RptDtAndTm> [1..1] ± 238
   ReportCurrency <RptCcy> [1..1] CodeSet C16 238
   CalculationDateAndTime <ClctnDtAndTm> [1..1] DateTime 238
   Frequency <Frqcy> [1..1] CodeSet 238
   ReportNumber <RptNb> [0..1] Text 239
Constraints
• ReportNumberRule
(Rule)
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.005.001.02 MarginReportV02
March 2026 237
```

