---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.26 Status"]
file_pages: [1140]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.26 Status

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1140 to 1140.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1140

```text
16.1.26 Status
16.1.26.1  CancelledStatus5
Definition: Choice between a reason or no reason for the corporate action instruction or instruction
cancellation cancelled/cancellation completed status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CancelledQuantity <CancQty> [0..1] ± 1140
   CancellationReason <CxlRsn> [1..1] ± 1140
16.1.26.1.1  CancelledQuantity <CancQty>
Presence: [0..1]
Definition: Quantity of instructed securities for which instruction is cancelled.
CancelledQuantity <CancQty> contains one of the following elements (see "Quantity51Choice" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C13 1091
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 1091
16.1.26.1.2  CancellationReason <CxlRsn>
Presence: [1..1]
Definition: Reason for the cancelled status.
CancellationReason <CxlRsn> contains one of the following elements (see
"CancelledStatus12Choice" on page 1146 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1147
Or}   Reason <Rsn> [1..*]  C2 1147
     ReasonCode <RsnCd> [1..1]  1147
{Or       Code <Cd> [1..1] CodeSet 1148
Or}       Proprietary <Prtry> [1..1] ± 1148
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1148
16.1.26.2  ProprietaryStatusAndReason6
Definition: Provides the proprietary status and reason of an instruction or an instruction cancellation.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1140 February 2026
```

