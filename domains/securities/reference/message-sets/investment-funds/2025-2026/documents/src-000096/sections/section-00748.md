---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.3 Quantity <Qty>", "35.4.14.10.3.4 AmortisedValue <AmtsdVal>"]
file_pages: [1028]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.3.4 AmortisedValue <AmtsdVal>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1028 to 1028.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1028

```text
Definition: Quantity expressed as an amount representing the face amount, that is, the principal, of a
debt instrument.
Datatype: "ImpliedCurrencyAndAmount" on page 5270
35.4.14.10.3.4  AmortisedValue <AmtsdVal>
Presence: [0..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Datatype: "ImpliedCurrencyAndAmount" on page 5270
35.4.14.10.3.5  CashAmount <CshAmt>
Presence: [0..1]
Definition: Cash amount to be transferred.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
35.4.14.10.3.6  OtherAsset <OthrAsst>
Presence: [0..1]
Definition: Quantity of asset to be transferred.
Datatype: "Max35Text" on page 5403
35.4.14.10.4  PartialInstructedQuantity <PrtlInstdQty>
Presence: [0..1]
Definition: Indicates that the quantity of asset to be transferred is a partially instructed quantity.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
35.4.14.10.5  TransferType <TrfTp>
Presence: [1..1]
Definition: Specifies how the financial instrument is transferred.
Impacted by: C41 "SECUGuideline"
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1028 May 2026
```

