---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "51.4 Message Building Blocks", "51.4.6 CopyDetails <CpyDtls>"]
file_pages: [3247]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.011.001.05"]
---

# 51.4.6 CopyDetails <CpyDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3247 to 3247.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3247

```text
CancellationReason <CxlRsn> contains one of the following elements (see
"CancellationReason32Choice" on page 4869 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] Text 4869
Or}   Proprietary <Prtry> [1..1] ± 4869
51.4.6 CopyDetails <CpyDtls>
Presence: [0..1]
Definition: Information provided when the message is a copy of a previous message.
CopyDetails <CpyDtls> contains the following elements (see "CopyInformation5" on page 4817 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CopyIndicator <CpyInd> [1..1] Indicator 4817
   OriginalReceiver <OrgnlRcvr> [0..1] IdentifierSet C4 4817
Approved by the Securities SEG on 27 January 2026 setr.011.001.05
SubscriptionOrderCancellationRequestV05
Investment Funds - Maintenance 2025 - 2026 3247 May 2026
```

