---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.26 Status", "16.1.26.10 PendingStatusReason29"]
file_pages: [1153]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.26.10 PendingStatusReason29

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1153 to 1153.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1153

```text
16.1.26.10  PendingStatusReason29
Definition: Specifies reasons for the pending status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReasonCode <RsnCd> [1..1] ± 1153
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1153
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
16.1.26.10.1  ReasonCode <RsnCd>
Presence: [1..1]
Definition: Specifies the reason why the instruction's processing is pending.
ReasonCode <RsnCd> contains one of the following elements (see "PendingReason70Choice" on
page 1153 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1153
Or}   Proprietary <Prtry> [1..1] ± 1154
16.1.26.10.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional information about the processed instruction.
Datatype: "Max210Text" on page 1249
16.1.26.11  PendingReason70Choice
Definition: Choice between a standard code and a proprietary code to specify the reason why the
instruction/event has a pending status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1153
Or}   Proprietary <Prtry> [1..1] ± 1154
16.1.26.11.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the reason why the instruction/event has a pending status.
Datatype: "PendingReason29Code" on page 1228
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1153 February 2026
```

