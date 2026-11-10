---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.7.16 StatusAndReason <StsAndRsn>", "9.4.7.16.5 InstructionProcessingStatus <InstrPrcgSts>", "9.4.7.16.5.3 AcknowledgedAccepted <AckdAccptd>"]
file_pages: [356]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.7.16.5.3 AcknowledgedAccepted <AckdAccptd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 356 to 356.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 356

```text
CancellationRequested <CxlReqd> contains the following elements (see "ProprietaryReason4" on
page 1899 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 1899
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1899
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
9.4.7.16.5.3  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus21Choice" on page 1968 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1968
Or}   Reason <Rsn> [1..*] ± 1969
9.4.7.16.5.4  Cancelled <Canc>
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
9.4.7.16.5.5  Generated <Gnrtd>
Presence: [1..1]
Definition: Transaction was created by the account servicer or a third party. It was not instructed directly
by the account owner.
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 356 March 2026
```

