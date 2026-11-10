---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["29 sese.006.001.09 TransferInCancellationRequestV09", "29.4 Message Building Blocks", "29.4.7 TransferReferences <TrfRefs>"]
file_pages: [693]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.006.001.09"]
---

# 29.4.7 TransferReferences <TrfRefs>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 693 to 693.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 693

```text
29.4.7 TransferReferences <TrfRefs>
Presence: [1..*]
Definition: Reference of the transfer to be cancelled.
TransferReferences <TrfRefs> contains the following TransferReference15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransferReference <TrfRef> [1..1] Text 693
   ClientReference <ClntRef> [0..1] ± 693
   CounterpartyReference <CtrPtyRef> [0..1] ± 693
   CancellationReference <CxlRef> [0..1] Text 694
   CancellationReason <CxlRsn> [0..1] Text 694
29.4.7.1  TransferReference <TrfRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the transfer instruction for which the cancellation
request is sent, as assigned by the instructing party.
Datatype: "Max35Text" on page 5403
29.4.7.2  ClientReference <ClntRef>
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
29.4.7.3  CounterpartyReference <CtrPtyRef>
Presence: [0..1]
Definition: Unambiguous identification of the transfer allocated by the counterparty.
Approved by the Securities SEG on 27 January 2026 sese.006.001.09
TransferInCancellationRequestV09
Investment Funds - Maintenance 2025 - 2026 693 May 2026
```

