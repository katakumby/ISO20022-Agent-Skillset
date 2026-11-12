---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 semt.013.001.07 IntraPositionMovementInstructionV07", "5.4 Message Building Blocks", "5.4.3.3 Cancelled <Canc>"]
file_pages: [155]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.014.001.09"]
---

# 5.4.3.3 Cancelled <Canc>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 155 to 155.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 155

```text
5.4.3.3  Cancelled <Canc>
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
5.4.3.4  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus34Choice" on page 2023 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2023
Or}   Reason <Rsn> [1..*] ± 2024
5.4.3.5  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies a choice of status for the processing of an intra-position movement.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on page 1877
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 1878
   ProprietaryReason <PrtryRsn> [0..*] ± C1 1878
5.4.4 SettlementStatus <SttlmSts>
Presence: [0..1]
Definition: Provides the status of settlement of a transaction.
Impacted by: C10 "PendingToFailingRule"
Approved by the Securities SEG on 27 January 2026 semt.014.001.09
IntraPositionMovementStatusAdviceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 155 March 2026
```

