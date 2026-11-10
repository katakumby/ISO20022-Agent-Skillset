---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.3 Constraints"]
file_pages: [711, 712, 713, 714, 715]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.3 Constraints

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 711 to 715.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 711

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 825
           ReferenceNumber <RefNb> [0..1] Text 826
           Date <Dt> [0..1] Date 827
           RemittedAmount <RmtdAmt> [0..1] Amount C2, C12 827
           FamilyMedicalInsuranceIndicator <FmlyMdclInsrncInd> [0..1] Indicator 827
           EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 827
         SecuritiesData <SctiesData> [0..*]  827
           UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 828
           Amount <Amt> [0..1] Amount C1, C11 828
         AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 828
     SupplementaryData <SplmtryData> [0..*] ± C46 828
   SupplementaryData <SplmtryData> [0..*] ± C46 0
6.3 Constraints
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
C3 AdditionalDateTimePresenceRule
AcceptanceDateTime or PoolingAdjustmentDate or ExpiryDateTime must be present. All can
be present.
C4 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C5 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
711 March 2026
```

## File page 712

```text
C6 ChargeBearerAndChargesInformationRule
If ChargeBearer contains DEBT, then ChargesInformation may be present to communicate
charges that have been added for (the) InstructedAgent(s).
If ChargeBearer contains CRED, then at least one occurrence of ChargesInformation must be
present to communicate charges that have been deducted from the InstructedAmount by (the)
InstructingAgent(s).
If ChargeBearer contains SHAR or SLEV, then ChargesInformation is optional.
C7 ChargesAmountGuideline
If ChargesInformation is present, then the currency of ChargesInformation/ChargesAmount is
recommended to be the same as the currency of InterbankSettlementAmount.
C8 ChargesInformationAndInstructedAmountRule
If ChargesInformation is present, then InstructedAmount must be present.
C9 ChargesInformationGuideline
The repetitive ChargesInformation should contain all information on charges amount and which
party has taken the charges, separately for each agent along the payment chain.
C10 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C11 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C12 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C13 GroupHeaderExpiryDateTimeRule
If GroupHeader/ExpiryDateTime is present, then CreditTransferTransactionInformation/
AdditionalDateTime/ExpiryDateTime is not allowed.
On Condition
    /GroupHeader/ExpiryDateTime is present
Following Must be True
    /CreditTransferTransactionInformation[*]/AdditionalDateTime/
ExpiryDateTime Must be absent
This constraint is defined at the MessageDefinition level.
C14 GroupHeaderInterbankSettlementDateRule
If GroupHeader/InterbankSettlementDate is present, then
CreditTransferTransactionInformation/InterbankSettlementDate is not allowed.
On Condition
    /GroupHeader/InterbankSettlementDate is present
Following Must be True
    /CreditTransferTransactionInformation[*]/InterbankSettlementDate Must be 
absent
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
712 March 2026
```

## File page 713

```text
This constraint is defined at the MessageDefinition level.
C15 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C16 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C17 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C18 InstructedAgentRule
If GroupHeader/InstructedAgent is present, then CreditTransferTransactionInformation/
InstructedAgent is not allowed.
On Condition
    /GroupHeader/InstructedAgent is present
Following Must be True
    /CreditTransferTransactionInformation[*]/InstructedAgent Must be absent
This constraint is defined at the MessageDefinition level.
C19 InstructedAmountAndExchangeRate1Rule
If InstructedAmount is present and the currency is different from the currency in
InterbankSettlementAmount, then ExchangeRate must be present.
C20 InstructedAmountAndExchangeRate2Rule
If InstructedAmount is present and the currency is the same as the currency in
InterbankSettlementAmount, then ExchangeRate is not allowed.
C21 InstructedAmountAndExchangeRate3Rule
If InstructedAmount is not present, then ExchangeRate is not allowed.
C22 InstructedReimbursementAgentAccountRule
If InstructedReimbursementAgentAccount is present, then InstructedReimbursementAgent
must be present.
C23 InstructingAgentRule
If GroupHeader/InstructingAgent is present, then CreditTransferTransactionInformation/
InstructingAgent is not allowed.
On Condition
    /GroupHeader/InstructingAgent is present
