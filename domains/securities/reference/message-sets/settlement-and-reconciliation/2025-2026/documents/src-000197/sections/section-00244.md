---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.7.16 StatusAndReason <StsAndRsn>", "9.4.7.16.5 InstructionProcessingStatus <InstrPrcgSts>", "9.4.7.16.5.7 PendingCancellation <PdgCxl>", "9.4.7.16.5.7.2 Reason <Rsn>", "9.4.7.16.5.7.2.1 Code <Cd>", "9.4.7.16.5.7.2.1.1 Code <Cd>"]
file_pages: [359]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.7.16.5.7.2.1.1 Code <Cd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 359 to 359.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 359

```text
Code <Cd> contains one of the following PendingReason77Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 359
Or}   Proprietary <Prtry> [1..1] ± 359
9.4.7.16.5.7.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why a cancellation request sent for the related instruction is pending.
Datatype: "PendingReason32Code" on page 2105
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. It will be
managed as per the bilateral service
agreement between the account servicer
and account owner.
CONF AwaitingConfirmation Awaiting confirmation from the
counterparty.
CDCY ConditionalCurrency Execution is conditional to the execution
of a process linked to the currency of the
transaction.
CDRE ConditionalRealignement Execution is conditional to the execution
of a process of realignment at the issuer
CSD.
CDRG ConditionalRegistrar Execution is conditional to the execution
of a process at the registrar.
OTHR Other Other. See Narrative.
9.4.7.16.5.7.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason code why the instruction or request is pending, using a proprietary
format.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
9.4.7.16.5.7.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 359 March 2026
```

