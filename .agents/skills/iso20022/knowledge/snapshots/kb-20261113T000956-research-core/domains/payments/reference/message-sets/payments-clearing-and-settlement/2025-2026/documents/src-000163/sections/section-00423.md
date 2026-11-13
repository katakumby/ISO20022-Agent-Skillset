---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.1 GroupHeader <GrpHdr>", "5.4.1.10 SettlementInformation <SttlmInf>", "5.4.1.10.1 SettlementMethod <SttlmMtd>"]
file_pages: [582]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.1.10.1 SettlementMethod <SttlmMtd>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 582 to 582.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 582

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
5.4.1.10.1  SettlementMethod <SttlmMtd>
Presence: [1..1]
Definition: Method used to settle the (batch of) payment instructions.
Datatype: "SettlementMethod1Code" on page 1237
CodeName Name Definition
INDA InstructedAgent Settlement is done by the agent
instructed to execute a payment
instruction.
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
582 March 2026
```

