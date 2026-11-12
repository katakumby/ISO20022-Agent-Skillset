---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.2 CodeSet", "37.2.2.40 PaymentInstrument1Code"]
file_pages: [862]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.2.40 PaymentInstrument1Code

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 862 to 862.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 862

```text
CodeName Name Definition
MIKS GenderNeutral Title of the person is gender neutral
(Mx).
37.2.2.40  PaymentInstrument1Code
Definition: Specifies the payment instrument used or the underlying financial transaction that resulted in
a payment transaction.
Type: CodeSet
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
37.2.2.41  PaymentRole1Code
Definition: Role associated with a specific party in relation to a payment instruction. The role identifies
either the specific function of the party, or the party's rights regarding management of the instruction.
Type: CodeSet
CodeName Name Definition
LQMG LiquidityManager Party in a financial institution responsible
for the management of liquidity for the
financial institution. This party has
access to some functions available on
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 862 February 2025
```

