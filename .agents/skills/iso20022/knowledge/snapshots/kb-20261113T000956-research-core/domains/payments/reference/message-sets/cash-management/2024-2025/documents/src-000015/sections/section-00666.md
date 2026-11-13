---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.15 Reservation", "37.1.15.2 Reservation3", "37.1.15.2.2 Status <Sts>", "37.1.15.2.2.2 Proprietary <Prtry>"]
file_pages: [843]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.15.2.2.2 Proprietary <Prtry>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 843 to 843.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 843

```text
CodeName Name Definition
.
BLKD Blocked Reservation is blocked or frozen due to
external circumstances such as a court
order, death of beneficiary or account
owner, or bankruptcy.
37.1.15.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Liquidity transfer request type, in a proprietary form.
Datatype: "Max35Text" on page 889
37.1.15.2.3  StartDateTime <StartDtTm>
Presence: [0..1]
Definition: Date and time at which the reservation becomes effective.
StartDateTime <StartDtTm> contains one of the following elements (see "DateAndDateTime2Choice"
on page 801 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 801
Or}   DateTime <DtTm> [1..1] DateTime 801
37.1.16 Status
37.1.16.1  CancellationReason33Choice
Definition: Specifies the reason for the cancellation request.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 843
Or}   Proprietary <Prtry> [1..1] Text 843
37.1.16.1.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the cancellation request, in a coded form.
Datatype: "ExternalCancellationReason1Code" on page 852
37.1.16.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the cancellation request, in a proprietary form.
Datatype: "Max35Text" on page 889
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 843 February 2025
```

