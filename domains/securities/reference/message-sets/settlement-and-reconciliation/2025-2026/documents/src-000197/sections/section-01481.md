---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.61 RepoCallRequestStatus7Choice", "35.1.29.61.1 AcknowledgedAccepted <AckdAccptd>"]
file_pages: [1972]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.61.1 AcknowledgedAccepted <AckdAccptd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1972 to 1972.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1972

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1]  1972
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1972
Or}     Reason <Rsn> [1..*]  1972
       Code <Cd> [1..1] ± 1973
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1973
Or   Denied <Dnd> [1..1] ± 1973
Or}   Proprietary <Prtry> [1..1] ± 1973
35.1.29.61.1  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following
AcknowledgedAcceptedStatus22Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1972
Or}   Reason <Rsn> [1..*]  1972
     Code <Cd> [1..1] ± 1973
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1973
35.1.29.61.1.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.61.1.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the acknowledged accepted status.
Reason <Rsn> contains the following AcknowledgementReason10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 1973
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1973
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1972 March 2026
```

