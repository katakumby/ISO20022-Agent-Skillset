---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.3 Constraints"]
file_pages: [140, 141, 142]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
topic_continuations: [{"constraint_ids": ["C32", "C33", "C34", "C35", "C36", "C37", "C38", "C39"], "until_heading": "3.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 143, "topic": "3.3 Constraints", "reference_path": "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00101.md"}]
---

# 3.3 Constraints

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 140 to 142.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 3.3 Constraints topic continues in [Constraints continuation C32–C39 (file p143)](section-00101.md#file-page-143). Read the text before **3.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 140

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 244
     SupplementaryData <SplmtryData> [0..*] ± C32 244
   SupplementaryData <SplmtryData> [0..*] ± C32 0
3.3 Constraints
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
C3 AmendmentIndicatorFalseRule
If AmendmentIndicator is false, then AmendmentInformationDetails is not allowed.
C4 AmendmentIndicatorTrueRule
If AmendmentIndicator is true, then AmendmentInformationDetails must be present.
C5 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C6 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C7 ChargesAmountGuideline
If ChargesInformation is present, then the currency of ChargesInformation/ChargesAmount is
recommended to be the same as the currency of InterbankSettlementAmount.
C8 ChargesInformationAndInstructedAmountRule
If ChargesInformation is present, then InstructedAmount must be present.
C9 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C10 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
140 March 2026
```

## File page 141

```text
Note: The decimal separator is a dot.
C11 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C12 GroupHeaderInterbankSettlementDateRule
If GroupHeader/InterbankSettlementDate is present, then DirectDebitTransactionInformation/
InterbankSettlementDate is not allowed.
On Condition
    /GroupHeader/InterbankSettlementDate is present
Following Must be True
    /DirectDebitTransactionInformation[*]/InterbankSettlementDate Must be 
absent
This constraint is defined at the MessageDefinition level.
C13 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C14 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C15 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C16 InstructedAgentRule
If GroupHeader/InstructedAgent is present, then DirectDebitTransactionInformation/
InstructedAgent is not allowed.
On Condition
    /GroupHeader/InstructedAgent is present
Following Must be True
    /DirectDebitTransactionInformation[*]/InstructedAgent Must be absent
This constraint is defined at the MessageDefinition level.
C17 InstructedAmountAndExchangeRate1Rule
If InstructedAmount is present and the currency is different from the currency in
InterbankSettlementAmount, then ExchangeRate must be present.
C18 InstructedAmountAndExchangeRate2Rule
If InstructedAmount is present and the currency is the same as the currency in
InterbankSettlementAmount, then ExchangeRate is not allowed.
C19 InstructedAmountAndExchangeRate3Rule
If InstructedAmount is not present, then ExchangeRate is not allowed.
C20 InstructingAgentRule
If GroupHeader/InstructingAgent is present, then DirectDebitTransactionInformation/
InstructingAgent is not allowed.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
141 March 2026
```

## File page 142

```text
On Condition
    /GroupHeader/InstructingAgent is present
Following Must be True
    /DirectDebitTransactionInformation[*]/InstructingAgent Must be absent
This constraint is defined at the MessageDefinition level.
C21 IntermediaryAgent1AccountRule
If IntermediaryAgent1Account is present, then IntermediaryAgent1 must be present.
C22 IntermediaryAgent2AccountRule
If IntermediaryAgent2Account is present, then IntermediaryAgent2 must be present.
C23 IntermediaryAgent2Rule
If IntermediaryAgent2 is present, then IntermediaryAgent1 must be present.
C24 IntermediaryAgent3AccountRule
If IntermediaryAgent3Account is present, then IntermediaryAgent3 must be present.
C25 IntermediaryAgent3Rule
If IntermediaryAgent3 is present, then IntermediaryAgent2 must be present.
C26 PaymentTypeInformationRule
If GroupHeader/PaymentTypeInformation is present, then DirectDebitTransactionInformation/
PaymentTypeInformation is not allowed.
On Condition
    /GroupHeader/PaymentTypeInformation is present
Following Must be True
    /DirectDebitTransactionInformation[*]/PaymentTypeInformation Must be 
absent
This constraint is defined at the MessageDefinition level.
C27 RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
C28 ReportingCodeAndInformationRule
Reporting code or information must be present. Both may be present.
C29 SettlementMethodAgentRule
If SettlementMethod is equal to INDA or INGA, then ClearingSystem is not allowed.
C30 SettlementMethodClearingRule
If SettlementMethod is equal to CLRG, then ClearingSystem must be present and
SettlementAccount is not allowed.
C31 SupplementaryDataRule
The SupplementaryData building block at message level must not be used to provide additional
information about a transaction. The SupplementaryData element at transaction level should be
used for that purpose.
This constraint is defined at the MessageDefinition level.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
142 March 2026
```

