---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.21 Quantity", "35.1.21.8 QuantityBreakdown58"]
file_pages: [1728]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.21.8 QuantityBreakdown58

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1728 to 1728.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1728

```text
35.1.21.8  QuantityBreakdown58
Definition: Details of breakdown of a quantity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 1728
   LotQuantity <LotQty> [0..1] ± 1728
   LotDateTime <LotDtTm> [0..1] ± 1728
   LotPrice <LotPric> [0..1] ± 1729
   TypeOfPrice <TpOfPric> [0..1] ± 1729
   AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [0..1] ± 1729
   InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± 1729
   AlternateReportingCurrencyAmounts
<AltrnRptgCcyAmts>
[0..1] ± 1730
35.1.21.8.1  LotNumber <LotNb>
Presence: [0..1]
Definition: Identification, for tax purposes, of a lot of identical securities that are bought at a certain date
and at a certain price.
LotNumber <LotNb> contains the following elements (see "GenericIdentification37" on page 1498 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1498
   Issuer <Issr> [0..1] Text 1498
35.1.21.8.2  LotQuantity <LotQty>
Presence: [0..1]
Definition: Quantity of financial instruments that is part of the lot described.
LotQuantity <LotQty> contains the following elements (see "Balance16" on page 1423 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [0..1] CodeSet 1423
   Quantity <Qty> [1..1] ± 1424
35.1.21.8.3  LotDateTime <LotDtTm>
Presence: [0..1]
Definition: Date/time at which the lot was purchased.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1728 March 2026
```

