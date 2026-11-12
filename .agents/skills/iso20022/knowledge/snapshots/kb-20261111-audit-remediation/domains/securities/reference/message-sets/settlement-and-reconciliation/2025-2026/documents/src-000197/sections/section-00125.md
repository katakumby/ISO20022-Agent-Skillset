---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 semt.015.001.10 IntraPositionMovementConfirmationV10", "6.4 Message Building Blocks", "6.4.9 IntraPositionDetails <IntraPosDtls>", "6.4.9.1 SettledQuantity <SttldQty>"]
file_pages: [173]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.015.001.10"]
---

# 6.4.9.1 SettledQuantity <SttldQty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 173 to 173.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 173

```text
IntraPositionDetails <IntraPosDtls> contains the following IntraPositionDetails65 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettledQuantity <SttldQty> [1..1] ± C12 173
   SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 174
   CollateralMonitorAmount <CollMntrAmt> [0..1] ± 174
   PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± C12 174
   RemainingToBeSettledQuantity <RmngToBeSttldQty> [0..1] ± C12 175
   SettlementDate <SttlmDt> [1..1] ± 175
   AvailableDate <AvlblDt> [0..1] ± 176
   CorporateActionEventType <CorpActnEvtTp> [0..1] ± C13 176
   BalanceFrom <BalFr> [1..1] ± 176
   BalanceTo <BalTo> [1..1] ± 177
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 177
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if InstructionProcessingAdditionalDetails
is present, then it must not contain information that can be provided in a structured field.
• BalanceFromToRule
The BalanceFrom/Type must be different from the BalanceTo/Type.
On Condition
    /BalanceFrom/Type/Code is present
 And    /BalanceTo/Type/Code is present
Following Must be True
    /BalanceFrom/Type/Code Must be different from /BalanceTo/Type/Code
6.4.9.1  SettledQuantity <SttldQty>
Presence: [1..1]
Definition: Quantity of financial instrument effectively settled.
Impacted by: C12 "DigitalTokenUnitUsageRule"
Approved by the Securities SEG on 27 January 2026 semt.015.001.10
IntraPositionMovementConfirmationV10
Settlement And Reconciliation - Maintenance 2025 - 2026 173 March 2026
```

