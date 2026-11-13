---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.3 PaymentSearch <PmtSch>", "4.4.2.2.2.2.3.10 PaymentMethod <PmtMtd>", "4.4.2.2.2.2.3.10.2 XMLMessageName <XMLMsgNm>"]
file_pages: [162]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.3.10.2 XMLMessageName <XMLMsgNm>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 162 to 162.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 162

```text
Datatype: "Max3NumericText" on page 889
4.4.2.2.2.2.3.10.2  XMLMessageName <XMLMsgNm>
Presence: [1..1]
Definition: Specifies that the payment was included in a SWIFT XML message.
Datatype: "Max35Text" on page 889
4.4.2.2.2.2.3.10.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies that the payment was included in a proprietary format message.
Datatype: "Max35Text" on page 889
4.4.2.2.2.2.3.10.4  Instrument <Instrm>
Presence: [1..1]
Definition: Specifies the type of payment when not included in a SWIFT or proprietary format.
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
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 162 February 2025
```

