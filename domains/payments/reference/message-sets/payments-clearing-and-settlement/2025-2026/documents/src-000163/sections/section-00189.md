---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.3 Constraints"]
file_pages: [265, 266, 267, 268, 269, 270, 271]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.3 Constraints

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 265 to 271.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 265

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           Account <Acct> [1..1] ± C22,
C21
559
           Purpose <Purp> [1..1] ± 559
           Reference <Ref> [1..1] Text 560
           RelatedReferences <RltdRefs> [0..*] ± 560
     SupplementaryData <SplmtryData> [0..*] ± C68 560
   SupplementaryData <SplmtryData> [0..*] ± C68 561
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
C7 ChargesInformationAndReturnedInstructedAmountRule
If ChargesInformation is present, then ReturnedInstructedAmount must be present.
C8 ControlSumAndGroupReturnRule
If GroupReturn is true, then ControlSum is not allowed.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
265 March 2026
```

## File page 266

```text
C9 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C10 CreditorAgentAccountRule
If CreditorAgentAccount is present, then CreditorAgent must be present.
C11 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C12 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C13 DebtorAgentAccountRule
If DebtorAgentAccount is present, then DebtorAgent must be present.
C14 GroupHeaderInterbankSettlementDateRule
If GroupHeader/InterbankSettlementDate is present, then TransactionInformation/
InterbankSettlementDate is not allowed.
On Condition
    /GroupHeader/InterbankSettlementDate is present
Following Must be True
    /TransactionInformation[*]/InterbankSettlementDate Must be absent
This constraint is defined at the MessageDefinition level.
C15 GroupReturnAndNumberOfTransactionsGuideline
If GroupReturn is true, then NumberOfTransactions equals the number of transactions in the
original message.
C16 GroupReturnAndNumberOfTransactionsRule
If GroupHeader/GroupReturn is false, then GroupHeader/NumberOfTransactions must equal
the number of occurrences of TransactionInformation.
On Condition
    /GroupHeader/GroupReturn is present
 And    /GroupHeader/GroupReturn is equal to value 'false'
Following Must be True
    /GroupHeader/NumberOfTransactions Must be equal to value 'Number 
Occurrences TransactionInformation'
This constraint is defined at the MessageDefinition level.
C17 GroupReturnAndReturnReasonRule
If GroupHeader/GroupReturn is true, then OriginalGroupInformation/ReturnReasonInformation/
ReturnReason must be present.
On Condition
    /GroupHeader/GroupReturn is present
 And    /GroupHeader/GroupReturn is equal to value 'true'
 And    /OriginalGroupInformation/ReturnReasonInformation[*]/
AdditionalInformation[1] is present
Following Must be True
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
266 March 2026
```

## File page 267

```text
    /OriginalGroupInformation/ReturnReasonInformation[*]/Reason Must be 
present
This constraint is defined at the MessageDefinition level.
C18 GroupReturnAndTransactionInformationNotPresentRule
If GroupHeader/GroupReturn is true, then TransactionInformation is not allowed.
On Condition
    /GroupHeader/GroupReturn is present
 And    /GroupHeader/GroupReturn is equal to value 'true'
Following Must be True
    /TransactionInformation[*] Must be absent
This constraint is defined at the MessageDefinition level.
C19 GroupReturnAndTransactionInformationPresentRule
If GroupHeader/GroupReturn is false, then at least one occurrence of TransactionInformation
must be present.
On Condition
    /GroupHeader/GroupReturn is present
 And    /GroupHeader/GroupReturn is equal to value 'false'
Following Must be True
    /TransactionInformation[1] Must be present
This constraint is defined at the MessageDefinition level.
C20 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C21 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C22 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C23 InstructedAgentRule
If GroupHeader/InstructedAgent is present, then TransactionInformation/InstructedAgent is not
allowed.
On Condition
    /GroupHeader/InstructedAgent is present
Following Must be True
    /TransactionInformation[*]/InstructedAgent Must be absent
This constraint is defined at the MessageDefinition level.
C24 InstructedReimbursementAgentAccountRule
If InstructedReimbursementAgentAccount is present, then InstructedReimbursementAgent
must be present.
C25 InstructingAgentRule
If GroupHeader/InstructingAgent is present, then TransactionInformation/InstructingAgent is not
allowed.
On Condition
    /GroupHeader/InstructingAgent is present
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
267 March 2026
```

## File page 268

```text
Following Must be True
    /TransactionInformation[*]/InstructingAgent Must be absent
