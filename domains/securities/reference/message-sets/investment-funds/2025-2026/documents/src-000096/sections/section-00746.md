---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.2 Instrument <Instrm>", "35.4.14.10.2.3 OtherAsset <OthrAsst>"]
file_pages: [1026]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.2.3 OtherAsset <OthrAsst>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1026 to 1026.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1026

```text
CashAsset <CshAsst> contains the following elements (see "CashAsset3" on page 4519 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAssetType <CshAsstTp> [1..1]  4520
{Or     Code <Cd> [1..1] CodeSet 4520
Or}     Proprietary <Prtry> [1..1] ± 4520
   HoldingCurrency <HldgCcy> [1..1] CodeSet C1 4520
   TransferCurrency <TrfCcy> [0..1] CodeSet C1 4521
   AdditionalInformation <AddtlInf> [0..1] ± 4521
Constraints
• HoldingTransferCurrencyGuideline
When cash is transferred in a currency other than that of the cash, the currency should be specified
in TransferCurrency.
35.4.14.10.2.3  OtherAsset <OthrAsst>
Presence: [1..1]
Definition: Identification of another kind of asset in the holding that is not a security or cash.
OtherAsset <OthrAsst> contains the following elements (see "OtherAsset2" on page 4525 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OtherAssetType <OthrAsstTp> [1..1]  4525
{Or     Code <Cd> [1..1] CodeSet 4525
Or}     Proprietary <Prtry> [1..1] ± 4526
   Identification <Id> [1..1] Text 4526
   Name <Nm> [0..1] Text 4526
   Description <Desc> [0..1] Text 4526
   OtherIdentification <OthrId> [0..5] Text 4526
   AdditionalInformation <AddtlInf> [0..*] ± 4527
35.4.14.10.3  Quantity <Qty>
Presence: [0..1]
Definition: Quantity of asset to be transferred.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1026 May 2026
```

