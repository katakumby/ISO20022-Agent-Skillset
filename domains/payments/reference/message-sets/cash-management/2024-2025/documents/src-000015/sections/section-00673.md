---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.2 CodeSet", "37.2.2.4 BalanceCounterparty1Code"]
file_pages: [850]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.2.4 BalanceCounterparty1Code

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 850 to 850.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 850

```text
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
37.2.2.4  BalanceCounterparty1Code
Definition: Specifies the type of counterparty to be taken into account for calculation of the balance.
Type: CodeSet
CodeName Name Definition
BILA Bilateral Balance calculated regarding one
member in the system.
MULT Multilateral Balance calculated regarding all
members in the system.
37.2.2.5  BalanceStatus1Code
Definition: Specifies the balance of transactions with a certain status.
Type: CodeSet
CodeName Name Definition
PDNG Pending Balance corresponding to the pending
transactions.
STLD Settled Final status of a transaction when the
associated transfer of cash has been
successfully processed.
37.2.2.6  CancelledStatusReason1Code
Definition: Specifies the underlying reason for cancellation of the associated transaction.
Type: CodeSet
CodeName Name Definition
CANI CancelledByYourself Transaction is cancelled by yourself.
CANS CancelledBySystem Transaction is cancelled by the system.
CSUB CancelledByAgent Transaction is cancelled by the agent.
37.2.2.7  CashPaymentStatus2Code
Definition: Specifies the state of a payment instruction at a specified time.
Type: CodeSet
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 850 February 2025
```

