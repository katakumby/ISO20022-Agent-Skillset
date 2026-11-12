---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.8 References69Choice", "35.1.14.8.1 SecuritiesSettlementTransactionConfirmationIdentification <SctiesSttlmTxConfId>"]
file_pages: [1490]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.8.1 SecuritiesSettlementTransactionConfirmationIdentification <SctiesSttlmTxConfId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1490 to 1490.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1490

```text
Constraints
• OtherMessageIdentificationUsageRule
If OtherMessageIdentification is used, then the message to be cancelled must not be one that can be
identified using of the message identification available in the choice list.
• SecuritiesSettlementTransactionAllegementNotificationRule
The SecuritiesMessageCancellationAdvice can be used to cancel a
SecuritiesSettlementTransactionAllegementNotification for two reasons:
- The message was sent by mistake
- The counterparty cancelled its instruction.
35.1.14.8.1  SecuritiesSettlementTransactionConfirmationIdentification <SctiesSttlmTxConfId>
Presence: [1..1]
Definition: Unambiguous identification of the confirmation to be cancelled.
SecuritiesSettlementTransactionConfirmationIdentification <SctiesSttlmTxConfId> contains the
following elements (see "SettlementTypeAndIdentification18" on page 1501 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [1..1] Text 1501
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1501
   Payment <Pmt> [1..1] CodeSet 1501
35.1.14.8.2  IntraPositionMovementConfirmationIdentification <IntraPosMvmntConfId>
Presence: [1..1]
Definition: Unambiguous account servicer identification of the intra-position movement confirmation to
be cancelled.
Datatype: "Max35Text" on page 2192
35.1.14.8.3  SecuritiesBalanceAccountingReportIdentification <SctiesBalAcctgRptId>
Presence: [1..1]
Definition: Unambiguous identification of the report message to be cancelled.
Datatype: "Max35Text" on page 2192
35.1.14.8.4  SecuritiesBalanceCustodyReportIdentification <SctiesBalCtdyRptId>
Presence: [1..1]
Definition: Unambiguous identification of the report message to be cancelled.
Datatype: "Max35Text" on page 2192
35.1.14.8.5  IntraPositionMovementPostingReportIdentification <IntraPosMvmntPstngRptId>
Presence: [1..1]
Definition: Identification of the intra-position movement posting report to be cancelled.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1490 March 2026
```

