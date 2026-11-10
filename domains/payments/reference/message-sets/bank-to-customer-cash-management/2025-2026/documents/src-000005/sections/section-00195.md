---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.2 StatementPagination <StmtPgntn>"]
file_pages: [302]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.2 StatementPagination <StmtPgntn>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 302 to 302.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 302

```text
3.4.2.2  StatementPagination <StmtPgntn>
Presence: [0..1]
Definition: Provides details on the page number of the statement.
Usage: The pagination of the statement is only allowed when agreed between the parties.
StatementPagination <StmtPgntn> contains the following elements (see "Pagination1" on page 844
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 844
   LastPageIndicator <LastPgInd> [1..1] Indicator 845
3.4.2.3  ElectronicSequenceNumber <ElctrncSeqNb>
Presence: [0..1]
Definition: Sequential number of the statement, as assigned by the account servicer.
Usage: The sequential number is increased incrementally for each statement sent electronically.
Datatype: "Number" on page 912
3.4.2.4  ReportingSequence <RptgSeq>
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
3.4.2.5  LegalSequenceNumber <LglSeqNb>
Presence: [0..1]
Definition: Legal sequential number of the statement, as assigned by the account servicer. It is
increased incrementally for each statement sent.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
302 March 2026
```

