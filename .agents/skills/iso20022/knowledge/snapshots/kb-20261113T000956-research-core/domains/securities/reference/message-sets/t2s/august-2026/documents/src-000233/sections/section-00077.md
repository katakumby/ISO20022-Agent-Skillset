---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02", "8.3 Constraints"]
file_pages: [117]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.067.001.02"]
topic_continuations: [{"constraint_ids": ["C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15"], "until_heading": "8.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 118, "topic": "8.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00078.md"}]
---

# 8.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 117 to 117.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 8.3 Constraints topic continues in [Constraints continuation C6–C15 (file p118)](section-00078.md#file-page-118). Read the text before **8.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 117

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     BalanceTo <BalTo> [1..1]  129
       Type <Tp> [1..1]  129
{Or         Code <Cd> [1..1] CodeSet 129
Or}         Proprietary <Prtry> [1..1] ± 129
       QuantityBreakdown <QtyBrkdwn> [0..*]  130
         LotNumber <LotNb> [0..1] ± 130
         LotAmount <LotAmt> [0..1] ± 130
         LotQuantity <LotQty> [0..1] ± 131
         CashSubBalanceType <CshSubBalTp> [0..1] ± 131
     CashSubBalanceIdentification <CshSubBalId> [0..1] ± 131
     Priority <Prty> [0..1] ± 131
     InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls> [0..1] Text 132
   SupplementaryData <SplmtryData> [0..*] ± C15 132
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
C5 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities 117 August 2026
```

