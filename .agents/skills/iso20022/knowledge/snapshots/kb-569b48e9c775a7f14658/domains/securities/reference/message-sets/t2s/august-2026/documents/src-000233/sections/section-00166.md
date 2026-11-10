---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["13 camt.075.001.02 IntraBalanceMovementCancellationRequestStatusAdviceV02", "13.3 Constraints"]
file_pages: [218]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.075.001.02"]
---

# 13.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 218 to 218.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 218

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         CashSubBalanceType <CshSubBalTp> [0..1] ± 228
     BalanceTo <BalTo> [1..1]  229
       Type <Tp> [1..1]  229
{Or         Code <Cd> [1..1] CodeSet 229
Or}         Proprietary <Prtry> [1..1] ± 229
       QuantityBreakdown <QtyBrkdwn> [0..*]  230
         LotNumber <LotNb> [0..1] ± 230
         LotAmount <LotAmt> [0..1] ± 230
         LotQuantity <LotQty> [0..1] ± 231
         CashSubBalanceType <CshSubBalTp> [0..1] ± 231
     CashSubBalanceIdentification <CshSubBalId> [0..1] ± 231
     Priority <Prty> [0..1] ± 231
     InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls> [0..1] Text 232
   SupplementaryData <SplmtryData> [0..*] ± C13 232
13.3 Constraints
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.075.001.02
IntraBalanceMovementCancellationRequestStatusA
dviceV02
Target2-Securities 218 August 2026
```

