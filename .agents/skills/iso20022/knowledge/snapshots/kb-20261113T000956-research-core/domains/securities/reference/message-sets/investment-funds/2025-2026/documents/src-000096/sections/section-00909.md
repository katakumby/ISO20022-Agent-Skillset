---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "36.4.15.11.10 UnitsDetails <UnitsDtls>", "36.4.15.11.10.8 TransactionOverhead <TxOvrhd>", "36.4.15.11.10.8.7 DigitalNetworkFee <DgtlNtwkFee>", "36.4.15.11.10.8.7.2 Quantity <Qty>", "36.4.15.11.10.8.7.2.2 ProprietaryQuantity <PrtryQty>", "36.4.15.11.10.8.7.2.2.1 Quantity <Qty>"]
file_pages: [1252]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.11.10.8.7.2.2.1 Quantity <Qty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1252 to 1252.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1252

```text
ProprietaryQuantity <PrtryQty> contains the following ProprietaryQuantity8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] Quantity 1252
   QuantityType <QtyTp> [1..1] Text 1252
   Issuer <Issr> [1..1] Text 1252
   SchemeName <SchmeNm> [0..1] Text 1252
36.4.15.11.10.8.7.2.2.1  Quantity <Qty>
Presence: [1..1]
Definition: Provides the proprietary quantity with a decimal number.
Datatype: "DecimalNumber" on page 5400
36.4.15.11.10.8.7.2.2.2  QuantityType <QtyTp>
Presence: [1..1]
Definition: Identifies the type of proprietary quantity reported.
Datatype: "Exact4AlphaNumericText" on page 5402
36.4.15.11.10.8.7.2.2.3  Issuer <Issr>
Presence: [1..1]
Definition: Provides information related to issuer in free format.
Datatype: "Max35Text" on page 5403
36.4.15.11.10.8.7.2.2.4  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 5403
36.4.15.11.10.8.7.3  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of settlement expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 5392
36.4.15.11.10.9  OtherAmount <OthrAmt>
Presence: [0..*]
Definition: Amount not covered in the price, fee or tax.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1252 May 2026
```

