---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["30 camt.069.001.05 GetStandingOrderV05", "30.3 Constraints"]
file_pages: [688]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.069.001.05"]
topic_continuations: [{"constraint_ids": ["C5", "C6", "C7", "C8", "C9"], "until_heading": "30.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 689, "topic": "30.3 Constraints", "reference_path": "domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00527.md"}]
---

# 30.3 Constraints

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 688 to 688.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 30.3 Constraints topic continues in [Constraints continuation C5–C9 (file p689)](section-00527.md#file-page-689). Read the text before **30.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 688

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           SystemMemberIndicator <SysMmbInd> [0..1] Indicator 702
           ResponsiblePartyIndicator <RspnsblPtyInd> [0..1] Indicator 703
           CurrencyIndicator <CcyInd> [0..1] Indicator 703
           DebtorAccountIndicator <DbtrAcctInd> [0..1] Indicator 703
           CreditorAccountIndicator <CdtrAcctInd> [0..1] Indicator 703
           AssociatedPoolAccount <AssoctdPoolAcct> [0..1] Indicator 703
           FrequencyIndicator <FrqcyInd> [0..1] Indicator 704
           ExecutionTypeIndicator <ExctnTpInd> [0..1] Indicator 704
           ValidityFromIndicator <VldtyFrInd> [0..1] Indicator 704
           ValidToIndicator <VldToInd> [0..1] Indicator 704
           LinkSetIdentificationIndicator <LkSetIdInd> [0..1] Indicator 704
           LinkSetOrderIdentificationIndicator <LkSetOrdrIdInd> [0..1] Indicator 704
           LinkSetOrderSequenceIndicator <LkSetOrdrSeqInd> [0..1] Indicator 705
           TotalAmountIndicator <TtlAmtInd> [0..1] Indicator 705
           ZeroSweepIndicator <ZeroSweepInd> [0..1] Indicator 705
   SupplementaryData <SplmtryData> [0..*] ± C9 705
30.3 Constraints
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
C3 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C4 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
Approved by the Payments SEG on 04 February 2025 camt.069.001.05 GetStandingOrderV05
Cash Management - Maintenance 2024 - 2025 688 February 2025
```

