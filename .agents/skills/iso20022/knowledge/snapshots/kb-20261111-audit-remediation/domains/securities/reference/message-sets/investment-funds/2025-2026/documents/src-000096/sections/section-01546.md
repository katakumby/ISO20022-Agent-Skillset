---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.15 TransactionOverhead <TxOvrhd>", "44.4.4.9.15.2 IndividualFee <IndvFee>", "44.4.4.9.15.2.5 DiscountDetails <DscntDtls>", "44.4.4.9.15.2.5.2 Rate <Rate>"]
file_pages: [2170]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.15.2.5.2 Rate <Rate>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2170 to 2170.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2170

```text
EXAMPLE:
Standard charge is EUR 100
Discount is EUR 30
Applied charge is EUR 70.
Impacted by: C3 "ActiveCurrency", C10 "CurrencyAmount"
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
44.4.4.9.15.2.5.2  Rate <Rate>
Presence: [0..1]
Definition: Difference between the standard fee (charge/commission) rate and the applied rate of the
fee (charge/commission).
EXAMPLE:
Standard rate is 5%
Discount rate is 3%
Applied rate is 2%.
Datatype: "PercentageRate" on page 5401
44.4.4.9.15.2.5.3  Basis <Bsis>
Presence: [0..1]
Definition: Form of the discount or rebate, for example, cash.
Basis <Bsis> contains one of the following WaivingInstruction2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2170
Or}   Proprietary <Prtry> [1..1] ± 2171
44.4.4.9.15.2.5.3.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2170 May 2026
```

