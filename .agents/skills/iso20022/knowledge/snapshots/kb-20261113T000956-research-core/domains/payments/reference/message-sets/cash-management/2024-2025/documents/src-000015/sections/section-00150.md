---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.1 PaymentCommonInformation <PmtCmonInf>", "5.4.2.1.1.3 CommonStatus <CmonSts>", "5.4.2.1.1.3.3 Reason <Rsn>", "5.4.2.1.1.3.3.7 Proprietary <Prtry>"]
file_pages: [248]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.1.3.3.7 Proprietary <Prtry>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 248 to 248.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 248

```text
5.4.2.1.1.3.3.7  Proprietary <Prtry>
Presence: [1..1]
Definition: Defines a free text proprietary reason.
Datatype: "Max35Text" on page 889
5.4.2.1.1.4  RequestedExecutionDate <ReqdExctnDt>
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
5.4.2.1.1.5  EntryDate <NtryDt>
Presence: [0..1]
Definition: Date and time at which an entry is posted to an account on the account servicer's books.
EntryDate <NtryDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 801 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 801
Or}   DateTime <DtTm> [1..1] DateTime 801
5.4.2.1.1.6  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the payment instruction is a debit or a credit.
.
Datatype: "CreditDebitCode" on page 851
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
5.4.2.1.1.7  PaymentMethod <PmtMtd>
Presence: [0..1]
Definition: Indicates the message or event from which an instruction has been initiated.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 248 February 2025
```

