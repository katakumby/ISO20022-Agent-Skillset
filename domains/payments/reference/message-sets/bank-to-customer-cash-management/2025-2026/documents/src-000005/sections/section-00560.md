---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 camt.060.001.07 AccountReportingRequestV07", "5.4 Message Building Blocks", "5.4.2 ReportingRequest <RptgReq>", "5.4.2.7 ReportingSequence <RptgSeq>"]
file_pages: [793]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.060.001.07"]
---

# 5.4.2.7 ReportingSequence <RptgSeq>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 793 to 793.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 793

```text
5.4.2.7  ReportingSequence <RptgSeq>
Presence: [0..1]
Definition: Specifies the range of identification sequence numbers which are being requested.
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
5.4.2.8  RequestedTransactionType <ReqdTxTp>
Presence: [0..1]
Definition: Identifies the transactions to be reported.
RequestedTransactionType <ReqdTxTp> contains the following TransactionType2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1] ± 793
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 794
   FloorLimit <FlrLmt> [0..*]  794
     Amount <Amt> [1..1] Amount C1, C5 794
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 794
5.4.2.8.1  Status <Sts>
Presence: [1..1]
Definition: Specifies the status on the books of the account servicer of the transactions to be reported.
Status <Sts> contains one of the following elements (see "EntryStatus1Choice" on page 882 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 882
Or}   Proprietary <Prtry> [1..1] Text 882
Approved by the Payments SEG on 12 January 2026 camt.060.001.07 AccountReportingRequestV07
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
793 March 2026
```

