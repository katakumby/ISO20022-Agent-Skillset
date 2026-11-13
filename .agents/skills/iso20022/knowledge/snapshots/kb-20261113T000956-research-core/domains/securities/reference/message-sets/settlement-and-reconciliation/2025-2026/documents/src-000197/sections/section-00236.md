---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.7.16 StatusAndReason <StsAndRsn>", "9.4.7.16.4 SettlementStatus <SttlmSts>"]
file_pages: [351]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.7.16.4 SettlementStatus <SttlmSts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 351 to 351.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 351

```text
InferredMatchingStatus <IfrrdMtchgSts> contains one of the following elements (see
"MatchingStatus24Choice" on page 1963 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Matched <Mtchd> [1..1] ± C1 1964
Or   Unmatched <Umtchd> [1..1]  1964
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1965
Or}     Reason <Rsn> [1..*]  1965
       Code <Cd> [1..1]  1965
{Or         Code <Cd> [1..1] CodeSet 1966
Or}         Proprietary <Prtry> [1..1] ± 1968
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1968
Or}   Proprietary <Prtry> [1..1] ± 1968
9.4.7.16.4  SettlementStatus <SttlmSts>
Presence: [1..1]
Definition: Provides the status of settlement of a transaction.
Impacted by: C27 "PendingToFailingRule"
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus30Choice" on page 1952 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1] ± 1953
Or   Failing <Flng> [1..1] ± 1953
Or}   Proprietary <Prtry> [1..1] ± 1953
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
9.4.7.16.5  InstructionProcessingStatus <InstrPrcgSts>
Presence: [1..1]
Definition: Provides the status of an instruction.
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 351 March 2026
```

