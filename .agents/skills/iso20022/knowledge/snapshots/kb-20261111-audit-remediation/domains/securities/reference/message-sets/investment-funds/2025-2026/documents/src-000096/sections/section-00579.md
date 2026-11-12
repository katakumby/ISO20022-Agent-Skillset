---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["31 sese.008.001.09 ReversalOfTransferInConfirmationV09", "31.4 Message Building Blocks", "31.4.7 ReversalReferences <RvslRefs>", "31.4.7.6 ReversalReason <RvslRsn>"]
file_pages: [783]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.008.001.09"]
---

# 31.4.7.6 ReversalReason <RvslRsn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 783 to 783.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 783

```text
31.4.7.6  ReversalReason <RvslRsn>
Presence: [0..1]
Definition: Reason for the reversal of confirmation.
Datatype: "Max35Text" on page 5403
31.4.8 MarketPracticeVersion <MktPrctcVrsn>
Presence: [0..1]
Definition: Identifies the market practice to which the message conforms.
MarketPracticeVersion <MktPrctcVrsn> contains the following elements (see
"MarketPracticeVersion1" on page 4818 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4818
   Date <Dt> [0..1] YearMonth 4819
   Number <Nb> [0..1] Text 4819
31.4.9 CopyDetails <CpyDtls>
Presence: [0..1]
Definition: Information provided when the message is a copy of a previous message.
CopyDetails <CpyDtls> contains the following elements (see "CopyInformation5" on page 4817 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CopyIndicator <CpyInd> [1..1] Indicator 4817
   OriginalReceiver <OrgnlRcvr> [0..1] IdentifierSet C4 4817
Approved by the Securities SEG on 27 January 2026 sese.008.001.09
ReversalOfTransferInConfirmationV09
Investment Funds - Maintenance 2025 - 2026 783 May 2026
```

