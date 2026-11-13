---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks"]
file_pages: [283]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
preceding_topic_continuations: [{"constraint_ids": ["C24", "C25", "C26", "C27", "C28", "C29", "C30", "C31", "C32"], "until_heading": "4.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 283, "topic": "4.3 Constraints", "reference_path": "domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000174/sections/section-00196.md"}]
---

# 4.4 Message Building Blocks

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 283 to 283.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 283, C24–C32 before **4.4 Message Building Blocks** continue [4.3 Constraints](section-00196.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 283

```text
C24 RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
C25 SettlementMethodAgentRule
If SettlementMethod is equal to INDA or INGA, then ReimbursementAgent(s) and
ClearingSystem are not allowed.
C26 SettlementMethodClearingRule
If SettlementMethod is equal to CLRG, then SettlementAccount and ReimbursementAgent(s)
are not allowed.
C27 SettlementMethodCoverAgentRule
If SettlementMethod is equal to COVE, then InstructedReimbursementAgent or
InstructingReimbursementAgent must be present.
C28 SettlementMethodCoverRule
If SettlementMethod is equal to COVE, then SettlementAccount and ClearingSystem are not
allowed.
C29 SupplementaryDataRule
The SupplementaryData building block at message level must not be used to provide additional
information about a transaction. The SupplementaryData element at transaction level should be
used for that purpose.
This constraint is defined at the MessageDefinition level.
C30 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C31 ThirdReimbursementAgentAccountRule
If ThirdReimbursementAgentAccount is present, then ThirdReimbursementAgent must be
present.
C32 ThirdReimbursementAgentRule
If ThirdReimbursementAgent is present, then InstructingReimbursementAgent and
InstructedReimbursementAgent must both be present.
4.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
4.4.1 GroupHeader <GrpHdr>
Presence: [1..1]
Definition: Set of characteristics shared by all individual transactions included in the message.
Impacted by: C7 "ControlSumAndGroupReversalRule", C12
"GroupReversalAndNumberOfTransactionsGuideline"
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 283 March 2026
```

