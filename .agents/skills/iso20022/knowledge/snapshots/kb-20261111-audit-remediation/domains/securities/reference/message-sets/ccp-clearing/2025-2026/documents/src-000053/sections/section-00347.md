---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.13 Miscellaneous", "12.1.13.2 Pagination1", "12.1.13.2.1 PageNumber <PgNb>"]
file_pages: [440]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.13.2.1 PageNumber <PgNb>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 440 to 440.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 440

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 440
   LastPageIndicator <LastPgInd> [1..1] Indicator 440
12.1.13.2.1  PageNumber <PgNb>
Presence: [1..1]
Definition: Page number.
Datatype: Max5NumericText on page 493
12.1.13.2.2  LastPageIndicator <LastPgInd>
Presence: [1..1]
Definition: Indicates the last page.
Datatype: One of the following values must be used (see YesNoIndicator on page 490):
• Meaning When True: Yes
• Meaning When False: No
12.1.13.3  Pagination
Definition: Number used to sequence pages when it is not possible for data to be conveyed in a single
message and the data has to be split across several pages (messages).
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 440
   LastPageIndicator <LastPgInd> [1..1] Indicator 440
12.1.13.3.1  PageNumber <PgNb>
Presence: [1..1]
Definition: Page number.
Datatype: Max5NumericText on page 493
12.1.13.3.2  LastPageIndicator <LastPgInd>
Presence: [1..1]
Definition: Indicates the last page.
Datatype: One of the following values must be used (see YesNoIndicator on page 490):
• Meaning When True: Yes
• Meaning When False: No
12.1.13.4  SupplementaryData1
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 440
```

