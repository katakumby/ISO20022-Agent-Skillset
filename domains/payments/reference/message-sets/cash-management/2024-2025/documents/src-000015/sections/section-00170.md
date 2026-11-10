---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.4 Payment <Pmt>", "5.4.2.1.3.2.1.4.1 MessageIdentification <MsgId>"]
file_pages: [280]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.4.1 MessageIdentification <MsgId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 280 to 280.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 280

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       Party <Pty> [1..1] ± 311
Or}       Agent <Agt> [1..1] ± 312
     UltimateCreditor <UltmtCdtr> [0..1]  313
{Or       Party <Pty> [1..1] ± 313
Or}       Agent <Agt> [1..1] ± 314
5.4.2.1.3.2.1.4.1  MessageIdentification <MsgId>
Presence: [0..1]
Definition: Point to point reference, as assigned by the original initiating party, to unambiguously identify
the original payment transaction message
Usage: this is the former TransactionReference.
Datatype: "Max35Text" on page 889
5.4.2.1.3.2.1.4.2  RequestedExecutionDate <ReqdExctnDt>
Presence: [0..1]
Definition: Date and time at which the cash is at the disposal of the credit account owner, or ceases to
be at the disposal of the debit account owner.
RequestedExecutionDate <ReqdExctnDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 801 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 801
Or}   DateTime <DtTm> [1..1] DateTime 801
5.4.2.1.3.2.1.4.3  Status <Sts>
Presence: [0..*]
Definition: Detailed information about the status of a transfer.
.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 280 February 2025
```

