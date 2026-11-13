---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.15 LevelOfControl1Choice", "66.1.28.15.1 Code <Cd>"]
file_pages: [4833]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.15.1 Code <Cd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4833 to 4833.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4833

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4833
Or}   Proprietary <Prtry> [1..1] ± 4833
66.1.28.15.1  Code <Cd>
Presence: [1..1]
Definition: Level of control expressed as a code.
Datatype: "LevelOfControl1Code" on page 5329
CodeName Name Definition
TRAN Transactions Transactions are permitted on the
account.
VIEW View Account may be viewed only.
66.1.28.15.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Level of control expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.28.16  Pagination
Definition: Number used to sequence pages when it is not possible for data to be conveyed in a single
message and the data has to be split across several pages (messages).
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 4833
   LastPageIndicator <LastPgInd> [1..1] Indicator 4833
66.1.28.16.1  PageNumber <PgNb>
Presence: [1..1]
Definition: Page number.
Datatype: "Max5NumericText" on page 5404
66.1.28.16.2  LastPageIndicator <LastPgInd>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4833 May 2026
```

