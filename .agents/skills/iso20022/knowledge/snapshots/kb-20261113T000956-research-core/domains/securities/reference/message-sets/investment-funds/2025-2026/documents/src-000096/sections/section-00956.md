---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "37.4 Message Building Blocks", "37.4.5 MasterReference <MstrRef>"]
file_pages: [1305]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.014.001.09"]
---

# 37.4.5 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1305 to 1305.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1305

```text
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
37.4.5 MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual transfers as assigned by the
instructing party. This identifier links the individual transfers together.
Datatype: "Max35Text" on page 5403
37.4.6 TransferReferences <TrfRefs>
Presence: [1..1]
Definition: Reference of the portfolio transfer instruction to be cancelled.
TransferReferences <TrfRefs> contains the following TransferReference14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransferReference <TrfRef> [1..1] Text 1305
   ClientReference <ClntRef> [0..1] ± 1305
   CounterpartyReference <CtrPtyRef> [0..1] ± 1306
   TransferConfirmationReference <TrfConfRef> [0..1] Text 1306
   CancellationReference <CxlRef> [0..1] Text 1306
   CancellationReason <CxlRsn> [0..1] Text 1306
37.4.6.1  TransferReference <TrfRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the portfolio transfer instruction, as assigned by the
instructing party.
Datatype: "Max35Text" on page 5403
37.4.6.2  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of the portfolio transfer. This reference can
typically be used in a hub scenario to give the reference of the transfer as assigned by the underlying
client.
Approved by the Securities SEG on 27 January 2026 sese.014.001.09
PortfolioTransferCancellationRequestV09
Investment Funds - Maintenance 2025 - 2026 1305 May 2026
```

