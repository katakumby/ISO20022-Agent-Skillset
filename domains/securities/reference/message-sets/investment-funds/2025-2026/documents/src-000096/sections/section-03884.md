---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.7 PendingStatusReason14"]
file_pages: [5174, 5175]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.7 PendingStatusReason14

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5174 to 5175.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5174

```text
Rejected <Rjctd> contains the following elements (see "RejectionReason31" on page 5201 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  5202
{Or     Code <Cd> [1..1] CodeSet 5202
Or}     Proprietary <Prtry> [1..1] ± 5202
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 5202
66.1.45.7  PendingStatusReason14
Definition: Reason for a pending status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 5174
   AdditionalInformation <AddtlInf> [0..1] Text 5174
66.1.45.7.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the pending account status.
Code <Cd> contains one of the following elements (see "PendingStatusReason2Choice" on page 5180
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5180
Or}   Proprietary <Prtry> [1..1] ± 5180
66.1.45.7.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the reason for the pending account status.
Datatype: "Max350Text" on page 5403
66.1.45.8  AccountStatus2
Definition: Status of an account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5174 May 2026
```

## File page 5175

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Enabled <Nbld> [0..1] ± 5176
   Disabled <Dsbld> [0..1] ± 5176
   Pending <Pdg> [0..1] ± 5177
   PendingOpening <PdgOpng> [0..1] ± 5177
   Proforma <Profrm> [0..1] ± 5177
   Closed <Clsd> [0..1] ± 5178
   ClosurePending <ClsrPdg> [0..1] ± 5178
   Other <Othr> [0..*] ± 5179
Constraints
• ClosedStatus1Rule
If Closed is present then Enabled is not allowed.
On Condition
    /Closed is present
Following Must be True
    /Enabled Must be absent
• ClosedStatus2Rule
If Closed is present then Disabled is not allowed.
On Condition
    /Closed is present
Following Must be True
    /Disabled Must be absent
• ClosedStatus3Rule
If Closed is present then Pending is not allowed.
On Condition
    /Closed is present
Following Must be True
    /Pending Must be absent
• ClosedStatus4Rule
If Closed is present then PendingOpening is not allowed.
On Condition
    /Closed is present
Following Must be True
    /PendingOpening Must be absent
• ClosedStatus5Rule
If Closed is present then Proforma is not allowed.
On Condition
    /Closed is present
Following Must be True
    /Proforma Must be absent
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5175 May 2026
```

