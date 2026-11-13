---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.4 Payment <Pmt>", "5.4.2.1.3.2.1.4.7 PaymentMethod <PmtMtd>", "5.4.2.1.3.2.1.4.7.1 FINMessageType <FINMT>"]
file_pages: [293]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.4.7.1 FINMessageType <FINMT>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 293 to 293.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 293

```text
PaymentMethod <PmtMtd> contains one of the following PaymentOrigin1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FINMessageType <FINMT> [1..1] Text 293
Or   XMLMessageName <XMLMsgNm> [1..1] Text 293
Or   Proprietary <Prtry> [1..1] Text 293
Or}   Instrument <Instrm> [1..1] CodeSet 293
5.4.2.1.3.2.1.4.7.1  FINMessageType <FINMT>
Presence: [1..1]
Definition: Specifies that the payment was included in a SWIFT FIN format message, for example, MT
103.
Datatype: "Max3NumericText" on page 889
5.4.2.1.3.2.1.4.7.2  XMLMessageName <XMLMsgNm>
Presence: [1..1]
Definition: Specifies that the payment was included in a SWIFT XML message.
Datatype: "Max35Text" on page 889
5.4.2.1.3.2.1.4.7.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies that the payment was included in a proprietary format message.
Datatype: "Max35Text" on page 889
5.4.2.1.3.2.1.4.7.4  Instrument <Instrm>
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
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 293 February 2025
```

