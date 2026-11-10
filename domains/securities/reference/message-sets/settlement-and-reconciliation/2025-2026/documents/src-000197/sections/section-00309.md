---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "13.4 Message Building Blocks", "13.4.6 AccountOwner <AcctOwnr>", "13.4.7.8 ModificationProcessingStatus <ModPrcgSts>", "13.4.7.8.6 Modified <Modfd>", "13.4.7.8.6.2 Reason <Rsn>", "13.4.7.8.6.2.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [454]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.022.001.07"]
---

# 13.4.7.8.6.2.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 454 to 454.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 454

```text
13.4.7.8.6.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
13.4.7.8.7  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on page 1877
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 1878
   ProprietaryReason <PrtryRsn> [0..*] ± C1 1878
13.4.7.9  CancellationStatus <CxlSts>
Presence: [0..1]
Definition: Provides details on the processing status of the cancellation request.
CancellationStatus <CxlSts> contains one of the following ProcessingStatus86Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingCancellation <PdgCxl> [1..1] ± 454
Or   Rejected <Rjctd> [1..1] ± 455
Or   Repair <Rpr> [1..1] ± 455
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 455
Or   Proprietary <Prtry> [1..1] ± 456
Or   Denied <Dnd> [1..1] ± 456
Or}   Cancelled <Canc> [1..1] ± 456
13.4.7.9.1  PendingCancellation <PdgCxl>
Presence: [1..1]
Definition: The cancellation is pending processing.
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 454 March 2026
```

