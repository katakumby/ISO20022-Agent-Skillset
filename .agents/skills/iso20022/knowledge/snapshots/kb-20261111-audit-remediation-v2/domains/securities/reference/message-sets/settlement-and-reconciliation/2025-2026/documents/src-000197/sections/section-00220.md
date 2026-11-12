---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.7.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>"]
file_pages: [329]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.7.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 329 to 329.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 329

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or     SettlementStatus <SttlmSts> [1..1] ± C27 351
Or}     InstructionProcessingStatus <InstrPrcgSts> [1..1]  351
{Or       PendingProcessing <PdgPrcg> [1..1]  352
{Or         NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 353
Or}         Reason <Rsn> [1..*]  353
           Code <Cd> [1..1]  353
{Or             Code <Cd> [1..1] CodeSet 354
Or}             Proprietary <Prtry> [1..1] ± 355
           AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 355
Or       CancellationRequested <CxlReqd> [1..1] ± C4 355
Or       AcknowledgedAccepted <AckdAccptd> [1..1] ± 356
Or       Cancelled <Canc> [1..1] ± 356
Or       Generated <Gnrtd> [1..1]  356
{Or         NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 357
Or}         Reason <Rsn> [1..*] ± 357
Or       Repair <Rpr> [1..1] ± 357
Or       PendingCancellation <PdgCxl> [1..1]  357
{Or         NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 358
Or}         Reason <Rsn> [1..*]  358
           Code <Cd> [1..1]  358
{Or             Code <Cd> [1..1] CodeSet 359
Or}             Proprietary <Prtry> [1..1] ± 359
           AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 359
Or}       ModificationRequested <ModReqd> [1..1] ± C4 360
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
9.4.7.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 329 March 2026
```

