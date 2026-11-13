---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.4 Payment <Pmt>", "5.4.2.1.3.2.1.4.3 Status <Sts>", "5.4.2.1.3.2.1.4.3.1 Code <Cd>", "5.4.2.1.3.2.1.4.3.1.2 Final <Fnl>"]
file_pages: [283]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.4.3.1.2 Final <Fnl>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 283 to 283.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 283

```text
5.4.2.1.3.2.1.4.3.1.2  Final <Fnl>
Presence: [1..1]
Definition: Qualifies further the final status.
Datatype: "FinalStatus1Code" on page 857
CodeName Name Definition
STLD Settled Transaction has been successfully
processed by the clearing agent.
RJTD Rejected Transaction has been rejected by the
clearing agent.
CAND Cancelled Transaction has been cancelled.
FNLD Finalised Transaction has been successfully
processed by the clearing agent.
Settlement will take place outside of the
system.
5.4.2.1.3.2.1.4.3.1.3  RTGS <RTGS>
Presence: [1..1]
Definition: Qualifies further the RTGS status.
Datatype: "Max4AlphaNumericText" on page 890
5.4.2.1.3.2.1.4.3.1.4  Settlement <Sttlm>
Presence: [1..1]
Definition: Qualifies further the settlement status.
Datatype: "Max4AlphaNumericText" on page 890
5.4.2.1.3.2.1.4.3.1.5  Proprietary <Prtry>
Presence: [1..1]
Definition: Qualifies further the proprietary status.
Datatype: "Max35Text" on page 889
5.4.2.1.3.2.1.4.3.2  DateTime <DtTm>
Presence: [0..1]
Definition: Date and time at which the status was assigned to the transfer.
DateTime <DtTm> contains one of the following elements (see "DateAndDateTime2Choice" on
page 801 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 801
Or}   DateTime <DtTm> [1..1] DateTime 801
5.4.2.1.3.2.1.4.3.3  Reason <Rsn>
Presence: [0..*]
Definition: Reason provided for the status of a transfer.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 283 February 2025
```

