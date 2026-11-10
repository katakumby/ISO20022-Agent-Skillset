---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.2 Message Datatypes", "17.2.2 CodeSet", "17.2.2.8 CancelledStatusReason5Code"]
file_pages: [477]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.2.2.8 CancelledStatusReason5Code

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 477 to 477.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 477

```text
CodeName Name Definition
CANS CancelledBySystem Transaction is cancelled by the system.
CSUB CancelledByAgent Instruction has been cancelled by the
agent due to an event deadline
extension.
CXLR EndOfLife Transaction is rejected by the executing
party, the rejection is final therefore the
order is cancelled in the system.
CANT CancelledDueToTransformation Original transaction has been cancelled
and replaced due to a corporate action.
CANZ CancelledSplitPartialSettlement Original transaction has been cancelled
and replaced to allow a partial or split
settlement.
CORP CancelledDueToCorporateAction Transaction has been cancelled due to a
corporate action.
SCEX SecuritiesNoLongerEligible Transaction has been cancelled; the
security no longer exists or is no longer
eligible on the market instructed. For
corporate action related cancellation,
CORP should be used.
OTHR Other Other. See Narrative.
CTHP CancelledByThirdParty Instruction is cancelled by a Third party.
17.2.2.8  CancelledStatusReason5Code
Definition: Specifies the underlying reason for the cancellation of the associated transaction.
Type: CodeSet
CodeName Name Definition
CANI CancelledByYourself Transaction is cancelled by yourself.
OTHR Other Other. See Narrative.
17.2.2.9  ClearingChannel2Code
Definition: Specifies the clearing channel for the routing of the transaction, as part of the payment type
identification.
Type: CodeSet
CodeName Name Definition
RTGS RealTimeGrossSettlementSystem Clearing channel is a real-time gross
settlement system.
RTNS RealTimeNetSettlementSystem Clearing channel is a real-time net
settlement system.
MPNS MassPaymentNetSystem Clearing channel is a mass payment net
settlement system.
BOOK BookTransfer Payment through internal book transfer.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
477 March 2024
```

