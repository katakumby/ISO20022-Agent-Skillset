---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.3 Constraints"]
file_pages: [842, 843, 844, 845, 846, 847]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.3 Constraints

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 842 to 847.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 842

```text
7.3 Constraints
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
C6 CreditorAgentAccountRule
If CreditorAgentAccount is present, then CreditorAgent must be present.
C7 CreditorAgentAccountRule
If CreditorAgentAccount is present, then CreditorAgent must be present.
C8 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 DebtorAgentAccountRule
If DebtorAgentAccount is present, then DebtorAgent must be present.
C11 DebtorAgentAccountRule
If DebtorAgentAccount is present, then DebtorAgent must be present.
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
842 March 2026
```

## File page 843

```text
C12 GroupHeaderExpiryDateTimeRule
If GroupHeader/ExpiryDateTime is present, then CreditTransferTransactionInformation/
ExpiryDateTime is not allowed.
On Condition
    /GroupHeader/ExpiryDateTime is present
Following Must be True
    /CreditTransferTransactionInformation[*]/ExpiryDateTime Must be absent
This constraint is defined at the MessageDefinition level.
C13 GroupHeaderInterbankSettlementDateRule
If GroupHeader/InterbankSettlementDate is present, then
CreditTransferTransactionInformation/InterbankSettlementDate is not allowed.
On Condition
    /GroupHeader/InterbankSettlementDate is present
Following Must be True
    /CreditTransferTransactionInformation[*]/InterbankSettlementDate Must be 
absent
This constraint is defined at the MessageDefinition level.
C14 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C15 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C16 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C17 InstructedAgentRule
If GroupHeader/InstructedAgent is present, then CreditTransferTransactionInformation/
InstructedAgent is not allowed.
On Condition
    /GroupHeader/InstructedAgent is present
Following Must be True
    /CreditTransferTransactionInformation[*]/InstructedAgent Must be absent
This constraint is defined at the MessageDefinition level.
C18 InstructedReimbursementAgentAccountRule
If InstructedReimbursementAgentAccount is present, then InstructedReimbursementAgent
must be present.
C19 InstructingAgentRule
If GroupHeader/InstructingAgent is present, then CreditTransferTransactionInformation/
InstructingAgent is not allowed.
On Condition
    /GroupHeader/InstructingAgent is present
Following Must be True
    /CreditTransferTransactionInformation[*]/InstructingAgent Must be absent
This constraint is defined at the MessageDefinition level.
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
843 March 2026
```

## File page 844

```text
C20 InstructingReimbursementAgentAccountRule
If InstructingReimbursementAgentAccount is present, then InstructingReimbursementAgent
must be present.
C21 IntermediaryAgent1AccountRule
If IntermediaryAgent1Account is present, then IntermediaryAgent1 must be present.
C22 IntermediaryAgent1AccountRule
If IntermediaryAgent1Account is present, then IntermediaryAgent1 must be present.
C23 IntermediaryAgent1AccountRule
If IntermediaryAgent1Account is present, then IntermediaryAgent1 must be present.
C24 IntermediaryAgent1Rule
If IntermediaryAgent1 is present, then CreditorAgent must be present.
C25 IntermediaryAgent1Rule
If IntermediaryAgent1 is present, then CreditorAgent must be present.
C26 IntermediaryAgent2AccountRule
If IntermediaryAgent2Account is present, then IntermediaryAgent2 must be present.
C27 IntermediaryAgent2AccountRule
If IntermediaryAgent2Account is present, then IntermediaryAgent2 must be present.
C28 IntermediaryAgent2AccountRule
If IntermediaryAgent2Account is present, then IntermediaryAgent2 must be present.
C29 IntermediaryAgent2Rule
If IntermediaryAgent2 is present, then IntermediaryAgent1 must be present.
C30 IntermediaryAgent2Rule
If IntermediaryAgent2 is present, then IntermediaryAgent1 must be present.
C31 IntermediaryAgent2Rule
If IntermediaryAgent2 is present, then IntermediaryAgent1 must be present.
C32 IntermediaryAgent3AccountRule
If IntermediaryAgent3Account is present, then IntermediaryAgent3 must be present.
C33 IntermediaryAgent3AccountRule
If IntermediaryAgent3Account is present, then IntermediaryAgent3 must be present.
C34 IntermediaryAgent3AccountRule
If IntermediaryAgent3Account is present, then IntermediaryAgent3 must be present.
C35 IntermediaryAgent3Rule
If IntermediaryAgent3 is present, then IntermediaryAgent2 must be present.
C36 IntermediaryAgent3Rule
If IntermediaryAgent3 is present, then IntermediaryAgent2 must be present.
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
844 March 2026
```

## File page 845

