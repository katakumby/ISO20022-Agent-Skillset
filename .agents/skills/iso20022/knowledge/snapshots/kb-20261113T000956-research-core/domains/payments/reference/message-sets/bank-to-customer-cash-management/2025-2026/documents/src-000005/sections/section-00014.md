---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.2 ReportPagination <RptPgntn>"]
file_pages: [43]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.2 ReportPagination <RptPgntn>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 43 to 43.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 43

```text
2.4.2.2  ReportPagination <RptPgntn>
Presence: [0..1]
Definition: Provides details on the page number of the report.
Usage: The pagination of the report is only allowed when agreed between the parties.
ReportPagination <RptPgntn> contains the following elements (see "Pagination1" on page 844 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 844
   LastPageIndicator <LastPgInd> [1..1] Indicator 845
2.4.2.3  ElectronicSequenceNumber <ElctrncSeqNb>
Presence: [0..1]
Definition: Sequential number of the report, as assigned by the account servicer.
Usage: The sequential number is increased incrementally for each report sent electronically.
Datatype: "Number" on page 912
2.4.2.4  ReportingSequence <RptgSeq>
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
2.4.2.5  LegalSequenceNumber <LglSeqNb>
Presence: [0..1]
Definition: Legal sequential number of the report, as assigned by the account servicer. It is increased
incrementally for each report sent.
Datatype: "Number" on page 912
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
43 March 2026
```

