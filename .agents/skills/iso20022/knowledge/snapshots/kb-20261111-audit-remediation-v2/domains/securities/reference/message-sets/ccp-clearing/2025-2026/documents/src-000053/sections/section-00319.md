---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.11 Margin Call Calculation", "12.1.11.1 MarginCalculation2", "12.1.11.1.2 ExposureAmount <XpsrAmt>"]
file_pages: [410]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.11.1.2 ExposureAmount <XpsrAmt>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 410 to 410.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 410

```text
• ISINPresenceRule
(Rule)
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
Error handling:
– Error severity: Fatal
– Error Code: X00194
– Error Text: At least one identification must be present.
• OtherIdentificationPresenceRule
(Rule)
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
Error handling:
– Error severity: Fatal
– Error Code: X00193
– Error Text: At least one identification must be present.
12.1.11.1.2  ExposureAmount <XpsrAmt>
Presence: [0..1]
Definition: Net total of the transaction exposure of all outstanding deals.
ExposureAmount <XpsrAmt> contains the following Amount2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
410
   ReportingAmount <RptgAmt> [1..1] Amount 411
12.1.11.1.2.1  OriginalCurrencyAmount <OrgnlCcyAmt>
Presence: [0..1]
Definition: Amount expressed in the original currency.
Impacted by:   'C1 ActiveCurrency  ',   'C7 CurrencyAmount  '
Datatype: ActiveCurrencyAndAmount on page 470
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 410
```

