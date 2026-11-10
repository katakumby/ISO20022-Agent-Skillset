---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "27.4 Message Building Blocks", "27.4.5 MasterReference <MstrRef>"]
file_pages: [605]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.004.001.09"]
---

# 27.4.5 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 605 to 605.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 605

```text
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
27.4.5 MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual transfers as assigned by the
instructing party. This identifier links the individual transfers together.
Datatype: "Max35Text" on page 5403
27.4.6 ReversalReferences <RvslRefs>
Presence: [1..*]
Definition: Reference of the transfer confirmation to be reversed.
ReversalReferences <RvslRefs> contains the following TransferReference16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransferReference <TrfRef> [1..1] Text 605
   ClientReference <ClntRef> [0..1] ± 605
   TransferConfirmationReference <TrfConfRef> [0..1] Text 606
   CounterpartyReference <CtrPtyRef> [0..1] ± 606
   CancellationReference <CxlRef> [0..1] Text 606
   ReversalReason <RvslRsn> [0..1] Text 606
27.4.6.1  TransferReference <TrfRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the transfer instruction for which the confirmation
reversal is sent, as assigned by the instructing party.
Datatype: "Max35Text" on page 5403
27.4.6.2  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of the transfer. This reference can typically
be used in a hub scenario to give the reference of the transfer as assigned by the underlying client.
Approved by the Securities SEG on 27 January 2026 sese.004.001.09
ReversalOfTransferOutConfirmationV09
Investment Funds - Maintenance 2025 - 2026 605 May 2026
```

