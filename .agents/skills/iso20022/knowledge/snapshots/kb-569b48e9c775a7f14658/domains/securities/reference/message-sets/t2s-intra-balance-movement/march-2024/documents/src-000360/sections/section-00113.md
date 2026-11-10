---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["8 camt.075.001.02 IntraBalanceMovementCancellationRequestStatusAdviceV02", "8.3 Constraints"]
file_pages: [135]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.075.001.02"]
---

# 8.3 Constraints

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 135 to 135.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 135

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         CashSubBalanceType <CshSubBalTp> [0..1] ± 145
     BalanceTo <BalTo> [1..1]  146
       Type <Tp> [1..1]  146
{Or         Code <Cd> [1..1] CodeSet 146
Or}         Proprietary <Prtry> [1..1] ± 146
       QuantityBreakdown <QtyBrkdwn> [0..*]  147
         LotNumber <LotNb> [0..1] ± 147
         LotAmount <LotAmt> [0..1] ± 147
         LotQuantity <LotQty> [0..1] ± 148
         CashSubBalanceType <CshSubBalTp> [0..1] ± 148
     CashSubBalanceIdentification <CshSubBalId> [0..1] ± 148
     Priority <Prty> [0..1] ± 148
     InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls> [0..1] Text 149
   SupplementaryData <SplmtryData> [0..*] ± C13 149
8.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 AdditionalDetailsRule
Unless bilaterally agreed between the sender and the receiver, if
InstructionProcessingAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
C4 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.075.001.02
IntraBalanceMovementCancellationRequestStatusA
dviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
135 March 2024
```

