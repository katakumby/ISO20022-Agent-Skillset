---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.7 AdditionalAsset <AddtlAsst>"]
file_pages: [1607]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.7 AdditionalAsset <AddtlAsst>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1607 to 1607.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1607

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
40.4.15.11.7  AdditionalAsset <AddtlAsst>
Presence: [0..1]
Definition: Indicates the asset is a new asset, not previously identified by the transferor party (ceding
party) in the account holding discovery process.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
40.4.15.11.8  NotAvailable <NotAvlbl>
Presence: [0..1]
Definition: Indicates the asset is no longer available at the transferor party (ceding party).
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
40.4.15.11.9  Conversion <Convs>
Presence: [0..1]
Definition: Security was converted from another security before transfer.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1607 May 2026
```

