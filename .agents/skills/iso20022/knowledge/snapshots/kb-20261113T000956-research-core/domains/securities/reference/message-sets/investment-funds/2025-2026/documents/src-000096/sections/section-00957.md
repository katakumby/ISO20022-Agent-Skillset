---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "37.4 Message Building Blocks", "37.4.6 TransferReferences <TrfRefs>", "37.4.6.3 CounterpartyReference <CtrPtyRef>"]
file_pages: [1306, 1307]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.014.001.09"]
---

# 37.4.6.3 CounterpartyReference <CtrPtyRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1306 to 1307.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1306

```text
ClientReference <ClntRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
37.4.6.3  CounterpartyReference <CtrPtyRef>
Presence: [0..1]
Definition: Unambiguous identification of the portfolio transfer allocated by the counterparty.
CounterpartyReference <CtrPtyRef> contains the following elements (see "AdditionalReference10"
on page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
37.4.6.4  TransferConfirmationReference <TrfConfRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the portfolio transfer execution, as assigned by the
confirming party.
Datatype: "Max35Text" on page 5403
37.4.6.5  CancellationReference <CxlRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the portfolio transfer cancellation, as assigned by the
instructing party.
Datatype: "Max35Text" on page 5403
37.4.6.6  CancellationReason <CxlRsn>
Presence: [0..1]
Definition: Reason for the cancellation.
Datatype: "Max35Text" on page 5403
37.4.7 MarketPracticeVersion <MktPrctcVrsn>
Presence: [0..1]
Definition: Identifies the market practice to which the message conforms.
Approved by the Securities SEG on 27 January 2026 sese.014.001.09
PortfolioTransferCancellationRequestV09
Investment Funds - Maintenance 2025 - 2026 1306 May 2026
```

## File page 1307

```text
MarketPracticeVersion <MktPrctcVrsn> contains the following elements (see
"MarketPracticeVersion1" on page 4818 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4818
   Date <Dt> [0..1] YearMonth 4819
   Number <Nb> [0..1] Text 4819
Approved by the Securities SEG on 27 January 2026 sese.014.001.09
PortfolioTransferCancellationRequestV09
Investment Funds - Maintenance 2025 - 2026 1307 May 2026
```

