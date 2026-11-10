---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.3 Constraints"]
file_pages: [571, 572, 573, 574, 575]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.3 Constraints

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 571 to 575.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 571

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       Debtor <Dbtr> [0..1]  689
{Or         Party <Pty> [1..1] ± 689
Or}         Agent <Agt> [1..1] ± 690
       DebtorAccount <DbtrAcct> [0..1] ± C20,
C19
691
       DebtorAgent <DbtrAgt> [0..1] ± 692
       DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C20,
C19
692
       CreditorAgent <CdtrAgt> [0..1] ± 693
       CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C20,
C19
694
       Creditor <Cdtr> [0..1]  695
{Or         Party <Pty> [1..1] ± 695
Or}         Agent <Agt> [1..1] ± 696
       CreditorAccount <CdtrAcct> [0..1] ± C20,
C19
697
       UltimateCreditor <UltmtCdtr> [0..1]  698
{Or         Party <Pty> [1..1] ± 698
Or}         Agent <Agt> [1..1] ± 699
       Purpose <Purp> [0..1] ± 700
     SupplementaryData <SplmtryData> [0..*] ± C35 700
   SupplementaryData <SplmtryData> [0..*] ± C35 701
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
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
571 March 2026
```

## File page 572

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
C7 ChargesInformationAndReversedInstructedAmountRule
If ChargesInformation is present, then ReversedInstructedAmount must be present.
C8 ControlSumAndGroupReversalRule
If GroupReversal is true, then ControlSum is not allowed.
C9 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C10 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C11 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C12 GroupHeaderInterbankSettlementDateRule
If GroupHeader/InterbankSettlementDate is present, then TransactionInformation/
InterbankSettlementDate is not allowed.
On Condition
    /GroupHeader/InterbankSettlementDate is present
Following Must be True
    /TransactionInformation[*]/InterbankSettlementDate Must be absent
This constraint is defined at the MessageDefinition level.
C13 GroupReversalAndNumberOfTransactionsGuideline
If GroupReversal is true, then NumberOfTransactions equals the number of transactions in the
original message.
C14 GroupReversalAndNumberOfTransactionsRule
If GroupHeader/GroupReversal is false, then GroupHeader/NumberOfTransactions must equal
the number of occurrences of TransactionInformation.
On Condition
    /GroupHeader/GroupReversal is present
 And    /GroupHeader/GroupReversal is equal to value 'false'
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
572 March 2026
```

## File page 573

```text
Following Must be True
    /GroupHeader/NumberOfTransactions Must be equal to value 'Number 
Occurrences TransactionInformation'
This constraint is defined at the MessageDefinition level.
C15 GroupReversalAndReasonRule
If GroupHeader/GroupReversal is true, then OriginalGroupInformation/
ReversalReasonInformation/Reason must present.
On Condition
    /GroupHeader/GroupReversal is present
 And    /GroupHeader/GroupReversal is equal to value 'true'
Following Must be True
    /OriginalGroupInformation/ReversalReasonInformation[1] Must be present
 And    /OriginalGroupInformation/ReversalReasonInformation[*]/Reason Must be 
present
This constraint is defined at the MessageDefinition level.
C16 GroupReversalAndTransactionInformationNotPresentRule
If GroupHeader/GroupReversal is true, then TransactionInformation is not allowed.
On Condition
    /GroupHeader/GroupReversal is present
 And    /GroupHeader/GroupReversal is equal to value 'true'
Following Must be True
    /TransactionInformation[*] Must be absent
This constraint is defined at the MessageDefinition level.
C17 GroupReversalAndTransactionInformationPresentRule
If GroupHeader/GroupReversal is false, then at least one occurrence of TransactionInformation
must be present.
On Condition
    /GroupHeader/GroupReversal is present
 And    /GroupHeader/GroupReversal is equal to value 'false'
Following Must be True
    /TransactionInformation[1] Must be present
This constraint is defined at the MessageDefinition level.
C18 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C19 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C20 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C21 InstructedAgentRule
If GroupHeader/InstructedAgent is present, then TransactionInformation/InstructedAgent is not
allowed.
On Condition
    /GroupHeader/InstructedAgent is present
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
573 March 2026
```

## File page 574

