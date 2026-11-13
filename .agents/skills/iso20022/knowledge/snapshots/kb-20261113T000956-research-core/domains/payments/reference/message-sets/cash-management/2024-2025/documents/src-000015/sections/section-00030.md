---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10", "3.3 Constraints"]
file_pages: [52]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
topic_continuations: [{"constraint_ids": ["C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11"], "until_heading": "3.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 53, "topic": "3.3 Constraints", "reference_path": "domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00031.md"}]
---

# 3.3 Constraints

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 52 to 52.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 3.3 Constraints topic continues in [Constraints continuation C2–C11 (file p53)](section-00031.md#file-page-53). Read the text before **3.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 52

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
                 Currency <Ccy> [0..1] CodeSet C1 91
               PendingPredefinedOrder <PdgPrdfndOrdr> [1..1]  91
                 TotalAmount <TtlAmt> [1..1] Amount 92
                 CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 92
                 Currency <Ccy> [0..1] CodeSet C1 92
               SetStandingOrder <SetStgOrdr> [1..1]  92
                 TotalAmount <TtlAmt> [1..1] Amount 93
                 CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 93
                 Currency <Ccy> [0..1] CodeSet C1 93
               PendingStandingOrder <PdgStgOrdr> [1..1]  93
                 TotalAmount <TtlAmt> [1..1] Amount 94
                 CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 94
                 Currency <Ccy> [0..1] CodeSet C1 94
             ZeroSweepIndicator <ZeroSweepInd> [0..1] Indicator 94
Or}         BusinessError <BizErr> [1..*]  95
           Error <Err> [1..1]  95
{Or             Code <Cd> [1..1] CodeSet 95
Or}             Proprietary <Prtry> [1..1] Text 95
           Description <Desc> [0..1] Text 95
Or}     OperationalError <OprlErr> [1..*]  95
       Error <Err> [1..1]  96
{Or         Code <Cd> [1..1] CodeSet 96
Or}         Proprietary <Prtry> [1..1] Text 96
       Description <Desc> [0..1] Text 96
   SupplementaryData <SplmtryData> [0..*] ± C11 96
3.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 52 February 2025
```

