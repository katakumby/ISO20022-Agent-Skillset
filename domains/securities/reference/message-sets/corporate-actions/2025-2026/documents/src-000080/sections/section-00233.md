---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.9 CorporateActionInstruction <CorpActnInstr>", "5.4.9.12 SecuritiesQuantityOrInstructedAmount <SctiesQtyOrInstdAmt>", "5.4.9.12.1 SecuritiesQuantity <SctiesQty>", "5.4.9.12.1.1 ConditionalQuantity <CondlQty>"]
file_pages: [310]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.9.12.1.1 ConditionalQuantity <CondlQty>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 310 to 310.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 310

```text
SecuritiesQuantity <SctiesQty> contains the following SecuritiesOption79 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ConditionalQuantity <CondlQty> [0..1] ± C12 310
   InstructedQuantity <InstdQty> [1..1] ± 310
   AdditionalRoundUpQuantity <AddtlRndUpQty> [0..1] ± C12 310
5.4.9.12.1.1  ConditionalQuantity <CondlQty>
Presence: [0..1]
Definition: Minimum quantity of securities to be accepted (used in the framework of conditional privilege
on election). In case of proration, if this minimum quantity is not reached then the instruction is void.
Impacted by: C12 "DigitalTokenUnitUsageRule"
ConditionalQuantity <CondlQty> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1091 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1092
Or   FaceAmount <FaceAmt> [1..1] Amount 1092
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1092
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1092
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
5.4.9.12.1.2  InstructedQuantity <InstdQty>
Presence: [1..1]
Definition: Quantity of securities to which this instruction applies.
InstructedQuantity <InstdQty> contains one of the following elements (see "Quantity52Choice" on
page 1097 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1097
Or   OriginalAndCurrentFaceAmount <OrgnlAndCurFaceAmt> [1..1] ± 1097
Or}   Quantity <Qty> [1..1] ± C13 1098
5.4.9.12.1.3  AdditionalRoundUpQuantity <AddtlRndUpQty>
Presence: [0..1]
Definition: Quantity of additional shares requested due to the difference of "round-up against payment"
practice between the account servicer and the account holder (for instance for French dividend option).
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 310 February 2026
```

