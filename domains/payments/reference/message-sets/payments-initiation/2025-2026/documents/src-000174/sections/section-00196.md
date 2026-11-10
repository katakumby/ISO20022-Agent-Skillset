---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.3 Constraints"]
file_pages: [280, 281, 282]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.3 Constraints

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 280 to 282.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 280

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         Debtor <Dbtr> [0..1]  390
{Or           Party <Pty> [1..1] ± 390
Or}           Agent <Agt> [1..1] ± 391
         DebtorAccount <DbtrAcct> [0..1] ± C18,
C17
392
         DebtorAgent <DbtrAgt> [0..1] ± 393
         DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C18,
C17
393
         CreditorAgent <CdtrAgt> [0..1] ± 394
         CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C18,
C17
395
         Creditor <Cdtr> [0..1]  396
{Or           Party <Pty> [1..1] ± 396
Or}           Agent <Agt> [1..1] ± 397
         CreditorAccount <CdtrAcct> [0..1] ± C18,
C17
398
         UltimateCreditor <UltmtCdtr> [0..1]  399
{Or           Party <Pty> [1..1] ± 399
Or}           Agent <Agt> [1..1] ± 400
         Purpose <Purp> [0..1] ± 401
       SupplementaryData <SplmtryData> [0..*] ± C30 401
   SupplementaryData <SplmtryData> [0..*] ± C30 0
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
C3 AmendmentIndicatorFalseRule
If AmendmentIndicator is false, then AmendmentInformationDetails is not allowed.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 280 March 2026
```

## File page 281

```text
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
C7 ControlSumAndGroupReversalRule
If GroupReversal is true, then ControlSum is not allowed.
C8 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C11 GroupReversalAndNumberOfTransactionsGuideline
If GroupHeader/GroupReversal is false and OriginalPaymentInformationAndReversal[*]/
PaymentInformationReversal is false, then NumberOfTransactions must equal the number of
occurrences of OriginalPaymentInformationAndReversal[*]/TransactionInformation.
This constraint is defined at the MessageDefinition level.
C12 GroupReversalAndNumberOfTransactionsGuideline
If GroupReversal is true, then NumberOfTransactions equals the number of transactions in the
original message.
C13 GroupReversalAndPaymentInformationNotPresentRule
If GroupHeader/GroupReversal is true, then OriginalPaymentInformationAndReversal is not
allowed.
On Condition
    /GroupHeader/GroupReversal is present
 And    /GroupHeader/GroupReversal is equal to value 'true'
Following Must be True
    /OriginalPaymentInformationAndReversal[*] Must be absent
This constraint is defined at the MessageDefinition level.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 281 March 2026
```

## File page 282

```text
C14 GroupReversalAndPaymentInformationPresentRule
If GroupHeader/GroupReversal is false, then at least one occurrence of
OriginalPaymentInformationAndReversal must be present.
On Condition
    /GroupHeader/GroupReversal is present
 And    /GroupHeader/GroupReversal is equal to value 'false'
Following Must be True
    /OriginalPaymentInformationAndReversal[1] Must be present
This constraint is defined at the MessageDefinition level.
C15 GroupReversalAndReasonRule
If GroupHeader/GroupReversal is true, then OriginalGroupInformation/
ReversalReasonInformation/Reason must present.
On Condition
    /GroupHeader/GroupReversal is present
 And    /GroupHeader/GroupReversal is equal to value 'true'
Following Must be True
    /OriginalGroupInformation/ReversalReasonInformation[*]/Reason Must be 
present
This constraint is defined at the MessageDefinition level.
C16 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C17 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C18 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C19 InstructedReimbursementAgentAccountRule
If InstructedReimbursementAgentAccount is present, then InstructedReimbursementAgent
must be present.
C20 InstructingReimbursementAgentAccountRule
If InstructingReimbursementAgentAccount is present, then InstructingReimbursementAgent
must be present.
C21 PaymentInformationReversalAndReasonRule
If PaymentInformationReversal is true, then ReversalReasonInformation/ReversalReason must
present.
C22 PaymentInformationReversalAndTransactionInformationNotPresentRule
If PaymentInformationReversal is true, then TransactionInformation is not allowed.
C23 PaymentInformationReversalAndTransactionInformationPresentRule
If PaymentInformationReversal is false, then at least one occurrence of TransactionInformation
must be present.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 282 March 2026
```

