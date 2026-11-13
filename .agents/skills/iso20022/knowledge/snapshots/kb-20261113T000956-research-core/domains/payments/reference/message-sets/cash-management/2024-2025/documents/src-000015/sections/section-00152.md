---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.2 TransactionsSummary <TxsSummry>"]
file_pages: [250]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.2 TransactionsSummary <TxsSummry>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 250 to 250.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 250

```text
CodeName Name Definition
institution) to pay a stated sum to a
named recipient (the payee)).
BKT BookTransfer Transfer that is a movement of cash on
the books of the account servicer.
DCP DebitCardPayment Payment instrument is a debit card. (The
payment originated using a debit card
scheme.).
CCP CreditCardPayment Payment instrument is a credit card.
(The payment originated using a credit
card scheme.).
RTI Return Entry related to a returned or unpaid
item.
CAN CancellationRequest Reverse entry that is the result of the
cancellation of a previously booked
entry.
5.4.2.1.2  TransactionsSummary <TxsSummry>
Presence: [0..1]
Definition: Indicates the total number and sum of the transactions.
Impacted by: C11 "DebitCreditIndicatorGuideline"
TransactionsSummary <TxsSummry> contains the following NumberAndSumOfTransactions2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NumberOfEntries <NbOfNtries> [0..1] Text 250
   Sum <Sum> [0..1] Quantity 250
   TotalNetEntryAmount <TtlNetNtryAmt> [0..1] Quantity 251
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 251
Constraints
• DebitCreditIndicatorGuideline
DebitCreditIndicator should be present when TotalNetEntryAmount is present.
5.4.2.1.2.1  NumberOfEntries <NbOfNtries>
Presence: [0..1]
Definition: Number of individual entries included in the report.
Datatype: "Max15NumericText" on page 888
5.4.2.1.2.2  Sum <Sum>
Presence: [0..1]
Definition: Total of all individual entries included in the report.
Datatype: "DecimalNumber" on page 886
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 250 February 2025
```

