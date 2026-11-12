---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.2 IndividualOrderDetailsReport <IndvOrdrDtlsRpt>", "56.4.3.2.5 NonceIdentification <NonceId>"]
file_pages: [4140]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.2.5 NonceIdentification <NonceId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4140 to 4140.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4140

```text
Datatype: "Max35Text" on page 5403
56.4.3.2.5  NonceIdentification <NonceId>
Presence: [0..1]
Definition: Unambiguous identification of a random or semi-random number used once (NONCE)
generated in the frame of a cryptographic communication.
Datatype: "Max35Text" on page 5403
56.4.3.2.6  CancellationReference <CxlRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the order cancellation, as assigned by the instructing
party.
Datatype: "Max35Text" on page 5403
56.4.3.2.7  OrderStatus <OrdrSts>
Presence: [1..1]
Definition: Status of the individual order.
OrderStatus <OrdrSts> contains one of the following OrderStatus6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Status <Sts> [1..1] CodeSet 4140
Or   Cancelled <Canc> [1..1] ± C3, C5 4141
Or   ConditionallyAccepted <CondlyAccptd> [1..1] ± 4142
Or   Rejected <Rjctd> [1..10]  C18 4142
     Reason <Rsn> [0..1]  4143
{Or       Code <Cd> [1..1] CodeSet 4143
Or}       Proprietary <Prtry> [1..1] ± 4145
     AdditionalInformation <AddtlInf> [0..1] Text 4146
Or   Suspended <Sspd> [1..1] ± 4146
Or   InRepair <InRpr> [1..1] ± 4146
Or}   PartiallySettled <PrtlySttld> [1..1] ± 4147
56.4.3.2.7.1  Status <Sts>
Presence: [1..1]
Definition: Status of the individual order is accepted or already executed or sent to next party or
received. There is no reason attached.
Datatype: "OrderStatus4Code" on page 5333
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4140 May 2026
```

