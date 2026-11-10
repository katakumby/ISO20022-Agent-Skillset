---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.1.10 SettlementInformation <SttlmInf>", "4.4.1.10.1 SettlementMethod <SttlmMtd>"]
file_pages: [279]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.1.10.1 SettlementMethod <SttlmMtd>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 279 to 279.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 279

```text
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
4.4.1.10.1  SettlementMethod <SttlmMtd>
Presence: [1..1]
Definition: Method used to settle the (batch of) payment instructions.
Datatype: "SettlementMethod1Code" on page 1237
CodeName Name Definition
INDA InstructedAgent Settlement is done by the agent
instructed to execute a payment
instruction.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
279 March 2026
```

