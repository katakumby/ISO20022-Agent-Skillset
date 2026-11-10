---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.7.16 StatusAndReason <StsAndRsn>", "9.4.7.16.5 InstructionProcessingStatus <InstrPrcgSts>", "9.4.7.16.5.1 PendingProcessing <PdgPrcg>", "9.4.7.16.5.1.2 Reason <Rsn>", "9.4.7.16.5.1.2.1 Code <Cd>", "9.4.7.16.5.1.2.1.2 Proprietary <Prtry>"]
file_pages: [355]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.7.16.5.1.2.1.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 355 to 355.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 355

```text
CodeName Name Definition
CERT WrongCertificatesNumbers Certificate number error.
NEXT NextProcess Next process is launched. No processing
pending problems to be reported.
PRSY SystemOnHold Transaction was put on hold/frozen by
the system.
CSDH CSDHold Central securities depository sets the
instruction in a hold/frozen/preadvice
mode.
CDEL ConditionalDelivery Instruction is in a hold/frozen/preadvice
mode as it fulfils predefined conditional
delivery rules in the market infrastructure
platform for conditional delivery.
CVAL CSDValidation Instruction is in a hold/frozen/preadvice
mode as it fulfils predefined conditions of
a restriction processing type in the
market infrastructure platform.
CDLR ConditionalDeliveryAwaitingRelease Instruction is in a hold/frozen/preadvice
mode. Market infrastructure platform is
awaiting release.
INBC IncompleteNumberCount Not all the instructions part of a pool
have been received.
CDAC ConditionalDeliveryAwaitingCancellation Awaiting cancellation of one of the party.
9.4.7.16.5.1.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending processing status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
9.4.7.16.5.1.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
9.4.7.16.5.2  CancellationRequested <CxlReqd>
Presence: [1..1]
Definition: Cancellation request from your counterparty for this transaction is pending waiting for your
cancellation request.
Impacted by: C4 "AdditionalReasonInforrmationRule"
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 355 March 2026
```

