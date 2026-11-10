---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.32 Liability1Choice"]
file_pages: [4870]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.32 Liability1Choice

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4870 to 4870.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4870

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 4552 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   Issuer <Issr> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4553
66.1.28.32  Liability1Choice
Definition: Choice of formats for liability.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4870
Or}   Proprietary <Prtry> [1..1] ± 4870
66.1.28.32.1  Code <Cd>
Presence: [1..1]
Definition: Liability expressed as a code.
Datatype: "Liability1Code" on page 5329
CodeName Name Definition
INVE Investor Investor is responsible.
BROK Broker Broker is responsible.
66.1.28.32.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Liability expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.28.33  CashAll1
Definition: Specifies whether all assets in the portfolio should be liquidated and transferred as cash.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4870 May 2026
```

