---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "18.4 Message Building Blocks", "18.4.3.3 Rejected <Rjctd>"]
file_pages: [572]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.024.001.14"]
---

# 18.4.3.3 Rejected <Rjctd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 572 to 572.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 572

```text
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
18.4.3.3  Rejected <Rjctd>
Presence: [1..1]
Definition: Instruction/request has been rejected for further processing.
Rejected <Rjctd> contains one of the following elements (see "RejectionStatus39Choice" on
page 1930 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1930
Or}   Reason <Rsn> [1..*]  1931
     Code <Cd> [1..1]  1931
{Or       Code <Cd> [1..1] CodeSet 1931
Or}       Proprietary <Prtry> [1..1] ± 1933
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1933
18.4.3.4  Repair <Rpr>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer but is in repair.
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
18.4.3.5  Cancelled <Canc>
Presence: [1..1]
Definition: Instruction/request has been cancelled.
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 572 March 2026
```

