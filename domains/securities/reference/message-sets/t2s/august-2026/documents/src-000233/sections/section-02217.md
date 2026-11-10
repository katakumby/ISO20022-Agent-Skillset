---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.5 Number3Choice", "82.1.19.5.1 Short <Shrt>"]
file_pages: [2980]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.5.1 Short <Shrt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2980 to 2980.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2980

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Short <Shrt> [1..1] Text 2980
Or}   Long <Lng> [1..1] Text 2980
82.1.19.5.1  Short <Shrt>
Presence: [1..1]
Definition: Number of maximum 3 numeric text.
Datatype: "Exact3NumericText" on page 3325
82.1.19.5.2  Long <Lng>
Presence: [1..1]
Definition: Number of maximum 5 numeric text. Is only to be used in a delta statement.
Datatype: "Exact5NumericText" on page 3325
82.1.19.6  Pagination1
Definition: Number used to sequence pages when it is not possible for data to be conveyed in a single
message and the data has to be split across several pages (messages).
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 2980
   LastPageIndicator <LastPgInd> [1..1] Indicator 2980
82.1.19.6.1  PageNumber <PgNb>
Presence: [1..1]
Definition: Page number.
Datatype: "Max5NumericText" on page 3329
82.1.19.6.2  LastPageIndicator <LastPgInd>
Presence: [1..1]
Definition: Indicates the last page.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
82.1.19.7  OptionType6Choice
Definition: Choice of format for the option type.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2980 August 2026
```

