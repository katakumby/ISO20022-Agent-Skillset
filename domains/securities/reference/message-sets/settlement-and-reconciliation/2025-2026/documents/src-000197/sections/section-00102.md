---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 semt.013.001.07 IntraPositionMovementInstructionV07", "4.4 Message Building Blocks", "4.4.11 IntraPositionDetails <IntraPosDtls>", "4.4.11.1 Priority <Prty>"]
file_pages: [147]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.013.001.07"]
---

# 4.4.11.1 Priority <Prty>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 147 to 147.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 147

```text
IntraPositionDetails <IntraPosDtls> contains the following IntraPositionDetails58 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Priority <Prty> [0..1] ± 147
   SettlementQuantity <SttlmQty> [1..1] ± C12 147
   SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 148
   SettlementDate <SttlmDt> [1..1] ± 148
   BalanceFrom <BalFr> [1..1] ± 148
   BalanceTo <BalTo> [1..1] ± 149
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 149
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if InstructionProcessingAdditionalDetails
is present, then it must not contain information that can be provided in a structured field.
• BalanceFromToRule
The SecuritiesBalanceType of BalanceFrom must be different from the SecuritiesBalanceType of
BalanceTo.
On Condition
    /BalanceFrom/Type/Code is present
 And    /BalanceTo/Type/Code is present
Following Must be True
    /BalanceFrom/Type/Code Must be different from /BalanceTo/Type/Code
4.4.11.1  Priority <Prty>
Presence: [0..1]
Definition: Specifies whether the transaction is to be executed with a high priority.
Priority <Prty> contains one of the following elements (see "PriorityNumeric4Choice" on page 1541 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 1541
Or}   Proprietary <Prtry> [1..1] ± 1541
4.4.11.2  SettlementQuantity <SttlmQty>
Presence: [1..1]
Definition: Total quantity of securities to be settled.
Impacted by: C12 "DigitalTokenUnitUsageRule"
Approved by the Securities SEG on 27 January 2026 semt.013.001.07
IntraPositionMovementInstructionV07
Settlement And Reconciliation - Maintenance 2025 - 2026 147 March 2026
```

