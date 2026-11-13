---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.1 OrderDetailsReport <OrdrDtlsRpt>", "56.4.3.1.1 MasterReference <MstrRef>"]
file_pages: [4128]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.1.1 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4128 to 4128.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4128

```text
OrderDetailsReport <OrdrDtlsRpt> contains the following OrderStatusAndReason11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MasterReference <MstrRef> [0..1] Text 4128
   OrderStatus <OrdrSts> [1..1]  4128
{Or     Status <Sts> [1..1] CodeSet 4129
Or     Cancelled <Canc> [1..1] ± C3, C5 4130
Or     ConditionallyAccepted <CondlyAccptd> [1..1] ± 4130
Or     Rejected <Rjctd> [1..10]  C18 4131
       Reason <Rsn> [0..1]  4131
{Or         Code <Cd> [1..1] CodeSet 4131
Or}         Proprietary <Prtry> [1..1] ± 4134
       AdditionalInformation <AddtlInf> [0..1] Text 4134
Or     Suspended <Sspd> [1..1] ± 4134
Or}     PartiallySettled <PrtlySttld> [1..1] ± 4134
   StatusInitiator <StsInitr> [0..1] ± 4135
56.4.3.1.1  MasterReference <MstrRef>
Presence: [0..1]
Definition: Reference assigned to a set of orders or trades in order to link them together.
Datatype: "Max35Text" on page 5403
56.4.3.1.2  OrderStatus <OrdrSts>
Presence: [1..1]
Definition: Status of a 'bulk' of orders. Can be used if all the individual orders conveyed in a bulk or
multiple order message have the same status.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4128 May 2026
```

