---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.3 Pagination1"]
file_pages: [4817]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.3 Pagination1

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4817 to 4817.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4817

```text
66.1.28.3  Pagination1
Definition: Number used to sequence pages when it is not possible for data to be conveyed in a single
message and the data has to be split across several pages (messages).
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 4817
   LastPageIndicator <LastPgInd> [1..1] Indicator 4817
66.1.28.3.1  PageNumber <PgNb>
Presence: [1..1]
Definition: Page number.
Datatype: "Max5NumericText" on page 5404
66.1.28.3.2  LastPageIndicator <LastPgInd>
Presence: [1..1]
Definition: Indicates the last page.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.28.4  CopyInformation5
Definition: Information provided when the message is a copy of a previous message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CopyIndicator <CpyInd> [1..1] Indicator 4817
   OriginalReceiver <OrgnlRcvr> [0..1] IdentifierSet C4 4817
66.1.28.4.1  CopyIndicator <CpyInd>
Presence: [1..1]
Definition: Indicates whether the message is a copy.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.28.4.2  OriginalReceiver <OrgnlRcvr>
Presence: [0..1]
Definition: Original receiver of the message, if this message is a copy.
Impacted by: C4 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 5389
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4817 May 2026
```