Following Must be True
    /CreditTransferTransactionInformation[*]/InstructingAgent Must be absent
This constraint is defined at the MessageDefinition level.
C24 InstructingReimbursementAgentAccountRule
If InstructingReimbursementAgentAccount is present, then InstructingReimbursementAgent
must be present.
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
713 March 2026
```

## File page 714

```text
C25 InstructionForCreditorAgentRule
If InstructionForCreditorAgent/Code contains CHQB (PayCreditorByCheque), then
CreditorAccount is not allowed.
Expression Language: UGRule
C26 IntermediaryAgent1AccountRule
If IntermediaryAgent1Account is present, then IntermediaryAgent1 must be present.
C27 IntermediaryAgent2AccountRule
If IntermediaryAgent2Account is present, then IntermediaryAgent2 must be present.
C28 IntermediaryAgent2Rule
If IntermediaryAgent2 is present, then IntermediaryAgent1 must be present.
C29 IntermediaryAgent3AccountRule
If IntermediaryAgent3Account is present, then IntermediaryAgent3 must be present.
C30 IntermediaryAgent3Rule
If IntermediaryAgent3 is present, then IntermediaryAgent2 must be present.
C31 NumberOfTransactionsAndCreditTransfersRule
GroupHeader/NumberOfTransactions must equal the number of occurrences of
CreditTransferTransactionInformation.
Following Must be True
    /GroupHeader/NumberOfTransactions Must be equal to value 'number of 
occurrences of CreditTransferTransactionInformation'
This constraint is defined at the MessageDefinition level.
C32 PaymentTypeInformationRule
If GroupHeader/PaymentTypeInformation is present, then
CreditTransferTransactionInformation/PaymentTypeInformation is not allowed.
On Condition
    /GroupHeader/PaymentTypeInformation is present
Following Must be True
    /CreditTransferTransactionInformation[*]/PaymentTypeInformation Must be 
absent
This constraint is defined at the MessageDefinition level.
C33 PreviousInstructingAgent1AccountRule
If PreviousInstructingAgent1Account is present, then PreviousInstructingAgent1 must be
present.
C34 PreviousInstructingAgent1Guideline
It is recommended that, when present, PreviousInstructingAgent1 is the closest to the
DebtorAgent in the payment chain.
C35 PreviousInstructingAgent2AccountRule
If PreviousInstructingAgent2Account is present, then PreviousInstructingAgent2 must be
present.
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
714 March 2026
```

## File page 715

```text
C36 PreviousInstructingAgent2Rule
If PreviousInstructingAgent2 is present, then PreviousInstructingAgent1 must be present.
C37 PreviousInstructingAgent3AccountRule
If PreviousInstructingAgent3Account is present, then PreviousInstructingAgent3 must be
present.
C38 PreviousInstructingAgent3Rule
If PreviousInstructingAgent3 is present, then PreviousInstructingAgent2 must be present.
C39 RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
C40 ReportingCodeAndInformationRule
Reporting code or information must be present. Both may be present.
C41 SettlementMethodAgentRule
If SettlementMethod is equal to INDA or INGA, then ReimbursementAgent(s) and
ClearingSystem are not allowed.
C42 SettlementMethodClearingRule
If SettlementMethod is equal to CLRG, then SettlementAccount and ReimbursementAgent(s)
are not allowed.
C43 SettlementMethodCoverAgentRule
If SettlementMethod is equal to COVE, then InstructedReimbursementAgent or
InstructingReimbursementAgent must be present.
C44 SettlementMethodCoverRule
If SettlementMethod is equal to COVE, then SettlementAccount and ClearingSystem are not
allowed.
C45 SupplementaryDataRule
The SupplementaryData building block at message level must not be used to provide additional
information about a transaction. The SupplementaryData element at transaction level should be
used for that purpose.
This constraint is defined at the MessageDefinition level.
C46 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C47 ThirdReimbursementAgentAccountRule
If ThirdReimbursementAgentAccount is present, then ThirdReimbursementAgent must be
present.
C48 ThirdReimbursementAgentRule
If ThirdReimbursementAgent is present, then InstructingReimbursementAgent and
InstructedReimbursementAgent must both be present.
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
715 March 2026
```

