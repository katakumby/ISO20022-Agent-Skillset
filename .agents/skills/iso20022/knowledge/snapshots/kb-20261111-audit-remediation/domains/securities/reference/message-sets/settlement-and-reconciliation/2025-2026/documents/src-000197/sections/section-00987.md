---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.4 Balance", "35.1.4.11 SecuritiesSubBalanceTypeAndQuantityBreakdown5"]
file_pages: [1423]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.4.11 SecuritiesSubBalanceTypeAndQuantityBreakdown5

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1423 to 1423.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1423

```text
35.1.4.11  SecuritiesSubBalanceTypeAndQuantityBreakdown5
Definition: Quantity breakdown information for a specific securities balance.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 1423
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 1423
35.1.4.11.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the securities sub balance type indicator (example restriction type for a market
infrastructure).
Type <Tp> contains one of the following elements (see "SecuritiesBalanceType6Choice" on page 1427
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1427
Or}   Proprietary <Prtry> [1..1] ± 1429
35.1.4.11.2  QuantityBreakdown <QtyBrkdwn>
Presence: [0..*]
Definition: Breakdown of a quantity into lots such as tax lots, instrument series.
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown61" on
page 1724 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 1724
   LotQuantity <LotQty> [0..1] ± C12 1724
   SecuritiesSubBalanceType <SctiesSubBalTp> [0..1] ± 1725
35.1.4.12  Balance16
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account. A securities balance is calculated from the sum of securities' receipts minus the sum
of securities' deliveries.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [0..1] CodeSet 1423
   Quantity <Qty> [1..1] ± 1424
35.1.4.12.1  ShortLongIndicator <ShrtLngInd>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1423 March 2026
```

