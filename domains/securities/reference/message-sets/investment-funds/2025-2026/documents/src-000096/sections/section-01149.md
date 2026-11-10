---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.3 Quantity <Qty>", "40.4.15.11.3.4 AmortisedValue <AmtsdVal>"]
file_pages: [1606]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.3.4 AmortisedValue <AmtsdVal>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1606 to 1606.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1606

```text
Definition: Quantity expressed as an amount representing the face amount, that is, the principal, of a
debt instrument.
Datatype: "ImpliedCurrencyAndAmount" on page 5270
40.4.15.11.3.4  AmortisedValue <AmtsdVal>
Presence: [0..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Datatype: "ImpliedCurrencyAndAmount" on page 5270
40.4.15.11.3.5  CashAmount <CshAmt>
Presence: [0..1]
Definition: Cash amount transferred.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
40.4.15.11.3.6  OtherAsset <OthrAsst>
Presence: [0..1]
Definition: Quantity of asset transferred.
Datatype: "Max35Text" on page 5403
40.4.15.11.4  PartialInstructedQuantity <PrtlInstdQty>
Presence: [0..1]
Definition: Indicates that the quantity of asset transferred is a partially instructed quantity.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
40.4.15.11.5  OriginalPercentageInstructed <OrgnlPctgInstd>
Presence: [0..1]
Definition: Percentage rate of assets transferred, as originally instructed.
Datatype: "PercentageRate" on page 5401
40.4.15.11.6  TransferType <TrfTp>
Presence: [1..1]
Definition: Specifies how the financial instrument were transferred.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1606 May 2026
```

