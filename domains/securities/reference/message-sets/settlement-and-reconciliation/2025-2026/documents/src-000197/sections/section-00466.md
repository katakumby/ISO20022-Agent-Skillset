---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09", "21.4 Message Building Blocks", "21.4.3 ProcessingStatus <PrcgSts>"]
file_pages: [714]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.027.001.09"]
---

# 21.4.3 ProcessingStatus <PrcgSts>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 714 to 714.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 714

```text
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
21.4.3 ProcessingStatus <PrcgSts>
Presence: [1..1]
Definition: Provides details on the processing status of the request.
ProcessingStatus <PrcgSts> contains one of the following ProcessingStatus105Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingCancellation <PdgCxl> [1..1] ± 714
Or   Rejected <Rjctd> [1..1] ± 714
Or   Repair <Rpr> [1..1] ± 715
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 715
Or   Proprietary <Prtry> [1..1] ± 715
Or   Denied <Dnd> [1..1] ± 716
Or}   Cancelled <Canc> [1..1] ± 716
21.4.3.1  PendingCancellation <PdgCxl>
Presence: [1..1]
Definition: Cancellation is pending processing.
PendingCancellation <PdgCxl> contains one of the following elements (see
"PendingStatus82Choice" on page 2017 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2018
Or}   Reason <Rsn> [1..*]  2018
     Code <Cd> [1..1] ± 2018
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2018
21.4.3.2  Rejected <Rjctd>
Presence: [1..1]
Definition: Instruction/Request has been rejected for further processing.
Approved by the Securities SEG on 27 January 2026 sese.027.001.09
SecuritiesTransactionCancellationRequestStatusAd
viceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 714 March 2026
```

