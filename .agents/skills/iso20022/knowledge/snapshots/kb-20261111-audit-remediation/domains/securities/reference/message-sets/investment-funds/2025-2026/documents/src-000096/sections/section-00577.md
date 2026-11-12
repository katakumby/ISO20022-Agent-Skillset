---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["31 sese.008.001.09 ReversalOfTransferInConfirmationV09", "31.4 Message Building Blocks", "31.4.5 MasterReference <MstrRef>"]
file_pages: [781]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.008.001.09"]
---

# 31.4.5 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 781 to 781.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 781

```text
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
31.4.5 MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual transfers as assigned by the
instructing party. This identifier links the individual transfers together.
Datatype: "Max35Text" on page 5403
31.4.6 Function <Fctn>
Presence: [0..1]
Definition: Function of the transfer-in, that is, whether the message is used as a reversal of a previously
sent confirmation or as a reversal of a previously sent advice. The absence of Function indicates the
message is a reversal of a previously sent confirmation.
Datatype: "TransferInFunction2Code" on page 5379
CodeName Name Definition
CONF Confirmation The transfer-in is a confirmation (rather
than an advice).
ADVI Advice The transfer-in provides advice about
account information for a transfer.
31.4.7 ReversalReferences <RvslRefs>
Presence: [1..*]
Definition: Reference of the transfer confirmation to be reversed.
ReversalReferences <RvslRefs> contains the following TransferReference16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransferReference <TrfRef> [1..1] Text 782
   ClientReference <ClntRef> [0..1] ± 782
   TransferConfirmationReference <TrfConfRef> [0..1] Text 782
   CounterpartyReference <CtrPtyRef> [0..1] ± 782
   CancellationReference <CxlRef> [0..1] Text 782
   ReversalReason <RvslRsn> [0..1] Text 783
Approved by the Securities SEG on 27 January 2026 sese.008.001.09
ReversalOfTransferInConfirmationV09
Investment Funds - Maintenance 2025 - 2026 781 May 2026
```

