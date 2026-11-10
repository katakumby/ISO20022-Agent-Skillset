---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.8 AccountStatus2", "66.1.45.8.1 Enabled <Nbld>"]
file_pages: [5176]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.8.1 Enabled <Nbld>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5176 to 5176.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5176

```text
• ClosedStatus6Rule
If Closed is present then ClosurePending is not allowed.
On Condition
    /Closed is absent
Following Must be True
    /ClosurePending Must be absent
• EnabledDisabledStatus1Rule
If Enabled is present, then Disabled is not allowed.
On Condition
    /Enabled is present
Following Must be True
    /Disabled Must be absent
• EnabledDisabledStatus2Rule
If Disabled is present, then Enabled is not allowed.
On Condition
    /Disabled is present
Following Must be True
    /Enabled Must be absent
• StatusElementRule
One of the elements (Enabled, Disabled, Pending, PendingOpening, Proforma, Closed,
ClosurePending, Other) must be present.
66.1.45.8.1  Enabled <Nbld>
Presence: [0..1]
Definition: Account can be used for its intended purpose.
Enabled <Nbld> contains one of the following elements (see "EnabledStatusReason1Choice" on
page 5202 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5203
Or}   Reason <Rsn> [1..*]  5203
     Code <Cd> [1..1]  5203
{Or       Code <Cd> [1..1] CodeSet 5203
Or}       Proprietary <Prtry> [1..1] ± 5204
     AdditionalInformation <AddtlInf> [0..1] Text 5204
66.1.45.8.2  Disabled <Dsbld>
Presence: [0..1]
Definition: Account cannot temporarily be used for its intended purpose.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5176 May 2026
```

