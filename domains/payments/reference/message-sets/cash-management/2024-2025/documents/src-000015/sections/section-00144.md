---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.1 PaymentCommonInformation <PmtCmonInf>", "5.4.2.1.1.3 CommonStatus <CmonSts>", "5.4.2.1.1.3.1 Code <Cd>", "5.4.2.1.1.3.1.1 Pending <Pdg>"]
file_pages: [238]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.1.3.1.1 Pending <Pdg>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 238 to 238.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 238

```text
5.4.2.1.1.3.1.1  Pending <Pdg>
Presence: [1..1]
Definition: Qualifies further the pending status.
Datatype: "PendingStatus4Code" on page 869
CodeName Name Definition
ACPD Accepted Transaction has been accepted by the
clearing agent.
VALD Validated Transaction has been validated by the
clearing agent.
MATD Matched Transaction has been matched with a
corresponding transaction by the
clearing agent.
AUTD Authorised Transaction has been authorised by the
transaction administrator or authorised
party.
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
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 238 February 2025
```

