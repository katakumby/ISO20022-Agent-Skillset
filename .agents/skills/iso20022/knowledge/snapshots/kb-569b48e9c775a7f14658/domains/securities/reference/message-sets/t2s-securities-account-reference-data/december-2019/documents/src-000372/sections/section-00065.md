---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01", "10.4 Message Building Blocks", "10.4.1 MessageHeader <MsgHdr>", "10.4.1.3 OriginalBusinessInstruction <OrgnlBizInstr>"]
file_pages: [71]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.037.001.01"]
---

# 10.4.1.3 OriginalBusinessInstruction <OrgnlBizInstr>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 71 to 71.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 71

```text
10.4.1.3  OriginalBusinessInstruction <OrgnlBizInstr>
Presence: [0..1]
Definition: Unique identification of the original instruction.
OriginalBusinessInstruction <OrgnlBizInstr> contains the following elements (see
"OriginalBusinessInstruction1" on page 82 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 82
   MessageNameIdentification <MsgNmId> [0..1] Text 83
   CreationDateTime <CreDtTm> [0..1] DateTime 83
10.4.2 ReportOrError <RptOrErr>
Presence: [1..1]
Definition: Provides information on report or error resulting from the originating query message.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.037.001.01
SecuritiesAccountAuditTrailReportV01
Target2-Securities - Securities Account Reference Data 71 December 2019
```

