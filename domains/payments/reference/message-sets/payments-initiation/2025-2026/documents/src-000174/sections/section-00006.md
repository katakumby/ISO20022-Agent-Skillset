---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.3 Constraints"]
file_pages: [14, 15, 16]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.3 Constraints

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 14 to 16.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 14

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
   SupplementaryData <SplmtryData> [0..*] ± C36 129
2.3 Constraints
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
C5 ChargeBearerRule
If ChargeBearer is present, then CreditTransferTransactionInformation/ChargeBearer is not
allowed.
If CreditTransferTransactionInformation/ChargeBearer is present, then ChargeBearer is not
allowed.
CreditTransferTransactionInformation/ChargeBearer and ChargeBearer may both be absent.
C6 ChargesAccountAgentRule
If ChargesAccountAgent is present, then it must contain a branch of the DebtorAgent. It must
not contain a completely different agent.
C7 ChargesAccountRule
If ChargesAccountAgent is present, then ChargesAccount must be present.
C8 ChequeAndCreditorAccountRule
If PaymentMethod is CHK (Cheque), then CreditTransferTransactionInformation/
CreditorAccount is not allowed.
C9 ChequeDeliveryAndCreditorAgentRule
If PaymentMethod is CHK (Cheque) and CreditTransferTransactionInformation/
ChequeInstruction/DeliveryMethod/Code is present and is equal to MLFA (MailToFinalAgent),
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 14 March 2026
```

## File page 15

```text
CRFA (CourierToFinalAgent), RGFA (RegisteredMailToFinalAgent) or PUFA
(PickUpByFinalAgent), then CreditTransferTransactionInformation/CreditorAgent must be
present.
C10 ChequeDeliveryAndNoCreditorAgentRule
If PaymentMethod is CHK (Cheque) and CreditTransferTransactionInformation/
ChequeInstruction/DeliveryMethod/Code is present and different from MLFA
(MailToFinalAgent), CRFA (CourierToFinalAgent), RGFA (RegisteredMailToFinalAgent) or
PUFA (PickUpByFinalAgent), then CreditTransferTransactionInformation/CreditorAgent is not
allowed.
C11 ChequeFromGuideline
CreditTransferTransactionInformation/ChequeInstruction/ChequeFrom may only be present if
different from CreditTransferTransactionInformation/UltimateDebtor or Debtor.
C12 ChequeInstructionDeliverToCreditorAgentGuideline
If CreditTransferTransactionInformation/ChequeInstruction/DeliveryMethod is present and is
CRFA (CourierToFinalAgent), MLFA (MailToFinalAgent), PUFA (PickUpByFinalAgent) or
RGFA (RegisteredMailToFinalAgent), then CreditTransferTransactionInformation/
ChequeInstruction/DeliverTo may only be present if different from
CreditTransferTransactionInformation/Creditor.
C13 ChequeInstructionDeliverToCreditorGuideline
If PaymentInformation/CreditTransferTransactionInformation/ChequeInstruction/DeliveryMethod
is present and is CRCD (CourierToCreditor), MLCD (MailToCreditor), PUCD
(PickUpByCreditor) or RGCD (RegisteredMailToCreditor), then
CreditTransferTransactionInformation/ChequeInstruction/DeliverTo may only be present if
different from CreditTransferTransactionInformation/Creditor.
C14 ChequeInstructionDeliverToDebtorGuideline
If CreditTransferTransactionInformation/ChequeInstruction/DeliveryMethod is present and if
CreditTransferTransactionInformation/ChequeInstruction/DeliveryMethod/Code is CRDB
(CourierToDebtor), MLDB (MailToDebtor), PUDB (PickUpByDebtor) or RGDB
(RegisteredMailToDebtor), then CreditTransferTransactionInformation/ChequeInstruction/
DeliverTo may only be present if different from Debtor.
C15 ChequeInstructionRule
If PaymentMethod is different from CHK (Cheque), then CreditTransferTransactionInformation/
ChequeInstruction is not allowed.
C16 ChequeMaturityDateRule
If ChequeMaturityDate is present, then ChequeType must be present and equal to DRFT or
ELDR.
C17 ChequeNoDeliveryAndNoCreditorAgentRule
If PaymentMethod is CHK (Cheque) and CreditTransferTransactionInformation/
ChequeInstruction/DeliveryMethod is not present, then CreditTransferTransactionInformation/
CreditorAgent is not allowed.
C18 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 15 March 2026
```

## File page 16

```text
C19 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C20 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C21 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C22 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C23 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C24 InstructionForCreditorAgentRule
If InstructionForCreditorAgent/Code contains CHQB, then CreditorAccount is not allowed.
C25 InstructionForDebtorAgentRule
If InstructionForDebtorAgent is present, then CreditTransferTransactionInformation/
InstructionForDebtorAgent is not allowed.
If CreditTransferTransactionInformation/InstructionForDebtorAgent is present, then
InstructionForDebtorAgent is not allowed.
CreditTransferTransactionInformation/InstructionForDebtorAgent and
InstructionForDebtorAgent may both be absent.
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
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 16 March 2026
```

