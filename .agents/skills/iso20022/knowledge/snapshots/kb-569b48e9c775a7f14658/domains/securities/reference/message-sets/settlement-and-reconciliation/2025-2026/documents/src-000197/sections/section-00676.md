---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks", "29.4.6 QuantityAndAccountDetails <QtyAndAcctDtls>", "29.4.6.2 PreviouslySettledQuantity <PrevslySttldQty>"]
file_pages: [1020]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4.6.2 PreviouslySettledQuantity <PrevslySttldQty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1020 to 1020.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1020

```text
SettledQuantity <SttldQty> contains one of the following elements (see "Quantity51Choice" on
page 1725 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C12 1725
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 1726
29.4.6.2  PreviouslySettledQuantity <PrevslySttldQty>
Presence: [0..1]
Definition: Quantity of financial instrument previously settled.
Impacted by: C20 "DigitalTokenUnitUsageRule"
PreviouslySettledQuantity <PrevslySttldQty> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1726 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1726
Or   FaceAmount <FaceAmt> [1..1] Amount 1726
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1726
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1727
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
29.4.6.3  RemainingToBeSettledQuantity <RmngToBeSttldQty>
Presence: [0..1]
Definition: Quantity of financial instrument remaining to be settled.
Impacted by: C20 "DigitalTokenUnitUsageRule"
RemainingToBeSettledQuantity <RmngToBeSttldQty> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1726 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1726
Or   FaceAmount <FaceAmt> [1..1] Amount 1726
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1726
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1727
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1020 March 2026
```

