---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.2 TransferReference <TrfRef>"]
file_pages: [841]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.2 TransferReference <TrfRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 841 to 841.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 841

```text
34.4.4.2  TransferReference <TrfRef>
Presence: [1..1]
Definition: Unique and unambiguous identification of the transfer, as assigned by the instructing party.
TransferReference <TrfRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
34.4.4.3  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of the transfer. This reference can typically
be used in a hub scenario to give the reference of the transfer as assigned by the underlying client.
ClientReference <ClntRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
34.4.4.4  CancellationReference <CxlRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a transfer cancellation, as assigned by the instructing
party.
Datatype: "Max35Text" on page 5403
34.4.4.5  TransferEventType <TrfEvtTp>
Presence: [0..*]
Definition: Type of event for which the message is sent.
TransferEventType <TrfEvtTp> contains one of the following TransferStatusType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 841
Or}   Proprietary <Prtry> [1..1] ± 842
34.4.4.5.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 841 May 2026
```