This constraint is defined at the MessageDefinition level.
C26 InstructingReimbursementAgentAccountRule
If InstructingReimbursementAgentAccount is present, then InstructingReimbursementAgent
must be present.
C27 IntermediaryAgent1AccountRule
If IntermediaryAgent1Account is present, then IntermediaryAgent1 must be present.
C28 IntermediaryAgent1AccountRule
If IntermediaryAgent1Account is present, then IntermediaryAgent1 must be present.
C29 IntermediaryAgent1AccountRule
If IntermediaryAgent1Account is present, then IntermediaryAgent1 must be present.
C30 IntermediaryAgent1Rule
If IntermediaryAgent1 is present, then CreditorAgent must be present.
C31 IntermediaryAgent2AccountRule
If IntermediaryAgent2Account is present, then IntermediaryAgent2 must be present.
C32 IntermediaryAgent2AccountRule
If IntermediaryAgent2Account is present, then IntermediaryAgent2 must be present.
C33 IntermediaryAgent2AccountRule
If IntermediaryAgent2Account is present, then IntermediaryAgent2 must be present.
C34 IntermediaryAgent2Rule
If IntermediaryAgent2 is present, then IntermediaryAgent1 must be present.
C35 IntermediaryAgent2Rule
If IntermediaryAgent2 is present, then IntermediaryAgent1 must be present.
C36 IntermediaryAgent3AccountRule
If IntermediaryAgent3Account is present, then IntermediaryAgent3 must be present.
C37 IntermediaryAgent3AccountRule
If IntermediaryAgent3Account is present, then IntermediaryAgent3 must be present.
C38 IntermediaryAgent3AccountRule
If IntermediaryAgent3Account is present, then IntermediaryAgent3 must be present.
C39 IntermediaryAgent3Rule
If IntermediaryAgent3 is present, then IntermediaryAgent2 must be present.
C40 IntermediaryAgent3Rule
If IntermediaryAgent3 is present, then IntermediaryAgent2 must be present.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
268 March 2026
```

## File page 269

```text
C41 NoCoverSettlementMethodRule
GroupHeader/SettlementInformation/SettlementMethod must be different from COVE (Cover)
when returning direct debit transactions.
On Condition
    /GroupHeader/SettlementInformation is present
 And    /GroupHeader/SettlementInformation/SettlementMethod is equal to value 
'CoverMethod'
Following Must be True
    substring(/OriginalGroupInformation/
OriginalMessageNameIdentification,1,8) Must be different from value 'pacs.003'
This constraint is defined at the MessageDefinition level.
C42 OriginalGroupInformationRule
If OriginalGroupInformation is present, then TransactionInformation/OriginalGroupInformation is
not allowed.
On Condition
    /OriginalGroupInformation is present
Following Must be True
    /TransactionInformation[*]/OriginalGroupInformation Must be absent
This constraint is defined at the MessageDefinition level.
C43 PaymentTypeInformationRule
If GroupHeader/PaymentTypeInformation is present, then TransactionInformation/
PaymentTypeInformation is not allowed.
On Condition
    /GroupHeader/PaymentTypeInformation is present
Following Must be True
    /TransactionInformation[*]/PaymentTypeInformation Must be absent
