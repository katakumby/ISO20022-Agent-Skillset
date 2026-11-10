---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.36 Quantity", "66.1.36.1 FinancialInstrumentQuantity33Choice", "66.1.36.1.3 AmortisedValue <AmtsdVal>"]
file_pages: [5129]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.36.1.3 AmortisedValue <AmtsdVal>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5129 to 5129.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5129

```text
Datatype: "ImpliedCurrencyAndAmount" on page 5270
66.1.36.1.3  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Datatype: "ImpliedCurrencyAndAmount" on page 5270
66.1.36.1.4  DigitalTokenUnit <DgtlTknUnit>
Presence: [1..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 5400
66.1.37 Report Parameter
66.1.37.1  FrequencyCodeAndDSSCode1Choice
Definition: Choice between formats for the frequency.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FrequencyAsCode <FrqcyAsCd> [1..1] CodeSet 5129
Or}   FrequencyAsDSS <FrqcyAsDSS> [1..1] ± 5130
66.1.37.1.1  FrequencyAsCode <FrqcyAsCd>
Presence: [1..1]
Definition: Frequency expressed as a code.
Datatype: "EventFrequency1Code" on page 5297
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
SEMI SemiAnnual Event takes place every six months or
two times a year.
QUTR Quarterly Event takes place every three months or
four times a year.
TOMN EveryTwoMonths Event takes place every two months.
MNTH Monthly Event takes place every month or once a
month.
TWMN TwiceAMonth Event takes place two times a month.
TOWK EveryTwoWeeks Event takes place every two weeks.
WEEK Weekly Event takes place once a week.
DAIL Daily Event takes place every day.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5129 May 2026
```

