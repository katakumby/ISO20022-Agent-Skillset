---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.10 MandateRelatedInformation <MndtRltdInf>", "4.4.3.8.9.10.1 DirectDebitMandate <DrctDbtMndt>", "4.4.3.8.9.10.1.9 Reason <Rsn>", "4.4.3.8.9.10.1.9.1 Code <Cd>"]
file_pages: [345]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.10.1.9.1 Code <Cd>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 345 to 345.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 345

```text
Definition: Reason for the direct debit mandate to allow the user to distinguish between different
mandates for the same creditor.
Reason <Rsn> contains one of the following MandateSetupReason1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 345
Or}   Proprietary <Prtry> [1..1] Text 345
4.4.3.8.9.10.1.9.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the mandate setup, as published in an external reason code list.
Datatype: "ExternalMandateSetupReason1Code" on page 595
4.4.3.8.9.10.1.9.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the mandate setup, in a proprietary form.
Datatype: "Max70Text" on page 610
4.4.3.8.9.10.1.10  TrackingDays <TrckgDays>
Presence: [0..1]
Definition: Specifies the number of days the direct debit instruction must be tracked.
Datatype: "Exact2NumericText" on page 607
4.4.3.8.9.10.2  CreditTransferMandate <CdtTrfMndt>
Presence: [1..1]
Definition: Specific credit transfer mandate data.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 345 March 2026
```

