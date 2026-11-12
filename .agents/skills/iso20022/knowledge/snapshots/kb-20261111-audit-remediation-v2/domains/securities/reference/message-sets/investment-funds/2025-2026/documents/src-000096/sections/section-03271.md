---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.6 TaxEfficientProductType2Choice", "66.1.18.6.2 Proprietary <Prtry>"]
file_pages: [4507]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.6.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4507 to 4507.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4507

```text
66.1.18.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of tax efficient product expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.18.7  GeneralInvestmentAccountType2Choice
Definition: Choice of formats for a type of investment account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4507
Or}   Proprietary <Prtry> [1..1] ± 4507
66.1.18.7.1  Code <Cd>
Presence: [1..1]
Definition: Type of investment account expressed as a code.
Datatype: "GeneralInvestmentAccountType2Code" on page 5308
CodeName Name Definition
ANYY Any Any type of general investment account.
EQUI ShareSavingsAccount General shares or equity savings
account.
66.1.18.7.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of investment account expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4507 May 2026
```

