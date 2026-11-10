---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.1 LineIdentification <LineId>"]
file_pages: [1019]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.1 LineIdentification <LineId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1019 to 1019.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1019

```text
• AssetQuantity1Guideline
If Instrument/Security is present and Quantity is present, then Quantity/Unit or Quantity/
PercentageRate or Quantity/FaceAmount or Quantity/AmortisedValue must be present.
• AssetQuantity2Guideline
If Instrument/CashAsset is present and Quantity is present, then Quantity/CashAmount or Quantity/
Percentage must be present.
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
• PartialInstructedQuantityRule
If the value of PartialInstructedQuantity is 'true' or '1' (Yes), then Quantity must be present.
If the value of PartialInstructedQuantity is 'false' or '0'(No), then Quantity maybe present.
On Condition
    /PartialInstructedQuantity is equal to value 'true'
 Or    /PartialInstructedQuantity is equal to value '1'
Following Must be True
    /Quantity Must be present
35.4.14.10.1  LineIdentification <LineId>
Presence: [0..1]
Definition: Identification of the line of holding in the portfolio.
Datatype: "Max35Text" on page 5403
35.4.14.10.2  Instrument <Instrm>
Presence: [1..1]
Definition: Identification of the asset.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1019 May 2026
```

