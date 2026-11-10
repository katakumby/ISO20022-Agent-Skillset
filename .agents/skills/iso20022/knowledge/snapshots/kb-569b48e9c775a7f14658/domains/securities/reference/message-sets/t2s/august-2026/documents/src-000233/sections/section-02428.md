---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.21 CancelledStatusReason5Code"]
file_pages: [3220]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.21 CancelledStatusReason5Code

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3220 to 3220.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3220

```text
Type: CodeSet
Format
minLength 1
maxLength 4
CodeName Name Definition
SCEX SecuritiesNoLongerEligible Transaction has been cancelled; the
security no longer exists or is no longer
eligible on the market instructed. For
corporate action related cancellation,
CORP should be used.
OTHR Other Other. See Narrative.
CXLR EndOfLife Transaction is rejected by the executing
party, the rejection is final therefore the
order is cancelled in the system.
BYIY CancelledDueToBuyIn Instruction has been cancelled because
a buy-in has been initiated.
CTHP CancelledByThirdParty Instruction is cancelled by a Third party.
CANZ CancelledSplitPartialSettlement Original transaction has been cancelled
and replaced to allow a partial or split
settlement.
CANT CancelledDueToTransformation Original transaction has been cancelled
and replaced due to a corporate action.
CSUB CancelledByAgent Instruction has been cancelled by the
agent due to an event deadline
extension.
CANS CancelledBySystem Transaction is cancelled by the system.
CANI CancelledByYourself Transaction is cancelled by yourself.
CORP CancelledDueToCorporateAction Transaction has been cancelled due to a
corporate action.
82.2.2.21  CancelledStatusReason5Code
Definition: Specifies the underlying reason for the cancellation of the associated transaction.
Type: CodeSet
CodeName Name Definition
CANI CancelledByYourself Transaction is cancelled by yourself.
OTHR Other Other. See Narrative.
82.2.2.22  CashSettlementSystem2Code
Definition: Specifies the cash settlement system used.
Type: CodeSet
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3220 August 2026
```

