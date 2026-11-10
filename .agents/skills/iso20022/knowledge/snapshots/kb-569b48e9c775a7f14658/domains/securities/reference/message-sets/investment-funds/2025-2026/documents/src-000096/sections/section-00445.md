---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "27.4 Message Building Blocks", "27.4.6 ReversalReferences <RvslRefs>", "27.4.6.3 TransferConfirmationReference <TrfConfRef>"]
file_pages: [606]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.004.001.09"]
---

# 27.4.6.3 TransferConfirmationReference <TrfConfRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 606 to 606.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 606

```text
ClientReference <ClntRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
27.4.6.3  TransferConfirmationReference <TrfConfRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the transfer execution for which the confirmation
reversal is sent, as assigned by the confirming party.
Datatype: "Max35Text" on page 5403
27.4.6.4  CounterpartyReference <CtrPtyRef>
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
27.4.6.5  CancellationReference <CxlRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the reversal as assigned by the confirming party.
Datatype: "Max35Text" on page 5403
27.4.6.6  ReversalReason <RvslRsn>
Presence: [0..1]
Definition: Reason for the reversal of confirmation.
Datatype: "Max35Text" on page 5403
27.4.7 MarketPracticeVersion <MktPrctcVrsn>
Presence: [0..1]
Definition: Identifies the market practice to which the message conforms.
Approved by the Securities SEG on 27 January 2026 sese.004.001.09
ReversalOfTransferOutConfirmationV09
Investment Funds - Maintenance 2025 - 2026 606 May 2026
```

