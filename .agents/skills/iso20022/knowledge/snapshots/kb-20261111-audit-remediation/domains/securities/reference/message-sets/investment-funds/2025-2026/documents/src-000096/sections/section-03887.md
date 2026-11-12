---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.8 AccountStatus2", "66.1.45.8.6 Closed <Clsd>"]
file_pages: [5178]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.8.6 Closed <Clsd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5178 to 5178.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5178

```text
Proforma <Profrm> contains one of the following elements (see "ProformaStatusReason1Choice" on
page 5171 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5171
Or}   Reason <Rsn> [1..*]  5172
     Code <Cd> [1..1]  5172
{Or       Code <Cd> [1..1] CodeSet 5172
Or}       Proprietary <Prtry> [1..1] ± 5172
     AdditionalInformation <AddtlInf> [0..1] Text 5173
66.1.45.8.6  Closed <Clsd>
Presence: [0..1]
Definition: Account is closed.
Closed <Clsd> contains one of the following elements (see "ClosedStatusReason1Choice" on
page 5188 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5188
Or}   Reason <Rsn> [1..*]  5188
     Code <Cd> [1..1]  5188
{Or       Code <Cd> [1..1] CodeSet 5189
Or}       Proprietary <Prtry> [1..1] ± 5189
     AdditionalInformation <AddtlInf> [0..1] Text 5189
66.1.45.8.7  ClosurePending <ClsrPdg>
Presence: [0..1]
Definition: Account closure is pending.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5178 May 2026
```

