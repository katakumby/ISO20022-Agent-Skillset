---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.16 RedemptionLegDetails <RedLegDtls>", "53.4.5.16.13 DigitalAssetSettlement <DgtlAsstSttlm>", "53.4.5.16.13.2 Quantity <Qty>", "53.4.5.16.13.2.2 ProprietaryQuantity <PrtryQty>", "53.4.5.16.13.2.2.1 Quantity <Qty>"]
file_pages: [3612]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.16.13.2.2.1 Quantity <Qty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3612 to 3612.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3612

```text
ProprietaryQuantity <PrtryQty> contains the following ProprietaryQuantity8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] Quantity 3612
   QuantityType <QtyTp> [1..1] Text 3612
   Issuer <Issr> [1..1] Text 3612
   SchemeName <SchmeNm> [0..1] Text 3612
53.4.5.16.13.2.2.1  Quantity <Qty>
Presence: [1..1]
Definition: Provides the proprietary quantity with a decimal number.
Datatype: "DecimalNumber" on page 5400
53.4.5.16.13.2.2.2  QuantityType <QtyTp>
Presence: [1..1]
Definition: Identifies the type of proprietary quantity reported.
Datatype: "Exact4AlphaNumericText" on page 5402
53.4.5.16.13.2.2.3  Issuer <Issr>
Presence: [1..1]
Definition: Provides information related to issuer in free format.
Datatype: "Max35Text" on page 5403
53.4.5.16.13.2.2.4  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 5403
53.4.5.16.13.3  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of settlement expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 5392
53.4.5.16.14  NonStandardSettlementInformation <NonStdSttlmInf>
Presence: [0..1]
Definition: Additional specific settlement information for non-regulated traded funds.
Datatype: "Max350Text" on page 5403
53.4.5.16.15  Equalisation <Equlstn>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3612 May 2026
```

