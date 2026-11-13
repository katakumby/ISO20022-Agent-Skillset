---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.7 SettlementInformation <SttlmInf>", "4.4.3.8.9.7.1 SettlementMethod <SttlmMtd>"]
file_pages: [324]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.7.1 SettlementMethod <SttlmMtd>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 324 to 324.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 324

```text
Following Must be True
    /ClearingSystem Must be absent
 And    /InstructingReimbursementAgent Must be absent
 And    /InstructedReimbursementAgent Must be absent
 And    /ThirdReimbursementAgent Must be absent
• SettlementMethodClearingRule
If SettlementMethod is equal to CLRG, then SettlementAccount and ReimbursementAgent(s) are not
allowed.
On Condition
    /SettlementMethod is equal to value 'ClearingSystem'
Following Must be True
    /SettlementAccount Must be absent
 And    /InstructingReimbursementAgent Must be absent
 And    /InstructedReimbursementAgent Must be absent
 And    /ThirdReimbursementAgent Must be absent
• SettlementMethodCoverAgentRule
If SettlementMethod is equal to COVE, then InstructedReimbursementAgent or
InstructingReimbursementAgent must be present.
On Condition
    /SettlementMethod is equal to value 'CoverMethod'
Following Must be True
    /InstructingReimbursementAgent Must be present
 Or    /InstructedReimbursementAgent Must be present
• SettlementMethodCoverRule
If SettlementMethod is equal to COVE, then SettlementAccount and ClearingSystem are not allowed.
On Condition
    /SettlementMethod is equal to value 'CoverMethod'
Following Must be True
    /SettlementAccount Must be absent
 And    /ClearingSystem Must be absent
• ThirdReimbursementAgentAccountRule
If ThirdReimbursementAgentAccount is present, then ThirdReimbursementAgent must be present.
On Condition
    /ThirdReimbursementAgent is absent
Following Must be True
    /ThirdReimbursementAgentAccount Must be absent
• ThirdReimbursementAgentRule
If ThirdReimbursementAgent is present, then InstructingReimbursementAgent and
InstructedReimbursementAgent must both be present.
On Condition
    /ThirdReimbursementAgent is present
Following Must be True
    /InstructingReimbursementAgent Must be present
 And    /InstructedReimbursementAgent Must be present
4.4.3.8.9.7.1  SettlementMethod <SttlmMtd>
Presence: [1..1]
Definition: Method used to settle the (batch of) payment instructions.
Datatype: "SettlementMethod1Code" on page 601
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 324 March 2026
```

