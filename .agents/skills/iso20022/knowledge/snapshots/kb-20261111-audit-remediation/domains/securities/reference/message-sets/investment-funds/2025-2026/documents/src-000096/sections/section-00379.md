---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "25.4 Message Building Blocks", "25.4.8 CopyDetails <CpyDtls>"]
file_pages: [518]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.002.001.09"]
---

# 25.4.8 CopyDetails <CpyDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 518 to 518.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 518

```text
MarketPracticeVersion <MktPrctcVrsn> contains the following elements (see
"MarketPracticeVersion1" on page 4818 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4818
   Date <Dt> [0..1] YearMonth 4819
   Number <Nb> [0..1] Text 4819
25.4.8 CopyDetails <CpyDtls>
Presence: [0..1]
Definition: Information provided when the message is a copy of a previous message.
CopyDetails <CpyDtls> contains the following elements (see "CopyInformation5" on page 4817 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CopyIndicator <CpyInd> [1..1] Indicator 4817
   OriginalReceiver <OrgnlRcvr> [0..1] IdentifierSet C4 4817
Approved by the Securities SEG on 27 January 2026 sese.002.001.09
TransferOutCancellationRequestV09
Investment Funds - Maintenance 2025 - 2026 518 May 2026
```

