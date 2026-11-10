---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.21 Quantity", "35.1.21.8 QuantityBreakdown58", "35.1.21.8.8 AlternateReportingCurrencyAmounts <AltrnRptgCcyAmts>"]
file_pages: [1730]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.21.8.8 AlternateReportingCurrencyAmounts <AltrnRptgCcyAmts>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1730 to 1730.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1730

```text
InstrumentCurrencyAmounts <InstrmCcyAmts> contains the following elements (see
"BalanceAmounts2" on page 1421 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldingValue <HldgVal> [1..1] ± 1421
   BookValue <BookVal> [0..1] ± 1421
   UnrealisedGainLoss <UrlsdGnLoss> [0..1] ± 1421
35.1.21.8.8  AlternateReportingCurrencyAmounts <AltrnRptgCcyAmts>
Presence: [0..1]
Definition: Valuation amounts for the lot provided in a currency other than the base currency of the
account.
AlternateReportingCurrencyAmounts <AltrnRptgCcyAmts> contains the following elements (see
"BalanceAmounts2" on page 1421 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldingValue <HldgVal> [1..1] ± 1421
   BookValue <BookVal> [0..1] ± 1421
   UnrealisedGainLoss <UrlsdGnLoss> [0..1] ± 1421
35.1.21.9  SubBalanceQuantity8Choice
Definition: Choice between formats for the balance information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C12 1730
Or   Proprietary <Prtry> [1..1] ± 1731
Or}   QuantityAndAvailability <QtyAndAvlbty> [1..1] ± 1731
35.1.21.9.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Impacted by: C12 "DigitalTokenUnitUsageRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1730 March 2026
```

