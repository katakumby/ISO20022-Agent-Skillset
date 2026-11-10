---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["7 reda.012.001.01 SecurityReportV01", "7.4 Message Building Blocks", "7.4.3 SecurityReportOrError <SctyRptOrErr>", "7.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>"]
file_pages: [99]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 7.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 99 to 99.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 99

```text
SecurityReportOrError <SctyRptOrErr> contains one of the following
SecurityOrOperationalError4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecurityReportOrBusinessError <SctyRptOrBizErr> [1..1]  99
{Or     SecurityReport <SctyRpt> [1..*]  100
       FinancialInstrumentIdentification <FinInstrmId> [0..*] ± C6, C7,
C8, C9,
C12
100
       FinancialInstrumentType <FinInstrmTp> [0..1] ± 101
       FinancialInstrumentAttributes <FinInstrmAttrbts> [0..*] ± 102
Or}     BusinessError <BizErr> [1..*]  111
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C6, C7,
C8, C9,
C12
111
       BusinessError <BizErr> [1..*]  112
         Error <Err> [1..1]  112
{Or           Code <Cd> [1..1] CodeSet 112
Or}           Proprietary <Prtry> [1..1] Text 113
         Description <Desc> [0..1] Text 113
Or}   OperationalError <OprlErr> [1..*]  113
     Error <Err> [1..1]  113
{Or       Code <Cd> [1..1] CodeSet 113
Or}       Proprietary <Prtry> [1..1] Text 113
     Description <Desc> [0..1] Text 114
7.4.3.1  SecurityReportOrBusinessError <SctyRptOrBizErr>
Presence: [1..1]
Definition: Provides the financial instruments details or the business error.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.012.001.01 SecurityReportV01
Target2-Securities - Securities Reference Data 99 March 2024
```

