---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.3 Constraints"]
file_pages: [106, 107]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
topic_continuations: [{"constraint_ids": ["C13", "C14", "C15", "C16", "C17", "C18"], "until_heading": "4.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 108, "topic": "4.3 Constraints", "reference_path": "domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00065.md"}]
---

# 4.3 Constraints

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 106 to 107.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 4.3 Constraints topic continues in [Constraints continuation C13–C18 (file p108)](section-00065.md#file-page-108). Read the text before **4.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 106

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             PaymentMethodIndicator <PmtMtdInd> [0..1] Indicator 203
             DebtorIndicator <DbtrInd> [0..1] Indicator 203
             DebtorAgentIndicator <DbtrAgtInd> [0..1] Indicator 204
             InstructingReimbursementAgentIndicator
<InstgRmbrsmntAgtInd>
[0..1] Indicator 204
             InstructedReimbursementAgentIndicator
<InstdRmbrsmntAgtInd>
[0..1] Indicator 204
             IntermediaryIndicator <IntrmyInd> [0..1] Indicator 204
             CreditorAgentIndicator <CdtrAgtInd> [0..1] Indicator 204
             CreditorIndicator <CdtrInd> [0..1] Indicator 205
   SupplementaryData <SplmtryData> [0..*] ± C16 205
4.3 Constraints
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
C3 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C4 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C5 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C6 EntryAmountCreditDebitIndicator1Rule
If at least one occurrence of EntryAmount/CurrencyAndAmountRange/CreditDebitIndicator is
present, then CreditDebitIndicator is not allowed.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 106 February 2025
```

## File page 107

```text
If EntryAmount/CurrencyAndAmountRange/CreditDebitIndicator is not present, then
CreditDebitIndicator is optional.
If CreditDebitIndicator is present then
all occurrences of EntryAmount/CurrencyAndAmountRange/CreditDebitIndicator must be
absent and
all occurrences of EntryAmount/ImpliedCurrencyAndAmountRange/CreditDebitIndicator must
be absent.
C7 EntryAmountCreditDebitIndicator2Rule
If at least one occurrence of EntryAmount/ImpliedCurrencyAndAmountRange/
CreditDebitIndicator is present, then CreditDebitIndicator is not allowed.
If EntryAmount/ImpliedCurrencyAndAmountRange/CreditDebitIndicator is not present, then
CreditDebitIndicator is optional.
C8 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C9 InstructedAmountCreditDebitIndicator1Rule
If at least one occurrence of InstructedAmount/CurrencyAndAmountRange/CreditDebitIndicator
is present, then CreditDebitIndicator is not allowed.
If InstructedAmount/CurrencyAndAmountRange/CreditDebitIndicator is not present, then
CreditDebitIndicator is optional.
C10 InstructedAmountCreditDebitIndicator2Rule
If at least one occurrence of InstructedAmount/ImpliedCurrencyAndAmountRange/
CreditDebitIndicator is present, then CreditDebitIndicator is not allowed.
If InstructedAmount/ImpliedCurrencyAndAmountRange/CreditDebitIndicator is not present, then
CreditDebitIndicator is optional.
C11 InstructedAmountCurrencyRule
If at least one occurrence of InstructedAmount/CurrencyAndAmountRange is present, then no
occurrence of InstructedAmountCurrency is allowed.
If InstructedAmount/CurrencyAndAmountRange is not present, then any occurrence of
InstructedAmountCurrency is optional.
C12 SearchAndReturnCriteriaAndStatementReportRule
The following combinations are allowed: only Search Criteria, or only Return Criteria, or only a
Statement Report, or a combination of Search and Return criteria, or a combination of Search
criteria and a Statement Report.
Rule rationale:
- If ReturnCriteria are present, they define the expected report.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 107 February 2025
```

