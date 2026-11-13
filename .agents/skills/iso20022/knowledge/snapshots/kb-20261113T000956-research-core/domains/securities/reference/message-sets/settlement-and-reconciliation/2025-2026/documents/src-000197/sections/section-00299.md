---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "13.4 Message Building Blocks", "13.4.6 AccountOwner <AcctOwnr>", "13.4.7.4 ProcessingStatus <PrcgSts>", "13.4.7.4.5 Cancelled <Canc>"]
file_pages: [444]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.022.001.07"]
---

# 13.4.7.4.5 Cancelled <Canc>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 444 to 444.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 444

```text
Repair <Rpr> contains one of the following elements (see "RepairStatus12Choice" on page 2010 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2011
Or}   Reason <Rsn> [1..*]  2011
     Code <Cd> [1..1]  2011
{Or       Code <Cd> [1..1] CodeSet 2011
Or}       Proprietary <Prtry> [1..1] ± 2013
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2013
13.4.7.4.5  Cancelled <Canc>
Presence: [1..1]
Definition: Instruction has been cancelled.
Cancelled <Canc> contains one of the following elements (see "CancellationStatus24Choice" on
page 1922 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1922
Or}   Reason <Rsn> [1..*]  1923
     Code <Cd> [1..1]  1923
{Or       Code <Cd> [1..1] CodeSet 1923
Or}       Proprietary <Prtry> [1..1] ± 1924
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1924
13.4.7.4.6  PendingCancellation <PdgCxl>
Presence: [1..1]
Definition: Cancellation request from yourself for this instruction is pending waiting for further
processing.
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 444 March 2026
```

