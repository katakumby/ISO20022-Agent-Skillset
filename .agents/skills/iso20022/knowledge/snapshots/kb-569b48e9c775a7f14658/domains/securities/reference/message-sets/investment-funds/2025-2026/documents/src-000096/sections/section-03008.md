---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "57.4 Message Building Blocks", "57.4.3 StatusReport <StsRpt>", "57.4.3.1 CancellationStatusReport <CxlStsRpt>"]
file_pages: [4213]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.017.001.05"]
---

# 57.4.3.1 CancellationStatusReport <CxlStsRpt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4213 to 4213.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4213

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         SeriesName <SrsNm> [0..1] Text 4231
57.4.3.1  CancellationStatusReport <CxlStsRpt>
Presence: [1..1]
Definition: Status report details of a bulk or multiple or switch order cancellation message.
CancellationStatusReport <CxlStsRpt> contains the following OrderStatusAndReason12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MasterReference <MstrRef> [0..1] Text 4213
   CancellationStatus <CxlSts> [1..1]  4213
{Or     Status <Sts> [1..1] CodeSet 4214
Or}     Rejected <Rjctd> [1..1]  C8 4214
       Reason <Rsn> [0..1]  4214
{Or         Code <Cd> [1..1] CodeSet 4215
Or}         Proprietary <Prtry> [1..1] ± 4215
       AdditionalInformation <AddtlInf> [0..1] Text 4215
   StatusInitiator <StsInitr> [0..1] ± 4216
57.4.3.1.1  MasterReference <MstrRef>
Presence: [0..1]
Definition: Reference assigned to a set of orders or trades in order to link them together.
Datatype: "Max35Text" on page 5403
57.4.3.1.2  CancellationStatus <CxlSts>
Presence: [1..1]
Definition: Cancellation status of the order cancellation.
CancellationStatus <CxlSts> contains one of the following CancellationStatus33Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Status <Sts> [1..1] CodeSet 4214
Or}   Rejected <Rjctd> [1..1]  C8 4214
     Reason <Rsn> [0..1]  4214
{Or       Code <Cd> [1..1] CodeSet 4215
Or}       Proprietary <Prtry> [1..1] ± 4215
     AdditionalInformation <AddtlInf> [0..1] Text 4215
Approved by the Securities SEG on 27 January 2026 setr.017.001.05 OrderCancellationStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4213 May 2026
```

