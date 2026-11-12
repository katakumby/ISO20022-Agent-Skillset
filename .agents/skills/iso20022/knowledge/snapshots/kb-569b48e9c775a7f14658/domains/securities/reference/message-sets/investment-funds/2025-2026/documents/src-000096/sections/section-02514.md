---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.8 RelatedPartyDetails <RltdPtyDtls>", "53.4.5.8.4 Role <Role>"]
file_pages: [3542]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.8.4 Role <Role>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3542 to 3542.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3542

```text
53.4.5.8.4  Role <Role>
Presence: [0..1]
Definition: Function performed by the intermediary.
Role <Role> contains one of the following elements (see "InvestmentFundRole2Choice" on page 4779
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4779
Or}   Proprietary <Prtry> [1..1] ± 4780
53.4.5.9  RequestedFutureTradeDate <ReqdFutrTradDt>
Presence: [0..1]
Definition: Future date at which the investor requests the order to be executed.
The specification of a requested future trade date is not allowed in some markets. The date must be a
date in the future.
Datatype: "ISODate" on page 5388
53.4.5.10  SettlementAmount <SttlmAmt>
Presence: [0..1]
Definition: Total amount of money paid /to be paid or received in exchange for the financial instrument
in the individual order.
Impacted by: C2 "ActiveCurrency", C7 "CurrencyAmount"
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
53.4.5.11  CashSettlementDate <CshSttlmDt>
Presence: [0..1]
Definition: Date on which cash is available.
Datatype: "ISODate" on page 5388
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3542 May 2026
```

