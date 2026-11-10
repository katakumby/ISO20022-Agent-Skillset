---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.51 FailingStatus13Choice", "35.1.29.51.2 Reason <Rsn>"]
file_pages: [1957]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.51.2 Reason <Rsn>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1957 to 1957.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1957

```text
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.51.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the failing status.
Reason <Rsn> contains the following FailingReason11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 1957
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1957
35.1.29.51.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a failing status.
Code <Cd> contains one of the following elements (see "FailingReason16Choice" on page 1888 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1888
Or}   Proprietary <Prtry> [1..1] ± 1892
35.1.29.51.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.52  SecuritiesPaymentStatus5Choice
Definition: Choice of format for the status of payment of a security at a particular time.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1957
Or}   Proprietary <Prtry> [1..1] ± 1958
35.1.29.52.1  Code <Cd>
Presence: [1..1]
Definition: Securities payment status expressed as an ISO 20022 code.
Datatype: "SecuritiesPaymentStatus1Code" on page 2142
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1957 March 2026
```

