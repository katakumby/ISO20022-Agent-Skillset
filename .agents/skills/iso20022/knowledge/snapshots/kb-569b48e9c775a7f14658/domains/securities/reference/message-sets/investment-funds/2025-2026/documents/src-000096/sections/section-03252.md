---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.1 FinancialInstrument96", "66.1.18.1.9 FrontEndLoad <FrntEndLd>"]
file_pages: [4488]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.1.9 FrontEndLoad <FrntEndLd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4488 to 4488.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4488

```text
CodeName Name Definition
DAIL Daily Event takes place every day.
CLOS Closed Event cannot take place, because, for
example, the fund is closed.
TOMN EveryTwoMonths Event takes place every two months.
TOWK EveryTwoWeeks Event takes place every two weeks.
TWMN TwiceAMonth Event takes place two times a month.
66.1.18.1.9  FrontEndLoad <FrntEndLd>
Presence: [0..1]
Definition: Indicates whether a front end charge on subscription orders for this class can be applied.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.18.1.10  BackEndLoad <BckEndLd>
Presence: [0..1]
Definition: Indicates whether an exit charge (for example, CDSC) on redemption orders for this class
can be applied.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.18.1.11  SwitchFee <SwtchFee>
Presence: [0..1]
Definition: Indicates whether a separate fee for switching between sub-funds of the same umbrella can
be applied.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.18.1.12  EUSavingsDirective <EUSvgsDrctv>
Presence: [0..1]
Definition: Indicates whether the investment fund class is subject to the European Union Saving
Directive.
Datatype: "EUSavingsDirective1Code" on page 5297
CodeName Name Definition
EUSI EUSavingsInScope Investment Fund is in the scope of the
directive.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4488 May 2026
```

