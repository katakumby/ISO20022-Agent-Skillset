---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.1 ReversalPaymentInformationIdentification <RvslPmtInfId>"]
file_pages: [299]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.1 ReversalPaymentInformationIdentification <RvslPmtInfId>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 299 to 299.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 299

```text
On Condition
    /PaymentInformationReversal is present
 And    /PaymentInformationReversal is equal to value 'true'
Following Must be True
    /ReversalReasonInformation[*]/Reason Must be present
• PaymentInformationReversalAndTransactionInformationNotPresentRule
If PaymentInformationReversal is true, then TransactionInformation is not allowed.
On Condition
    /PaymentInformationReversal is present
 And    /PaymentInformationReversal is equal to value 'true'
Following Must be True
    /TransactionInformation[*] Must be absent
• PaymentInformationReversalAndTransactionInformationPresentRule
If PaymentInformationReversal is false, then at least one occurrence of TransactionInformation must
be present.
On Condition
    /PaymentInformationReversal is present
 And    /PaymentInformationReversal is equal to value 'false'
Following Must be True
    /TransactionInformation[*] Must be present
4.4.3.1  ReversalPaymentInformationIdentification <RvslPmtInfId>
Presence: [0..1]
Definition: Unique identification, as assigned by an instructing party for an instructed party, to
unambiguously identify the reversed payment information group.
Usage: The instructing party is the party sending the reversal message and not the party that sent the
original instruction that is being reversed.
Datatype: "Max35Text" on page 609
4.4.3.2  OriginalPaymentInformationIdentification <OrgnlPmtInfId>
Presence: [1..1]
Definition: Unique identification, as assigned by the original sending party, to unambiguously identify the
original payment information group.
Datatype: "Max35Text" on page 609
4.4.3.3  OriginalNumberOfTransactions <OrgnlNbOfTxs>
Presence: [0..1]
Definition: Number of individual transactions contained in the original payment information group.
Datatype: "Max15NumericText" on page 608
4.4.3.4  OriginalControlSum <OrgnlCtrlSum>
Presence: [0..1]
Definition: Total of all individual amounts included in the original payment information group,
irrespective of currencies.
Datatype: "DecimalNumber" on page 606
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 299 March 2026
```

