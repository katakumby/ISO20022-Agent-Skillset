---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.11 Margin Call Calculation", "12.1.11.1 MarginCalculation2", "12.1.11.1.6 MarginResult <MrgnRslt>", "12.1.11.1.6.1 ExcessAmount <XcssAmt>"]
file_pages: [413]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.11.1.6.1 ExcessAmount <XcssAmt>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 413 to 413.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 413

```text
Definition: Provide details on the margin result taking into consideration the total margin amount and the
minimum requirements deposit.
MarginResult <MrgnRslt> contains one of the following MarginResult1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ExcessAmount <XcssAmt> [1..1] Amount   'C1,
  'C7
413
Or}   DeficitAmount <DfcitAmt> [1..1] Amount   'C1,
  'C7
413
12.1.11.1.6.1  ExcessAmount <XcssAmt>
Presence: [1..1]
Definition: Excess amount that the central counterparty may restitute to the Clearing member.
Impacted by:   'C1 ActiveCurrency  ',   'C7 CurrencyAmount  '
Datatype: ActiveCurrencyAndAmount on page 470
Constraints
• ActiveCurrency
(Rule)
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
Error handling:
– Error severity: Fatal
– Error Code: D00005
– Error Text: Invalid currency code
• CurrencyAmount
(Rule)
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Error handling:
– Error severity: Fatal
– Error Code: D00007
– Error Text: Invalid currency code or too many decimal digits.
12.1.11.1.6.2  DeficitAmount <DfcitAmt>
Presence: [1..1]
Definition: Deficit amount that the central counterparty will provide to the clearing member.
Impacted by:   'C1 ActiveCurrency  ',   'C7 CurrencyAmount  '
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 413
```

