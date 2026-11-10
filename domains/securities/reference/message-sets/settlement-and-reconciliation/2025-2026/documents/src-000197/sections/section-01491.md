---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.69 PendingStatus39Choice", "35.1.29.69.2 Reason <Rsn>", "35.1.29.69.2.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [1983]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.69.2.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1983 to 1983.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1983

```text
Code <Cd> contains one of the following elements (see "PendingReason30Choice" on page 1918 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1918
Or}   Proprietary <Prtry> [1..1] ± 1919
35.1.29.69.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.70  AcknowledgedAcceptedStatus24Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1983
Or}   Reason <Rsn> [1..*]  1983
     Code <Cd> [1..1] ± 1983
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1984
35.1.29.70.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.70.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the acknowledged accepted status.
Reason <Rsn> contains the following AcknowledgementReason12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 1983
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1984
35.1.29.70.2.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1983 March 2026
```

