---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.8 AccountStatus2", "66.1.45.8.3 Pending <Pdg>"]
file_pages: [5177]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.8.3 Pending <Pdg>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5177 to 5177.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5177

```text
Disabled <Dsbld> contains one of the following elements (see "DisabledStatusReason1Choice" on
page 5181 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5181
Or}   Reason <Rsn> [1..*]  5181
     Code <Cd> [1..1]  5181
{Or       Code <Cd> [1..1] CodeSet 5182
Or}       Proprietary <Prtry> [1..1] ± 5182
     AdditionalInformation <AddtlInf> [0..1] Text 5182
66.1.45.8.3  Pending <Pdg>
Presence: [0..1]
Definition: Account change is pending approval.
Pending <Pdg> contains one of the following elements (see "PendingStatusReason1Choice" on
page 5179 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5179
Or}   Reason <Rsn> [1..*] ± 5179
66.1.45.8.4  PendingOpening <PdgOpng>
Presence: [0..1]
Definition: Account opening is pending.
PendingOpening <PdgOpng> contains one of the following elements (see
"PendingOpeningStatusReason1Choice" on page 5194 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5195
Or}   Reason <Rsn> [1..*]  5195
     Code <Cd> [1..1]  5195
{Or       Code <Cd> [1..1] CodeSet 5195
Or}       Proprietary <Prtry> [1..1] ± 5196
     AdditionalInformation <AddtlInf> [0..1] Text 5196
66.1.45.8.5  Proforma <Profrm>
Presence: [0..1]
Definition: Account is temporary and can be partially used for its intended purpose. The account will be
fully available for use when the account servicer has received all relevant documents.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5177 May 2026
```