```text
Following Must be True
    /TransactionInformation[*]/InstructedAgent Must be absent
This constraint is defined at the MessageDefinition level.
C22 InstructedReimbursementAgentAccountRule
If InstructedReimbursementAgentAccount is present, then InstructedReimbursementAgent
must be present.
C23 InstructingAgentRule
If GroupHeader/InstructingAgent is present, then TransactionInformation/InstructingAgent is not
allowed.
On Condition
    /GroupHeader/InstructingAgent is present
Following Must be True
    /TransactionInformation[*]/InstructingAgent Must be absent
This constraint is defined at the MessageDefinition level.
C24 InstructingReimbursementAgentAccountRule
If InstructingReimbursementAgentAccount is present, then InstructingReimbursementAgent
must be present.
C25 NoCoverSettlementMethodRule
GroupHeader/SettlementInformation/SettlementMethod must be different from COVE (Cover)
when reversing direct debit transactions.
On Condition
    /GroupHeader/SettlementInformation is present
 And    /GroupHeader/SettlementInformation/SettlementMethod is equal to value 
'CoverMethod'
Following Must be True
    substring(/OriginalGroupInformation/
OriginalMessageNameIdentification,1,8) Must be different from value 'pacs.003'
This constraint is defined at the MessageDefinition level.
C26 OriginalGroupInformationRule
If OriginalGroupInformation is present, then TransactionInformation/OriginalGroupInformation is
not allowed.
On Condition
    /OriginalGroupInformation is present
Following Must be True
    /TransactionInformation[*]/OriginalGroupInformation Must be absent
This constraint is defined at the MessageDefinition level.
C27 RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
C28 ReversedInstructedAmountAndExchangeRate1Rule
If ReversedInstructedAmount is present and the currency is different from the currency in
InterbankSettlementAmount, then ExchangeRate must be present.
C29 ReversedInstructedAmountAndExchangeRate2Rule
If ReversedInstructedAmount is present and the currency is the same as the currency in
InterbankSettlementAmount, then ExchangeRate is not allowed.
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
574 March 2026
```

## File page 575

```text
C30 SettlementMethodAgentRule
If SettlementMethod is equal to INDA or INGA, then ReimbursementAgent(s) and
ClearingSystem are not allowed.
C31 SettlementMethodClearingRule
If SettlementMethod is equal to CLRG, then SettlementAccount and ReimbursementAgent(s)
are not allowed.
C32 SettlementMethodCoverAgentRule
If SettlementMethod is equal to COVE, then InstructedReimbursementAgent or
InstructingReimbursementAgent must be present.
C33 SettlementMethodCoverRule
If SettlementMethod is equal to COVE, then SettlementAccount and ClearingSystem are not
allowed.
C34 SupplementaryDataRule
The SupplementaryData building block at message level must not be used to provide additional
information about a transaction. The SupplementaryData element at transaction level should be
used for that purpose.
This constraint is defined at the MessageDefinition level.
C35 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C36 ThirdReimbursementAgentAccountRule
If ThirdReimbursementAgentAccount is present, then ThirdReimbursementAgent must be
present.
C37 ThirdReimbursementAgentRule
If ThirdReimbursementAgent is present, then InstructingReimbursementAgent and
InstructedReimbursementAgent must both be present.
C38 TotalInterbankSettlementAmountAndDateRule
If TotalReversedInterbankSettlementAmount is present, then InterbankSettlementDate must be
present.
C39 TotalReversedInterbankSettlementAmountAndSumRule
GroupHeader/TotalReversedInterbankSettlementAmount must equal the sum of all individual
TransactionInformation/ReversedInterbankSettlementAmount when present.
On Condition
    /GroupHeader/TotalReversedInterbankSettlementAmount is present
Following Must be True
    /GroupHeader/TotalReversedInterbankSettlementAmount Must be equal to 
value 'sum of TransactionInformation/ReversedInterbankSttlementAmount'
This constraint is defined at the MessageDefinition level.
C40 TotalReversedInterbankSettlementAmountRule
If GroupHeader/TotalReversedInterbankSettlementAmount is present, then all occurrences of
TransactionInformation/ReversedInterbankSettlementAmount must have the same currency as
the currency of GroupHeader/TotalReversedInterbankSettlementAmount.
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
575 March 2026
```

