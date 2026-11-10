---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["31 sese.008.001.09 ReversalOfTransferInConfirmationV09", "31.4 Message Building Blocks", "31.4.7 ReversalReferences <RvslRefs>", "31.4.7.1 TransferReference <TrfRef>"]
file_pages: [782]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.008.001.09"]
---

# 31.4.7.1 TransferReference <TrfRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 782 to 782.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 782

```text
31.4.7.1  TransferReference <TrfRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the transfer instruction for which the confirmation
reversal is sent, as assigned by the instructing party.
Datatype: "Max35Text" on page 5403
31.4.7.2  ClientReference <ClntRef>
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
31.4.7.3  TransferConfirmationReference <TrfConfRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the transfer execution for which the confirmation
reversal is sent, as assigned by the confirming party.
Datatype: "Max35Text" on page 5403
31.4.7.4  CounterpartyReference <CtrPtyRef>
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
31.4.7.5  CancellationReference <CxlRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the reversal as assigned by the confirming party.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 sese.008.001.09
ReversalOfTransferInConfirmationV09
Investment Funds - Maintenance 2025 - 2026 782 May 2026
```

