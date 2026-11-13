---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.11 Miscellaneous"]
file_pages: [552]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.11 Miscellaneous

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 552 to 552.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 552

```text
Classification <Clssfctn> contains one of the following elements (see "MandateClassification1Choice"
on page 549 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 549
Or}   Proprietary <Prtry> [1..1] Text 549
6.1.11 Miscellaneous
6.1.11.1  NumberOfTransactionsPerStatus5
Definition: Set of elements used to provide detailed information on the number of transactions that are
reported with a specific transaction status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DetailedNumberOfTransactions <DtldNbOfTxs> [1..1] Text 552
   DetailedStatus <DtldSts> [1..1] CodeSet 552
   DetailedControlSum <DtldCtrlSum> [0..1] Quantity 552
6.1.11.1.1  DetailedNumberOfTransactions <DtldNbOfTxs>
Presence: [1..1]
Definition: Number of individual transactions contained in the message, detailed per status.
Datatype: "Max15NumericText" on page 608
6.1.11.1.2  DetailedStatus <DtldSts>
Presence: [1..1]
Definition: Common transaction status for all individual transactions reported.
Datatype: "ExternalPaymentTransactionStatus1Code" on page 596
6.1.11.1.3  DetailedControlSum <DtldCtrlSum>
Presence: [0..1]
Definition: Total of all individual amounts included in the message, irrespective of currencies, detailed
per status.
Datatype: "DecimalNumber" on page 606
6.1.11.2  Authorisation1Choice
Definition: Provides the details on the user identification or any user key that allows to check if the
initiating party is allowed to issue the transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 553
Or}   Proprietary <Prtry> [1..1] Text 553
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 552 March 2026
```

