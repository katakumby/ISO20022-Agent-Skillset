---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.3 Constraints"]
file_pages: [411, 412]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.3 Constraints

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 411 to 412.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 411

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or                 Code <Cd> [1..1] CodeSet 521
Or}                 Proprietary <Prtry> [1..1] Text 521
               Issuer <Issr> [0..1] Text 521
             Garnishee <Grnshee> [0..1] ± 521
             GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 522
             ReferenceNumber <RefNb> [0..1] Text 523
             Date <Dt> [0..1] Date 524
             RemittedAmount <RmtdAmt> [0..1] Amount C2, C12 524
             FamilyMedicalInsuranceIndicator <FmlyMdclInsrncInd> [0..1] Indicator 524
             EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 524
           SecuritiesData <SctiesData> [0..*]  524
             UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 525
             Amount <Amt> [0..1] Amount C1, C13 525
           AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 525
       SupplementaryData <SplmtryData> [0..*] ± C21 525
   SupplementaryData <SplmtryData> [0..*] ± C21 0
5.3 Constraints
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
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 411 March 2026
```

## File page 412

```text
C5 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C6 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C7 ChargeBearerRule
If ChargeBearer is present, then DirectDebitTransactionInformation/ChargeBearer is not
allowed.
If DirectDebitTransactionInformation/ChargeBearer is present, then ChargeBearer is not
allowed.
DirectDebitTransactionInformation/ChargeBearer and ChargeBearer may both be absent.
C8 ChargesAccountAgentRule
If ChargesAccountAgent is present, then it must contain a branch of the CreditorAgent. It must
not contain a completely different agent.
C9 ChargesAccountRule
If ChargesAccountAgent is present, then ChargesAccount must be present.
C10 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C11 CreditorSchemeIdentificationRule
If CreditorSchemeIdentification is present, then DirectDebitTransactionInformation/
CreditorSchemeIdentification is not allowed.
If DirectDebitTransactionInformation/CreditorSchemeIdentification is present, then
CreditorSchemeIdentification is not allowed.
DirectDebitTransactionInformation/CreditorSchemeIdentification and
CreditorSchemeIdentification may both be absent.
C12 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C13 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C14 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 412 March 2026
```

