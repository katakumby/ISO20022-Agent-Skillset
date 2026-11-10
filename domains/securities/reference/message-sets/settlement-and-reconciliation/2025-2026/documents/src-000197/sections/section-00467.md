---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09", "21.4 Message Building Blocks", "21.4.3 ProcessingStatus <PrcgSts>", "21.4.3.3 Repair <Rpr>"]
file_pages: [715]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.027.001.09"]
---

# 21.4.3.3 Repair <Rpr>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 715 to 715.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 715

```text
Rejected <Rjctd> contains one of the following elements (see "RejectionOrRepairStatus43Choice" on
page 1951 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1952
Or}   Reason <Rsn> [1..*]  1952
     Code <Cd> [1..1] ± 1952
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1952
21.4.3.3  Repair <Rpr>
Presence: [1..1]
Definition: Instruction/Request is accepted but in repair.
Repair <Rpr> contains one of the following elements (see "RejectionOrRepairStatus42Choice" on
page 1919 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1919
Or}   Reason <Rsn> [1..*]  1919
     Code <Cd> [1..1] ± 1920
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1920
21.4.3.4  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus24Choice" on page 1983 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1983
Or}   Reason <Rsn> [1..*]  1983
     Code <Cd> [1..1] ± 1983
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1984
21.4.3.5  Proprietary <Prtry>
Presence: [1..1]
Definition: Status that cannot be reported using one of the available standard status.
Approved by the Securities SEG on 27 January 2026 sese.027.001.09
SecuritiesTransactionCancellationRequestStatusAd
viceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 715 March 2026
```