```text
C37 IntermediaryAgent3Rule
If IntermediaryAgent3 is present, then IntermediaryAgent2 must be present.
C38 PaymentTypeInformationRule
If GroupHeader/PaymentTypeInformation is present, then
CreditTransferTransactionInformation/PaymentTypeInformation is not allowed.
On Condition
    /GroupHeader/PaymentTypeInformation is present
Following Must be True
    /CreditTransferTransactionInformation[*]/PaymentTypeInformation Must be 
absent
This constraint is defined at the MessageDefinition level.
C39 PreviousInstructingAgent1AccountRule
If PreviousInstructingAgent1Account is present, then PreviousInstructingAgent1 must be
present.
C40 PreviousInstructingAgent1AccountRule
If PreviousInstructingAgent1Account is present, then PreviousInstructingAgent1 must be
present.
C41 PreviousInstructingAgent1AccountRule
If PreviousInstructingAgent1Account is present, then PreviousInstructingAgent1 must be
present.
C42 PreviousInstructingAgent1Guideline
It is recommended that, when present, PreviousInstructingAgent1 is the closest to the
DebtorAgent in the payment chain.
C43 PreviousInstructingAgent1Guideline
It is recommended that, when present, PreviousInstructingAgent1 is the closest to the
DebtorAgent in the payment chain.
C44 PreviousInstructingAgent1Guideline
It is recommended that, when present, PreviousInstructingAgent1 is the closest to the
DebtorAgent in the payment chain.
C45 PreviousInstructingAgent2AccountRule
If PreviousInstructingAgent2Account is present, then PreviousInstructingAgent2 must be
present.
C46 PreviousInstructingAgent2AccountRule
If PreviousInstructingAgent2Account is present, then PreviousInstructingAgent2 must be
present.
C47 PreviousInstructingAgent2AccountRule
If PreviousInstructingAgent2Account is present, then PreviousInstructingAgent2 must be
present.
C48 PreviousInstructingAgent2Rule
If PreviousInstructingAgent2 is present, then PreviousInstructingAgent1 must be present.
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
845 March 2026
```

## File page 846

```text
C49 PreviousInstructingAgent2Rule
If PreviousInstructingAgent2 is present, then PreviousInstructingAgent1 must be present.
C50 PreviousInstructingAgent2Rule
If PreviousInstructingAgent2 is present, then PreviousInstructingAgent1 must be present.
C51 PreviousInstructingAgent3AccountRule
If PreviousInstructingAgent3Account is present, then PreviousInstructingAgent3 must be
present.
C52 PreviousInstructingAgent3AccountRule
If PreviousInstructingAgent3Account is present, then PreviousInstructingAgent3 must be
present.
C53 PreviousInstructingAgent3AccountRule
If PreviousInstructingAgent3Account is present, then PreviousInstructingAgent3 must be
present.
C54 PreviousInstructingAgent3Rule
If PreviousInstructingAgent3 is present, then PreviousInstructingAgent2 must be present.
C55 PreviousInstructingAgent3Rule
If PreviousInstructingAgent3 is present, then PreviousInstructingAgent2 must be present.
C56 PreviousInstructingAgent3Rule
If PreviousInstructingAgent3 is present, then PreviousInstructingAgent2 must be present.
C57 RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
C58 ReportingCodeAndInformationRule
Reporting code or information must be present. Both may be present.
C59 SettlementMethodAgentRule
If SettlementMethod is equal to INDA or INGA, then ReimbursementAgent(s) and
ClearingSystem are not allowed.
C60 SettlementMethodClearingRule
If SettlementMethod is equal to CLRG, then SettlementAccount and ReimbursementAgent(s)
are not allowed.
C61 SettlementMethodCoverAgentRule
If SettlementMethod is equal to COVE, then InstructedReimbursementAgent or
InstructingReimbursementAgent must be present.
C62 SettlementMethodCoverRule
If SettlementMethod is equal to COVE, then SettlementAccount and ClearingSystem are not
allowed.
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
846 March 2026
```

## File page 847

```text
C63 SupplementaryDataRule
The SupplementaryData building block at message level must not be used to provide additional
information about a transaction. The SupplementaryData element at transaction level should be
used for that purpose.
This constraint is defined at the MessageDefinition level.
C64 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C65 ThirdReimbursementAgentAccountRule
If ThirdReimbursementAgentAccount is present, then ThirdReimbursementAgent must be
present.
C66 ThirdReimbursementAgentRule
If ThirdReimbursementAgent is present, then InstructingReimbursementAgent and
InstructedReimbursementAgent must both be present.
C67 TotalInterbankSettlementAmountAndDateRule
If TotalInterbankSettlementAmount is present, then InterbankSettlementDate must be present.
C68 TotalInterbankSettlementAmountAndSumRule
If GroupHeader/TotalInterbankSettlementAmount is present, then it must equal the sum of all
occurrences of CreditTransferTransactionInformation/InterbankSettlementAmount.
On Condition
    /GroupHeader/TotalInterbankSettlementAmount is present
Following Must be True
    /GroupHeader/TotalInterbankSettlementAmount Must be equal to value 'sum 
of /CreditTransferTransactionInformation/InterbankSettlementAmount'
This constraint is defined at the MessageDefinition level.
C69 TotalInterbankSettlementAmountRule
If GroupHeader/TotalInterbankSettlementAmount is present, then all occurrences of
CreditTransferTransactionInformation/InterbankSettlementAmount must have the same
currency as the currency of GroupHeader/TotalInterbankSettlementAmount.
On Condition
    /GroupHeader/TotalInterbankSettlementAmount is present
Following Must be True
    /CreditTransferTransactionInformation[*]/InterbankSettlementAmount/
attribute::Currency Must be equal to /GroupHeader/
TotalInterbankSettlementAmount/attribute::Currency
This constraint is defined at the MessageDefinition level.
C70 TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
C71 TransactionInterbankSettlementDateRule
If GroupHeader/InterbankSettlementDate is not present, then
CreditTransferTransactionInformation/InterbankSettlementDate must be present.
On Condition
    /GroupHeader/InterbankSettlementDate is absent
Following Must be True
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
847 March 2026
```

