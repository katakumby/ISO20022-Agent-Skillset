---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.47 Tax", "66.1.47.2 InformativeTax2", "66.1.47.2.2 EUCapitalGain <EUCptlGn>"]
file_pages: [5224]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.47.2.2 EUCapitalGain <EUCptlGn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5224 to 5224.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5224

```text
Definition: Amount included in the dividend that corresponds to gains directly or indirectly derived from
interest payment in the scope of the European Directive on taxation of savings income in the form of
interest payments.
Impacted by: C1 "ActiveCurrency", C13 "CurrencyAmount"
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
66.1.47.2.2  EUCapitalGain <EUCptlGn>
Presence: [0..1]
Definition: Specifies whether capital gain is in the scope of the European directive on taxation of
savings income in the form of interest payments (Council Directive 2003/48/EC 3 June), or an income
realised upon sale, a refund or redemption of shares and units, etc.
EUCapitalGain <EUCptlGn> contains one of the following EUCapitalGain3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5224
Or}   Proprietary <Prtry> [1..1] ± 5224
66.1.47.2.2.1  Code <Cd>
Presence: [1..1]
Definition: EU capital gain expressed as a code.
Datatype: "EUCapitalGain2Code" on page 5296
CodeName Name Definition
EUSI CapitalGainInScope Capital gain is in the scope of the
directive.
EUSO CapitalGainOutScope Capital gain is out of the scope of the
directive.
UKWN CapitalGainUnknown Unknown whether capital gain is in or
out of the scope of the directive.
66.1.47.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: EU capital gain expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5224 May 2026
```

