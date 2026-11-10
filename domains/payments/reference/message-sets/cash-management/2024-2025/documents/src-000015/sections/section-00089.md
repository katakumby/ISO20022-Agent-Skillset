---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.3 PaymentSearch <PmtSch>", "4.4.2.2.2.2.3.4 Status <Sts>", "4.4.2.2.2.2.3.4.1 PaymentInstructionStatus <PmtInstrSts>", "4.4.2.2.2.2.3.4.1.2 FinalStatus <FnlSts>"]
file_pages: [158]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.3.4.1.2 FinalStatus <FnlSts>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 158 to 158.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 158

```text
CodeName Name Definition
INVD Invalid Transaction is invalid.
UMAC Unmatched Clearing agent attempted to match the
transaction with a corresponding
transaction but failed.
STLE SettlementEligible Transaction is eligible for future
settlement.
STLM SettlementMature Transaction is eligible for immediate
settlement.
SSPD Suspended Transaction has been suspended by the
clearing agent.
PCAN PendingCancellation Clearing agent has received a
cancellation request for the transaction,
and needs either a matching request for
cancellation from the counterparty or a
confirmation from an authorised party.
PSTL PendingSettlement Transaction is eligible for settlement, but
is pending.
PFST PendingFailingSettlement Transaction eligible for immediate
settlement, has failed to settle.
SMLR SenderMultilateralLimitRelated Transaction causes the 'Sender
multilateral limit' to be exceeded and
cannot currently be processed.
RMLR ReceiverMultilateralLimitRelated Transaction causes the 'Receiver
multilateral limit' to be exceeded and
cannot currently be processed.
SRBL SenderReceiverBilateralLimitRelated Transaction causes the bilateral limit
fixed between Sender and Receiver to
be exceeded and cannot currently be
processed.
AVLB HeldForServiceAvailability Specifies that the message is queued to
the receiving payment system and is
awaiting processing because the
receiving payment system is not
operational (open) at that point in time.
SRML SenderReceiverMultilateralLimitRelated Transaction causes the multilateral limits
fixed between Sender and Receiver to
be exceeded by the total amount of
submitted payments at the end of the
day and cannot currently be processed.
4.4.2.2.2.2.3.4.1.2  FinalStatus <FnlSts>
Presence: [1..1]
Definition: Qualifies further the final status.
Datatype: "FinalStatusCode" on page 858
CodeName Name Definition
STLD Settled Transaction has been successfully
processed by the clearing agent.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 158 February 2025
```

