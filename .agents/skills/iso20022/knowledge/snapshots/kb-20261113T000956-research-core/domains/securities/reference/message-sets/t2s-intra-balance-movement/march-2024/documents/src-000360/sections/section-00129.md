---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["9 camt.078.001.02 IntraBalanceMovementQueryV02", "9.3 Constraints"]
file_pages: [154]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
topic_continuations: [{"constraint_ids": ["C5", "C6", "C7", "C8", "C9", "C10"], "until_heading": "9.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 155, "topic": "9.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00130.md"}]
---

# 9.3 Constraints

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 154 to 154.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 9.3 Constraints topic continues in [Constraints continuation C5–C10 (file p155)](section-00130.md#file-page-155). Read the text before **9.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 154

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       MessageOriginator <MsgOrgtr> [0..*] ± 186
       CreationDateTime <CreDtTm> [0..1]  187
{Or         Date <Dt> [1..1]  187
{Or           FromDate <FrDt> [1..1] Date 187
Or           ToDate <ToDt> [1..1] Date 188
Or           FromToDate <FrToDt> [1..1] ± 188
Or           EqualDate <EQDt> [1..1] Date 188
Or}           NotEqualDate <NEQDt> [1..1] Date 188
Or}         DateTime <DtTm> [1..1]  188
{Or           FromDateTime <FrDtTm> [1..1] DateTime 188
Or           ToDateTime <ToDtTm> [1..1] DateTime 189
Or           FromToDateTime <FrToDtTm> [1..1] ± 189
Or           EqualDateTime <EQDtTm> [1..1] DateTime 189
Or}           NotEqualDateTime <NEQDtTm> [1..1] DateTime 189
   SupplementaryData <SplmtryData> [0..*] ± C10 189
9.3 Constraints
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
C3 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C4 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
154 March 2024
```

