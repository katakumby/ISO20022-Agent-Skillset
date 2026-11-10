---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.1 LineIdentification <LineId>"]
file_pages: [1597]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.1 LineIdentification <LineId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1597 to 1597.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1597

```text
Constraints
• AssetQuantity1Guideline
If Instrument/Security is present, then Quantity/Unit or Quantity/FaceAmount or Quantity/
AmortisedValue must be present.
• AssetQuantity2Guideline
If Instrument/CashAsset is present, then Quantity/CashAmount must be present.
• Conversion1Rule
If TransferType/Code/CONV (Conversion) is present, then Conversion must be present.
On Condition
    /TransferType/Code is equal to value 'Conversion'
Following Must be True
    /Conversion Must be present
• Conversion2Rule
If TransferType/Code/CONV (Conversion) is not present, then Conversion is not allowed.
On Condition
    /TransferType/Code is different from value 'Conversion'
Following Must be True
    /Conversion Must be absent
• EffectiveDatesGuideline
When the portfolio transfer confirmation is used to confirm the intent to transfer, effective transfer
date and effective settlement date are not applicable.
40.4.15.11.1  LineIdentification <LineId>
Presence: [0..1]
Definition: Identification of the line of holding in the portfolio.
Datatype: "Max35Text" on page 5403
40.4.15.11.2  Instrument <Instrm>
Presence: [1..1]
Definition: Identification of the asset.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1597 May 2026
```

