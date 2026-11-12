---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "25.4 Message Building Blocks", "25.4.6 TransferReferences <TrfRefs>", "25.4.6.3 CounterpartyReference <CtrPtyRef>"]
file_pages: [517]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.002.001.09"]
---

# 25.4.6.3 CounterpartyReference <CtrPtyRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 517 to 517.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 517

```text
ClientReference <ClntRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
25.4.6.3  CounterpartyReference <CtrPtyRef>
Presence: [0..1]
Definition: Unambiguous identification of the transfer allocated by the counterparty.
CounterpartyReference <CtrPtyRef> contains the following elements (see "AdditionalReference10"
on page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
25.4.6.4  CancellationReference <CxlRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the transfer cancellation, as assigned by the
instructing party.
Datatype: "Max35Text" on page 5403
25.4.6.5  CancellationReason <CxlRsn>
Presence: [0..1]
Definition: Reason for the cancellation.
Datatype: "Max35Text" on page 5403
25.4.7 MarketPracticeVersion <MktPrctcVrsn>
Presence: [0..1]
Definition: Identifies the market practice to which the message conforms.
Approved by the Securities SEG on 27 January 2026 sese.002.001.09
TransferOutCancellationRequestV09
Investment Funds - Maintenance 2025 - 2026 517 May 2026
```

