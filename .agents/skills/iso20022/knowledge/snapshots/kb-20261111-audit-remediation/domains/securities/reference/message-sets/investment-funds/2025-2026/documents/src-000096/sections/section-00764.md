---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.9 UnitsDetails <UnitsDtls>", "35.4.14.10.9.8 TransactionOverhead <TxOvrhd>", "35.4.14.10.9.8.5 IndividualFee <IndvFee>", "35.4.14.10.9.8.5.5 DiscountDetails <DscntDtls>"]
file_pages: [1047]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.9.8.5.5 DiscountDetails <DscntDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1047 to 1047.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1047

```text
35.4.14.10.9.8.5.5  DiscountDetails <DscntDtls>
Presence: [0..1]
Definition: Discount or waiver applied to the fee (charge/commission).
Impacted by: C23 "DiscountElementRule"
DiscountDetails <DscntDtls> contains the following ChargeOrCommissionDiscount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] Amount C1, C18 1047
   Rate <Rate> [0..1] Rate 1048
   Basis <Bsis> [0..1]  1048
{Or     Code <Cd> [1..1] CodeSet 1048
Or}     Proprietary <Prtry> [1..1] ± 1048
Constraints
• DiscountElementRule
Amount Or Rate Or Basis must be present.
Following Must be True
    /Amount Must be present
 Or    /Rate Must be present
 Or    /Basis Must be present
35.4.14.10.9.8.5.5.1  Amount <Amt>
Presence: [0..1]
Definition: Difference between the standard fee (charge/commission) amount and the applied fee
(charge/commission) amount.
EXAMPLE:
Standard charge is EUR 100
Discount is EUR 30
Applied charge is EUR 70.
Impacted by: C1 "ActiveCurrency", C18 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1047 May 2026
```

