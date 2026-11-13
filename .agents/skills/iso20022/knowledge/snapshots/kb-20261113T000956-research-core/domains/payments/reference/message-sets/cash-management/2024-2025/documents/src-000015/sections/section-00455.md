---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["23 camt.025.001.09 ReceiptV09", "23.4 Message Building Blocks", "23.4.2 ReceiptDetails <RctDtls>", "23.4.2.2 OriginalPaymentIdentification <OrgnlPmtId>", "23.4.2.2.4 LongBusinessIdentification <LngBizId>", "23.4.2.2.4.6 InstructingAgent <InstgAgt>"]
file_pages: [614]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.025.001.09"]
---

# 23.4.2.2.4.6 InstructingAgent <InstgAgt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 614 to 614.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 614

```text
Datatype: "PaymentInstrument1Code" on page 862
CodeName Name Definition
BDT BankDebitTransfer Direct debit instruction in which the
debtor and the creditor are financial
institutions.
BCT BankCreditTransfer Funds transfer in which the debtor and
the creditor are financial institutions.
CDT CustomerDebitTransfer Direct debit instruction in which the
debtor or the creditor or both are non-
financial institutions.
CCT CustomerCreditTransfer Funds transfer in which the debtor or the
creditor or both are non-financial
institutions.
CHK Cheque Payment instrument is a cheque. (A
written order on which instructions are
given to an account holder (a financial
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
23.4.2.2.4.6  InstructingAgent <InstgAgt>
Presence: [1..1]
Definition: Agent that instructs the next party in the chain to carry out the (set of) instruction(s).
Approved by the Payments SEG on 04 February 2025 camt.025.001.09 ReceiptV09
Cash Management - Maintenance 2024 - 2025 614 February 2025
```

