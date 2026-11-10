---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.25 Securities Quantity", "7.1.25.2 OriginalAndCurrentQuantities1"]
file_pages: [519]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.25.2 OriginalAndCurrentQuantities1

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 519 to 519.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 519

```text
7.1.25.2  OriginalAndCurrentQuantities1
Definition: Original and current value of an asset-back instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FaceAmount <FaceAmt> [1..1] Amount 519
   AmortisedValue <AmtsdVal> [1..1] Amount 519
7.1.25.2.1  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, that is, the principal of a
debt instrument.
Datatype: "ImpliedCurrencyAndAmount" on page 613
7.1.25.2.2  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Datatype: "ImpliedCurrencyAndAmount" on page 613
7.1.25.3  QuantityBreakdown76
Definition: Details of breakdown of a quantity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 519
   LotQuantity <LotQty> [0..1] ± 520
   LotDateTime <LotDtTm> [0..1] ± 520
   LotPrice <LotPric> [0..1] ± 520
7.1.25.3.1  LotNumber <LotNb>
Presence: [0..1]
Definition: Identification, for tax purposes, of a lot of identical securities that are bought at a certain date
and at a certain price.
LotNumber <LotNb> contains the following elements (see "GenericIdentification37" on page 280 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 280
   Issuer <Issr> [0..1] Text 280
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 519 February 2025
```

