---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.23 DigitalAssetSettlement <DgtlAsstSttlm>", "50.4.4.9.23.2 Quantity <Qty>", "50.4.4.9.23.2.2 ProprietaryQuantity <PrtryQty>", "50.4.4.9.23.2.2.1 Quantity <Qty>"]
file_pages: [3177]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.23.2.2.1 Quantity <Qty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3177 to 3177.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3177

```text
ProprietaryQuantity <PrtryQty> contains the following ProprietaryQuantity8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] Quantity 3177
   QuantityType <QtyTp> [1..1] Text 3177
   Issuer <Issr> [1..1] Text 3177
   SchemeName <SchmeNm> [0..1] Text 3177
50.4.4.9.23.2.2.1  Quantity <Qty>
Presence: [1..1]
Definition: Provides the proprietary quantity with a decimal number.
Datatype: "DecimalNumber" on page 5400
50.4.4.9.23.2.2.2  QuantityType <QtyTp>
Presence: [1..1]
Definition: Identifies the type of proprietary quantity reported.
Datatype: "Exact4AlphaNumericText" on page 5402
50.4.4.9.23.2.2.3  Issuer <Issr>
Presence: [1..1]
Definition: Provides information related to issuer in free format.
Datatype: "Max35Text" on page 5403
50.4.4.9.23.2.2.4  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 5403
50.4.4.9.23.3  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of settlement expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 5392
50.4.4.9.24  NonStandardSettlementInformation <NonStdSttlmInf>
Presence: [0..1]
Definition: Additional specific settlement information for non-regulated traded funds.
Datatype: "Max350Text" on page 5403
50.4.4.9.25  StaffClientBreakdown <StffClntBrkdwn>
Presence: [0..4]
Definition: Breakdown of the net amount per type of order.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3177 May 2026
```

