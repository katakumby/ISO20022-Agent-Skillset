---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.1 OriginalPaymentInformationIdentification <OrgnlPmtInfId>"]
file_pages: [161]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.1 OriginalPaymentInformationIdentification <OrgnlPmtInfId>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 161 to 161.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 161

```text
• PaymentInformationStatusReceivedRule
If OriginalPaymentInformationAndStatus/PaymentInformationStatus is present and is equal to RCVD
(Received), then TransactionInformationAndStatus/TransactionStatus is not allowed.
On Condition
    /PaymentInformationStatus is present
 And    /PaymentInformationStatus is within DataType <<Code>> 
ValidationRuleReceived1Code
 And    /TransactionInformationAndStatus[1] is present
Following Must be True
    /TransactionInformationAndStatus[*]/TransactionStatus Must be absent
• PaymentInformationStatusRejectedRule
If OriginalPaymentInformationAndStatus/PaymentInformationStatus is present and is equal to RJCT
(Rejceted), then TransactionInformationAndStatus/TransactionStatus, if present, must be equal to
RJCT (Rejected).
On Condition
    /PaymentInformationStatus is present
 And    /PaymentInformationStatus is within DataType <<Code>> 
ValidationRuleRejected1Code
 And    /TransactionInformationAndStatus[*]/TransactionStatus is present
Following Must be True
    /TransactionInformationAndStatus[*]/TransactionStatus Must be within DataType 
<<Code>> ValidationRuleRejected1Code
3.4.3.1  OriginalPaymentInformationIdentification <OrgnlPmtInfId>
Presence: [1..1]
Definition: Unique identification, as assigned by the original sending party, to unambiguously identify the
original payment information group.
Datatype: "Max35Text" on page 609
3.4.3.2  OriginalNumberOfTransactions <OrgnlNbOfTxs>
Presence: [0..1]
Definition: Number of individual transactions contained in the original payment information group.
Datatype: "Max15NumericText" on page 608
3.4.3.3  OriginalControlSum <OrgnlCtrlSum>
Presence: [0..1]
Definition: Total of all individual amounts included in the original payment information group,
irrespective of currencies.
Datatype: "DecimalNumber" on page 606
3.4.3.4  PaymentInformationStatus <PmtInfSts>
Presence: [0..1]
Definition: Specifies the status of the payment information group.
Datatype: "ExternalPaymentGroupStatus1Code" on page 595
3.4.3.5  StatusReasonInformation <StsRsnInf>
Presence: [0..*]
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 161 March 2026
```

