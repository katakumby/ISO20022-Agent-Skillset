---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.21 Quantity", "35.1.21.12 QuantityBreakdown62", "35.1.21.12.5 TypeOfPrice <TpOfPric>"]
file_pages: [1735]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.21.12.5 TypeOfPrice <TpOfPric>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1735 to 1735.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1735

```text
LotPrice <LotPric> contains the following elements (see "Price7" on page 1715 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 1716
   Value <Val> [1..1] ± 1716
35.1.21.12.5  TypeOfPrice <TpOfPric>
Presence: [0..1]
Definition: Specifies the type of price and information about the price.
TypeOfPrice <TpOfPric> contains one of the following elements (see "TypeOfPrice29Choice" on
page 1711 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1711
Or}   Proprietary <Prtry> [1..1] ± 1711
35.1.21.13  BalanceQuantity14Choice
Definition: Choice between quantity formats for the balance information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C12 1735
Or}   Proprietary <Prtry> [1..1] ± 1736
35.1.21.13.1  Quantity <Qty>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
Impacted by: C12 "DigitalTokenUnitUsageRule"
Quantity <Qty> contains one of the following elements (see "FinancialInstrumentQuantity33Choice" on
page 1726 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1726
Or   FaceAmount <FaceAmt> [1..1] Amount 1726
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1726
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1727
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1735 March 2026
```

