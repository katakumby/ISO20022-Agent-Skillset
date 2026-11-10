---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes", "6.2.3 CodeSet", "6.2.3.9 ClearingChannel2Code"]
file_pages: [590]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2.3.9 ClearingChannel2Code

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 590 to 590.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 590

```text
CodeName Name Definition
early payment from any bank under
subtraction of a discount. The ordering
customer's account is debited on value
date.
ELDR ElectronicDraft An instrument with a future value date
(do not pay before], which in commercial
terms is a 'negotiatable instrument': the
beneficiary can receive early payment
from any bank under subtraction of a
discount. The ordering customer's
account is debited on value date.
6.2.3.9  ClearingChannel2Code
Definition: Specifies the clearing channel for the routing of the transaction, as part of the payment type
identification.
Type: CodeSet
CodeName Name Definition
RTGS RealTimeGrossSettlementSystem Clearing channel is a real-time gross
settlement system.
RTNS RealTimeNetSettlementSystem Clearing channel is a real-time net
settlement system.
MPNS MassPaymentNetSystem Clearing channel is a mass payment net
settlement system.
BOOK BookTransfer Payment through internal book transfer.
6.2.3.10  CountryCode
Definition: Code to identify a country, a dependency, or another area of particular geopolitical interest,
on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).
Type: CodeSet
Format
pattern [A-Z]{2,2}
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
6.2.3.11  CreditDebitCode
Definition: Specifies if an operation is an increase or a decrease.
Type: CodeSet
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 590 March 2026
```

