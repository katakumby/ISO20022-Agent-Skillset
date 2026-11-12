---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks"]
file_pages: [325]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4 Message Building Blocks

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 325 to 325.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 325

```text
If OtherIdentification is not present then either ISIN or Description must be
present. (CrossElementComplexRule)
Error handling:
– Error severity: Fatal
– Error Code: X00193
– Error Text: At least one identification must be present.
C18 SupplementaryDataRule
(Rule)
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C19 ValidationByTable
(Rule)
Must be a valid currency code which is registered with the ISO 4217 Maintenance Agency, and
consist of three contiguous letters. (Algorithm)
11.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
11.4.1 ReportParameters <RptParams>
Presence: [1..1]
Definition: Provides details about the report such as the report identification, the creation date and time.
ReportParameters <RptParams> contains the following ReportParameters8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportIdentification <RptId> [1..1] Text 325
   ReportDateAndTime <RptDtAndTm> [1..1] ± 325
11.4.1.1  ReportIdentification <RptId>
Presence: [1..1]
Definition: Unique identification of the report.
Datatype: Max35Text on page 493
11.4.1.2  ReportDateAndTime <RptDtAndTm>
Presence: [1..1]
Definition: Date and time of the report.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 325
```

