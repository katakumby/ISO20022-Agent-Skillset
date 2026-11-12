---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["7 reda.012.001.01 SecurityReportV01", "7.4 Message Building Blocks", "7.4.2 Pagination <Pgntn>"]
file_pages: [98]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 7.4.2 Pagination <Pgntn>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 98 to 98.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 98

```text
OriginalBusinessInstruction <OrgnlBizInstr> contains the following elements (see
"OriginalBusinessInstruction1" on page 485 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 485
   MessageNameIdentification <MsgNmId> [0..1] Text 485
   CreationDateTime <CreDtTm> [0..1] DateTime 485
7.4.2 Pagination <Pgntn>
Presence: [1..1]
Definition: Provides details on the page number of the message.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 485 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 485
   LastPageIndicator <LastPgInd> [1..1] Indicator 485
7.4.3 SecurityReportOrError <SctyRptOrErr>
Presence: [1..1]
Definition: Provides the financial instruments details or error raised during the generation of the report.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.012.001.01 SecurityReportV01
Target2-Securities - Securities Reference Data 98 March 2024
```

