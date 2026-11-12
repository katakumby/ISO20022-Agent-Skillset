---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11", "28.4 Message Building Blocks", "28.4.2 ProcessingStatus <PrcgSts>", "28.4.2.5 Repair <Rpr>"]
file_pages: [967]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.034.001.11"]
---

# 28.4.2.5 Repair <Rpr>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 967 to 967.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 967

```text
Definition: Instruction/Request has been rejected for further processing.
Rejected <Rjctd> contains one of the following elements (see "RejectionStatus36Choice" on
page 1995 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1995
Or}   Reason <Rsn> [1..*]  1995
     Code <Cd> [1..1]  1995
{Or       Code <Cd> [1..1] CodeSet 1996
Or}       Proprietary <Prtry> [1..1] ± 1998
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1998
28.4.2.5  Repair <Rpr>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer but is in repair.
Repair <Rpr> contains one of the following elements (see "RepairStatus14Choice" on page 1945 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1945
Or}   Reason <Rsn> [1..*]  1945
     Code <Cd> [1..1] ± 1945
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1946
28.4.2.6  Cancelled <Canc>
Presence: [1..1]
Definition: Instruction has been cancelled (only as a response to a SecuritiesTransactionStatusQuery).
The status on the processing of a cancellation request must be provided using a
SecuritiesTransactionCancellationRequestStatusAdvice.
Cancelled <Canc> contains one of the following elements (see "CancellationStatus16Choice" on
page 1973 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1974
Or}   Reason <Rsn> [1..*]  1974
     Code <Cd> [1..1] ± 1974
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1974
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 967 March 2026
```

