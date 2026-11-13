---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["16 camt.078.001.02 IntraBalanceMovementQueryV02", "16.3 Constraints"]
file_pages: [345]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
topic_continuations: [{"constraint_ids": ["C5", "C6", "C7", "C8", "C9", "C10"], "until_heading": "16.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 346, "topic": "16.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00265.md"}]
---

# 16.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 345 to 345.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 16.3 Constraints topic continues in [Constraints continuation C5–C10 (file p346)](section-00265.md#file-page-346). Read the text before **16.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 345

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       MessageOriginator <MsgOrgtr> [0..*] ± 377
       CreationDateTime <CreDtTm> [0..1]  378
{Or         Date <Dt> [1..1]  378
{Or           FromDate <FrDt> [1..1] Date 378
Or           ToDate <ToDt> [1..1] Date 379
Or           FromToDate <FrToDt> [1..1] ± 379
Or           EqualDate <EQDt> [1..1] Date 379
Or}           NotEqualDate <NEQDt> [1..1] Date 379
Or}         DateTime <DtTm> [1..1]  379
{Or           FromDateTime <FrDtTm> [1..1] DateTime 379
Or           ToDateTime <ToDtTm> [1..1] DateTime 380
Or           FromToDateTime <FrToDtTm> [1..1] ± 380
Or           EqualDateTime <EQDtTm> [1..1] DateTime 380
Or}           NotEqualDateTime <NEQDtTm> [1..1] DateTime 380
   SupplementaryData <SplmtryData> [0..*] ± C10 380
16.3 Constraints
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities 345 August 2026
```

