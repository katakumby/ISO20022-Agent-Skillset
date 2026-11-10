---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Direct Debit", "PaymentReturn with Direct Debit"]
content_origin: "source-transcription"
---

# PaymentReturn with Direct Debit

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Direct Debit / PaymentReturn with Direct Debit.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P535** PaymentReturn with Direct Debit

**P536**  A PaymentReturn message is initiated by the debtor agent and sent to the previous party in the payment chain when a debit cannot be executed due to an administrative reason (for example non existing/closed account) or due to a banking reason (for example insufficient funds).

**P537** The PaymentReturn message is also the message to be used by the debtor agent following the receipt of a refund request by the debtor (out of scope) as it is assumed that the refund request will be done through a non-automated tool (for example phone/fax) and is not part of the scope.

**P538** In this case, the PaymentReturn message will contain a code to indicate that it is triggered by a request for refund by the debtor. 

