---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["7 reda.012.001.01 SecurityReportV01", "7.4 Message Building Blocks", "7.4.3 SecurityReportOrError <SctyRptOrErr>", "7.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "7.4.3.1.1 SecurityReport <SctyRpt>"]
file_pages: [100]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 7.4.3.1.1 SecurityReport <SctyRpt>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 100 to 100.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 100

```text
SecurityReportOrBusinessError <SctyRptOrBizErr> contains one of the following
SecurityOrBusinessError4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecurityReport <SctyRpt> [1..*]  100
     FinancialInstrumentIdentification <FinInstrmId> [0..*] ± C6, C7,
C8, C9,
C12
100
     FinancialInstrumentType <FinInstrmTp> [0..1] ± 101
     FinancialInstrumentAttributes <FinInstrmAttrbts> [0..*] ± 102
Or}   BusinessError <BizErr> [1..*]  111
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C6, C7,
C8, C9,
C12
111
     BusinessError <BizErr> [1..*]  112
       Error <Err> [1..1]  112
{Or         Code <Cd> [1..1] CodeSet 112
Or}         Proprietary <Prtry> [1..1] Text 113
       Description <Desc> [0..1] Text 113
7.4.3.1.1  SecurityReport <SctyRpt>
Presence: [1..*]
Definition: Provides the financial instruments details.
SecurityReport <SctyRpt> contains the following SecurityAttributes11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [0..*] ± C6, C7,
C8, C9,
C12
100
   FinancialInstrumentType <FinInstrmTp> [0..1] ± 101
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..*] ± 102
7.4.3.1.1.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..*]
Definition: Way(s) of identifying the security.
Impacted by: C6 "DescriptionPresenceRule", C7 "DescriptionUsageRule", C8 "ISINGuideline", C9
"ISINPresenceRule", C12 "OtherIdentificationPresenceRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.012.001.01 SecurityReportV01
Target2-Securities - Securities Reference Data 100 March 2024
```

