---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks", "26.4.16 AdditionalPhysicalOrRegistrationDetails <AddtlPhysOrRegnDtls>", "26.4.18.1 ProcessingStatus <PrcgSts>"]
file_pages: [871]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4.18.1 ProcessingStatus <PrcgSts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 871 to 871.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 871

```text
Constraints
• SettlementStatusAndMatchedRule
If settlement status/reason is used alone, then it means that the transaction is matched (if a matching
process exists in the concerned market or at the concerned account servicer).
26.4.18.1  ProcessingStatus <PrcgSts>
Presence: [0..1]
Definition: Provides the status of an instruction.
ProcessingStatus <PrcgSts> contains one of the following ProcessingStatus104Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 871
Or   PendingProcessing <PdgPrcg> [1..1] ± 871
Or   Repair <Rpr> [1..1] ± 872
Or   PendingCancellation <PdgCxl> [1..1]  872
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 873
Or}     Reason <Rsn> [1..*]  873
       Code <Cd> [1..1]  873
{Or         Code <Cd> [1..1] CodeSet 874
Or}         Proprietary <Prtry> [1..1] ± 874
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 874
Or   Proprietary <Prtry> [1..1] ± 874
Or}   CancellationRequested <CxlReqd> [1..1] ± C7 875
26.4.18.1.1  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus21Choice" on page 1968 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1968
Or}   Reason <Rsn> [1..*] ± 1969
26.4.18.1.2  PendingProcessing <PdgPrcg>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer but processing of the instruction
is pending.
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 871 March 2026
```

