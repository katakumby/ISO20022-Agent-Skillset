---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.4 Message Building Blocks", "9.4.1 GroupHeader <GrpHdr>", "9.4.3.11 OriginalTransactionReference <OrgnlTxRef>", "9.4.3.11.7 SettlementInformation <SttlmInf>", "9.4.3.11.7.1 SettlementMethod <SttlmMtd>"]
file_pages: [1082]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
---

# 9.4.3.11.7.1 SettlementMethod <SttlmMtd>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1082 to 1082.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1082

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
9.4.3.11.7.1  SettlementMethod <SttlmMtd>
Presence: [1..1]
Definition: Method used to settle the (batch of) payment instructions.
Datatype: "SettlementMethod1Code" on page 1237
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1082 March 2026
```

