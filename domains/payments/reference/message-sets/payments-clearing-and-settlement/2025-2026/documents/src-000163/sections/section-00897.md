---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.11 Miscellaneous", "10.1.11.5 NumberOfTransactionsPerStatus5"]
file_pages: [1192]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.11.5 NumberOfTransactionsPerStatus5

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1192 to 1192.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1192

```text
Definition: Purpose, in a proprietary form.
Datatype: "Max35Text" on page 1246
10.1.11.5  NumberOfTransactionsPerStatus5
Definition: Set of elements used to provide detailed information on the number of transactions that are
reported with a specific transaction status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DetailedNumberOfTransactions <DtldNbOfTxs> [1..1] Text 1192
   DetailedStatus <DtldSts> [1..1] CodeSet 1192
   DetailedControlSum <DtldCtrlSum> [0..1] Quantity 1192
10.1.11.5.1  DetailedNumberOfTransactions <DtldNbOfTxs>
Presence: [1..1]
Definition: Number of individual transactions contained in the message, detailed per status.
Datatype: "Max15NumericText" on page 1244
10.1.11.5.2  DetailedStatus <DtldSts>
Presence: [1..1]
Definition: Common transaction status for all individual transactions reported.
Datatype: "ExternalPaymentTransactionStatus1Code" on page 1231
10.1.11.5.3  DetailedControlSum <DtldCtrlSum>
Presence: [0..1]
Definition: Total of all individual amounts included in the message, irrespective of currencies, detailed
per status.
Datatype: "DecimalNumber" on page 1242
10.1.11.6  RemittanceInformation2
Definition: Information supplied to enable the matching of an entry with the items that the transfer is
intended to settle.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unstructured <Ustrd> [0..*] Text 1192
10.1.11.6.1  Unstructured <Ustrd>
Presence: [0..*]
Definition: Information supplied to enable the matching of an entry with the items that the transfer is
intended to settle, for example, commercial invoices in an accounts' receivable system in an
unstructured form.
Datatype: "Max140Text" on page 1244
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1192 March 2026
```

