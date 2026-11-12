---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 camt.003.001.08 GetAccountV08", "2.3 Constraints"]
file_pages: [17]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.003.001.08"]
topic_continuations: [{"constraint_ids": ["C7", "C8", "C9", "C10"], "until_heading": "2.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 18, "topic": "2.3 Constraints", "reference_path": "domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00007.md"}]
---

# 2.3 Constraints

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 17 to 17.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 2.3 Constraints topic continues in [Constraints continuation C7–C10 (file p18)](section-00007.md#file-page-18). Read the text before **2.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 17

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           BilateralBalanceReturnCriteria <BilBalRtrCrit> [0..1]  44
             TypeIndicator <TpInd> [1..1] Indicator 45
             StatusIndicator <StsInd> [1..1] Indicator 45
             ValueDateIndicator <ValDtInd> [1..1] Indicator 45
             ProcessingDateIndicator <PrcgDtInd> [1..1] Indicator 45
             NumberOfPaymentsIndicator <NbOfPmtsInd> [1..1] Indicator 46
           StandingOrderIndicator <StgOrdrInd> [0..1] Indicator 46
           AccountOwnerIndicator <AcctOwnrInd> [0..1] Indicator 46
           AccountServicerIndicator <AcctSvcrInd> [0..1] Indicator 46
   SupplementaryData <SplmtryData> [0..*] ± C10 46
2.3 Constraints
C1 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C2 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C3 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C4 CashAccountIdentificationGuideline
If the account identification identifies a group of accounts with different types or in different
currencies, the currency and/or the account type can be used as additional search criteria.
C5 CounterpartyIdentification1Rule
If at least one occurrence of CounterpartyType is present and is equal to Multilateral (MULT),
then no occurrence of CounterpartyIdentification is allowed.
If CounterpartyType is not present, then any occurrence of CounterpartyIdentification is
optional.
C6 CounterpartyIdentification2Rule
If at least one occurrence of CounterpartyType is present and is equal to Bilateral (BILA), then
at least one occurrence of CounterpartyIdentification must be present.
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 17 February 2025
```