This constraint is defined at the MessageDefinition level.
C44 PreviousInstructingAgent1AccountRule
If PreviousInstructingAgent1Account is present, then PreviousInstructingAgent1 must be
present.
C45 PreviousInstructingAgent1AccountRule
If PreviousInstructingAgent1Account is present, then PreviousInstructingAgent1 must be
present.
C46 PreviousInstructingAgent1AccountRule
If PreviousInstructingAgent1Account is present, then PreviousInstructingAgent1 must be
present.
C47 PreviousInstructingAgent1Guideline
It is recommended that, when present, PreviousInstructingAgent1 is the closest to the
DebtorAgent in the payment chain.
C48 PreviousInstructingAgent1Guideline
It is recommended that, when present, PreviousInstructingAgent1 is the closest to the
DebtorAgent in the payment chain.
C49 PreviousInstructingAgent2AccountRule
If PreviousInstructingAgent2Account is present, then PreviousInstructingAgent2 must be
present.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
269 March 2026
```

## File page 270

```text
C50 PreviousInstructingAgent2AccountRule
If PreviousInstructingAgent2Account is present, then PreviousInstructingAgent2 must be
present.
C51 PreviousInstructingAgent2AccountRule
If PreviousInstructingAgent2Account is present, then PreviousInstructingAgent2 must be
present.
C52 PreviousInstructingAgent2Rule
If PreviousInstructingAgent2 is present, then PreviousInstructingAgent1 must be present.
C53 PreviousInstructingAgent2Rule
If PreviousInstructingAgent2 is present, then PreviousInstructingAgent1 must be present.
C54 PreviousInstructingAgent3AccountRule
If PreviousInstructingAgent3Account is present, then PreviousInstructingAgent3 must be
present.
C55 PreviousInstructingAgent3AccountRule
If PreviousInstructingAgent3Account is present, then PreviousInstructingAgent3 must be
present.
C56 PreviousInstructingAgent3AccountRule
If PreviousInstructingAgent3Account is present, then PreviousInstructingAgent3 must be
present.
C57 PreviousInstructingAgent3Rule
If PreviousInstructingAgent3 is present, then PreviousInstructingAgent2 must be present.
C58 PreviousInstructingAgent3Rule
If PreviousInstructingAgent3 is present, then PreviousInstructingAgent2 must be present.
C59 RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
C60 ReturnedInstructedAmountAndExchangeRate1Rule
If ReturnedInstructedAmount is present and the currency is different from the currency in
ReturnedInterbankSettlementAmount, then ExchangeRate must be present.
C61 ReturnedInstructedAmountAndExchangeRate2Rule
If ReturnedInstructedAmount is present and the currency is the same as the currency in
ReturnedInterbankSettlementAmount, then ExchangeRate is not allowed.
C62 ReturnReasonRule
If Reason/Code is equal to NARR, then AddititionalInformation must be present.
C63 SettlementMethodAgentRule
If SettlementMethod is equal to INDA or INGA, then ReimbursementAgent(s) and
ClearingSystem are not allowed.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
270 March 2026
```

## File page 271

```text
C64 SettlementMethodClearingRule
If SettlementMethod is equal to CLRG, then SettlementAccount and ReimbursementAgent(s)
are not allowed.
C65 SettlementMethodCoverAgentRule
If SettlementMethod is equal to COVE, then InstructedReimbursementAgent or
InstructingReimbursementAgent must be present.
C66 SettlementMethodCoverRule
If SettlementMethod is equal to COVE, then SettlementAccount and ClearingSystem are not
allowed.
C67 SupplementaryDataRule
The SupplementaryData building block at message level must not be used to provide additional
information about a transaction. The SupplementaryData element at transaction level should be
used for that purpose.
This constraint is defined at the MessageDefinition level.
C68 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C69 ThirdReimbursementAgentAccountRule
If ThirdReimbursementAgentAccount is present, then ThirdReimbursementAgent must be
present.
C70 ThirdReimbursementAgentRule
If ThirdReimbursementAgent is present, then InstructingReimbursementAgent and
InstructedReimbursementAgent must both be present.
C71 TotalInterbankSettlementAmountAndDateRule
If TotalReturnedInterbankSettlementAmount is present, then InterbankSettlementDate must be
present.
C72 TotalReturnedInterbankSettlementAmountAndSumRule
GroupHeader/TotalReturnedInterbankSettlementAmount must equal the sum of all occurrences
of TransactionInformation/ReturnedInterbankSettlementAmount when present.
On Condition
    /GroupHeader/TotalReturnedInterbankSettlementAmount is present
Following Must be True
    /GroupHeader/TotalReturnedInterbankSettlementAmount Must be equal to 
value 'sum of TransactionInformation/ReturnedInterbankSttlementAmount'
This constraint is defined at the MessageDefinition level.
C73 TotalReturnedInterbankSettlementAmountRule
If GroupHeader/TotalReturnedInterbankSettlementAmount is present, then all occurrences of
TransactionInformation/ReturnedInterbankSettlementAmount must have the same currency as
the currency of GroupHeader/TotalReturnedInterbankSettlementAmount.
On Condition
    /GroupHeader/TotalReturnedInterbankSettlementAmount is present
 And    /TransactionInformation[1] is present
 And    /TransactionInformation[*]/ReturnedInterbankSettlementAmount is 
present
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
271 March 2026
```

