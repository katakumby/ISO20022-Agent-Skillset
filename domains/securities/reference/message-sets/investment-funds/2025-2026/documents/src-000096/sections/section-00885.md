---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "36.4.15.11.7 AdditionalAsset <AddtlAsst>"]
file_pages: [1224]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.11.7 AdditionalAsset <AddtlAsst>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1224 to 1224.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1224

```text
Impacted by: C46 "SECUGuideline"
TransferType <TrfTp> contains one of the following elements (see "TransferType2Choice" on
page 5256 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5256
Or}   Proprietary <Prtry> [1..1] ± 5256
Constraints
• SECUGuideline
The code SECU (Asset) is used when a financial instrument such as units of a fund are to be
transferred.
The code SECU is also used when assets such as equities or bonds are to be transferred. The code
SECU is also used for assets such as property, moveable property and other similar types of other
asset.
36.4.15.11.7  AdditionalAsset <AddtlAsst>
Presence: [0..1]
Definition: Indicates the asset is a new asset, not previously identified by the transferor party (ceding
party) in the account holding discovery process.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
36.4.15.11.8  NotAvailable <NotAvlbl>
Presence: [0..1]
Definition: Indicates the asset is no longer available at the transferor party (ceding party).
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
36.4.15.11.9  Conversion <Convs>
Presence: [0..1]
Definition: Security is to be converted into another security before transfer.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1224 May 2026
```

