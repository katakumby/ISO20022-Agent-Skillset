---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.8 AccountDetails <AcctDtls>", "30.4.9.13 NetAmount <NetAmt>"]
file_pages: [766]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.9.13 NetAmount <NetAmt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 766 to 766.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 766

```text
CodeName Name Definition
ASTD Applicable Stamps duty is applicable.
SDRN NotApplicable Stamp duty not applicable.
30.4.9.13  NetAmount <NetAmt>
Presence: [0..1]
Definition: Deal amount.
Impacted by: C1 "ActiveCurrency", C10 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
30.4.9.14  Fees <Fees>
Presence: [0..*]
Definition: Fee related to the transfer of the financial instrument.
Impacted by: C19 "FeeTaxElementRule"
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 766 May 2026
```

