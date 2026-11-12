---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.6 FinancialInstrumentAttributes <FinInstrmAttrbts>", "3.4.6.10 OptionType <OptnTp>"]
file_pages: [69]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.6.10 OptionType <OptnTp>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 69 to 69.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 69

```text
Definition: Specifies how an option can be exercised (American, European, Bermudan).
OptionStyle <OptnStyle> contains one of the following elements (see "OptionStyle10Choice" on
page 288 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 288
Or}   Proprietary <Prtry> [1..1] ± 288
3.4.6.10  OptionType <OptnTp>
Presence: [0..1]
Definition: Specifies whether it is a Call option (right to purchase a specific underlying asset) or a Put
option (right to sell a specific underlying asset).
OptionType <OptnTp> contains one of the following elements (see "OptionType6Choice" on page 289
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 289
Or}   Proprietary <Prtry> [1..1] ± 290
3.4.6.11  DenominationCurrency <DnmtnCcy>
Presence: [0..1]
Definition: Currency in which a security is issued or redenominated.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 613
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
3.4.6.12  CouponDate <CpnDt>
Presence: [0..1]
Definition: Next payment date of an interest bearing financial instrument.
Datatype: "ISODate" on page 662
3.4.6.13  ExpiryDate <XpryDt>
Presence: [0..1]
Definition: Date on which a privilege expires.
Datatype: "ISODate" on page 662
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 69 February 2025
```

