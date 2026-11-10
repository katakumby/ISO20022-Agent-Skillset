---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.3 SwitchOrderDetailsReport <SwtchOrdrDtlsRpt>", "56.4.3.3.8 LegInformation <LegInf>", "56.4.3.3.8.3 RepairedFee <RprdFee>", "56.4.3.3.8.3.5 RepairedDiscountRate <RprdDscntRate>"]
file_pages: [4191]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.3.8.3.5 RepairedDiscountRate <RprdDscntRate>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4191 to 4191.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4191

```text
Definition: Modified value of the discount amount applied on the order (the discount amount in the
original individual order that has been repaired so that the order can be accepted).
Impacted by: C1 "ActiveCurrency", C8 "CurrencyAmount"
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
56.4.3.3.8.3.5  RepairedDiscountRate <RprdDscntRate>
Presence: [0..1]
Definition: Modified value of the discount rate applied on the order (the discount rate in the original
individual order that has been repaired so that the order can be accepted).
Datatype: "PercentageRate" on page 5401
56.4.3.3.8.3.6  RepairedRequestedAmount <RprdReqdAmt>
Presence: [0..1]
Definition: Modified value of the requested fee (charge/commission) amount applied on the order (the
requested fee (charge/commission) amount in the original individual order that has been repaired so
that the order can be accepted).
Impacted by: C1 "ActiveCurrency", C8 "CurrencyAmount"
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
56.4.3.3.8.3.7  RepairedRequestedRate <RprdReqdRate>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4191 May 2026
```

