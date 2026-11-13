---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.2 NotificationPagination <NtfctnPgntn>"]
file_pages: [562]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.2 NotificationPagination <NtfctnPgntn>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 562 to 562.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 562

```text
4.4.2.2  NotificationPagination <NtfctnPgntn>
Presence: [0..1]
Definition: Provides details on the page number of the notification.
Usage: The pagination of the notification is only allowed when agreed between the parties.
NotificationPagination <NtfctnPgntn> contains the following elements (see "Pagination1" on
page 844 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 844
   LastPageIndicator <LastPgInd> [1..1] Indicator 845
4.4.2.3  ElectronicSequenceNumber <ElctrncSeqNb>
Presence: [0..1]
Definition: Sequential number of the notification, as assigned by the account servicer.
Usage: The sequential number is increased incrementally for each notification sent electronically.
Datatype: "Number" on page 912
4.4.2.4  ReportingSequence <RptgSeq>
Presence: [0..1]
Definition: Specifies the range of identification sequence numbers, as provided in the request.
ReportingSequence <RptgSeq> contains one of the following elements (see
"SequenceRange1Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromSequence <FrSeq> [1..1] Text 843
Or   ToSequence <ToSeq> [1..1] Text 843
Or   FromToSequence <FrToSeq> [1..*]  844
     FromSequence <FrSeq> [1..1] Text 844
     ToSequence <ToSeq> [1..1] Text 844
Or   EqualSequence <EQSeq> [1..*] Text 844
Or}   NotEqualSequence <NEQSeq> [1..*] Text 844
4.4.2.5  LegalSequenceNumber <LglSeqNb>
Presence: [0..1]
Definition: Legal sequential number of the notification, as assigned by the account servicer. It is
increased incrementally for each notification sent.
Datatype: "Number" on page 912
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
562 March 2026
```

