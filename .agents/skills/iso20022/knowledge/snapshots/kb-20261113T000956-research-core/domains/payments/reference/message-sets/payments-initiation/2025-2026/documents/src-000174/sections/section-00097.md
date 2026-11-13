---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.3 Constraints"]
file_pages: [139, 140, 141, 142]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.3 Constraints

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 139 to 142.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 139

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}           Agent <Agt> [1..1] ± 266
         CreditorAccount <CdtrAcct> [0..1] ± C16,
C15
267
         UltimateCreditor <UltmtCdtr> [0..1]  268
{Or           Party <Pty> [1..1] ± 268
Or}           Agent <Agt> [1..1] ± 269
         Purpose <Purp> [0..1] ± 270
       SupplementaryData <SplmtryData> [0..*] ± C32 270
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
C7 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 139 March 2026
```

## File page 140

```text
C8 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 GroupStatusAcceptedRule
If OriginalGroupInformationAndStatus/GroupStatus is present and is equal to ACTC
(AcceptedTechnicalValidation), ACCP (AcceptedCustomerProfile), ACSP
(AcceptedSettlementInProcess), ACSC (AcceptedSettlementCompleted) or ACWC
(AcceptedWithChange), then OriginalPaymentInformationAndStatus/PaymentInformationStatus
must be different from RJCT (Rejected).
On Condition
    /OriginalGroupInformationAndStatus/GroupStatus is present
 And    /OriginalGroupInformationAndStatus/GroupStatus is within DataType 
<<Code>> ValidationRuleStatus1Code
 And    /OriginalPaymentInformationAndStatus[*]/PaymentInformationStatus is 
present
Following Must be True
    /OriginalPaymentInformationAndStatus[*]/PaymentInformationStatus Must not 
be within DataType <<Code>> ValidationRuleRejected1Code
This constraint is defined at the MessageDefinition level.
C11 GroupStatusPendingRule
If OriginalGroupInformationAndStatus/GroupStatus is present and is equal to PDNG (Pending),
then OriginalPaymentInformationAndStatus/PaymentInformationStatus must be different from
RJCT (Rejected).
On Condition
    /OriginalGroupInformationAndStatus/GroupStatus is present
 And    /OriginalGroupInformationAndStatus/GroupStatus is within DataType 
<<Code>> ValidationRulePending1Code
 And    /OriginalPaymentInformationAndStatus[*]/PaymentInformationStatus is 
present
Following Must be True
    /OriginalPaymentInformationAndStatus[*]/PaymentInformationStatus Must not 
be within DataType <<Code>> ValidationRuleRejected1Code
This constraint is defined at the MessageDefinition level.
C12 GroupStatusReceivedRule
If OriginalGroupInformationAndStatus/GroupStatus is present and is equal to RCVD
(Received), then OriginalPaymentInformationAndStatus/PaymentInformationStatus is not
allowed.
On Condition
    /OriginalGroupInformationAndStatus/GroupStatus is present
 And    /OriginalGroupInformationAndStatus/GroupStatus is within DataType 
<<Code>> ValidationRuleReceived1Code
 And    /OriginalPaymentInformationAndStatus[1] is present
Following Must be True
    /OriginalPaymentInformationAndStatus[*]/PaymentInformationStatus Must be 
absent
This constraint is defined at the MessageDefinition level.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 140 March 2026
```

## File page 141

```text
C13 GroupStatusRejectedRule
If OriginalGroupInformationAndStatus/GroupStatus is present and is equal to RJCT (Rejected),
then OriginalPaymentInformationAndStatus/PaymentInformationStatus, if present, must be
equal to RJCT (Rejected).
On Condition
    /OriginalGroupInformationAndStatus/GroupStatus is present
 And    /OriginalGroupInformationAndStatus/GroupStatus is within DataType 
<<Code>> ValidationRuleRejected1Code
 And    /OriginalPaymentInformationAndStatus[*]/PaymentInformationStatus is 
present
Following Must be True
    /OriginalPaymentInformationAndStatus[*]/PaymentInformationStatus Must be 
within DataType <<Code>> ValidationRuleRejected1Code
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
C17 InstructedReimbursementAgentAccountRule
If InstructedReimbursementAgentAccount is present, then InstructedReimbursementAgent
must be present.
C18 InstructingReimbursementAgentAccountRule
If InstructingReimbursementAgentAccount is present, then InstructingReimbursementAgent
must be present.
C19 NumberOfTransactionPerStatusGuideline
OriginalGroupInformationAndStatus/NumberOfTransactionsPerStatus should only be present if
GroupStatus equals 'PART'.
C20 PaymentInformationStatusAcceptedRule
If PaymentInformationStatus is present and is equal to ACTC (AcceptedTechnicalValidation),
ACCP (AcceptedCustomerProfile), ACSP (AcceptedSettlementInProcess), ACSC
(AcceptedSettlementCompleted) or ACWC (AcceptedWithChange), then
TransactionInformationAndStatus/TransactionStatus must be different from RJCT (Rejected).
C21 PaymentInformationStatusPendingRule
If OriginalPaymentInformationAndStatus/PaymentInformationStatus is present and is equal to
PDNG (Pending), then TransactionInformationAndStatus/TransactionStatus must be different
from RJCT (Rejected).
C22 PaymentInformationStatusReceivedRule
If OriginalPaymentInformationAndStatus/PaymentInformationStatus is present and is equal to
RCVD (Received), then TransactionInformationAndStatus/TransactionStatus is not allowed.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 141 March 2026
```

## File page 142

```text
C23 PaymentInformationStatusRejectedRule
If OriginalPaymentInformationAndStatus/PaymentInformationStatus is present and is equal to
RJCT (Rejceted), then TransactionInformationAndStatus/TransactionStatus, if present, must be
equal to RJCT (Rejected).
C24 RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
C25 SettlementMethodAgentRule
If SettlementMethod is equal to INDA or INGA, then ReimbursementAgent(s) and
ClearingSystem are not allowed.
C26 SettlementMethodClearingRule
If SettlementMethod is equal to CLRG, then SettlementAccount and ReimbursementAgent(s)
are not allowed.
C27 SettlementMethodCoverAgentRule
If SettlementMethod is equal to COVE, then InstructedReimbursementAgent or
InstructingReimbursementAgent must be present.
C28 SettlementMethodCoverRule
If SettlementMethod is equal to COVE, then SettlementAccount and ClearingSystem are not
allowed.
C29 StatusReasonInformationRule
If GroupStatus is present and is different from RJCT or PDNG then StatusReasonInformation/
AdditionalInformation must be absent.
C30 StatusReasonRule
If Reason/Code is equal to NARR, then AddititionalInformation must be present.
C31 SupplementaryDataRule
The SupplementaryData building block at message level must not be used to provide additional
information about a transaction. The SupplementaryData element at transaction level should be
used for that purpose.
This constraint is defined at the MessageDefinition level.
C32 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C33 ThirdReimbursementAgentAccountRule
If ThirdReimbursementAgentAccount is present, then ThirdReimbursementAgent must be
present.
C34 ThirdReimbursementAgentRule
If ThirdReimbursementAgent is present, then InstructingReimbursementAgent and
InstructedReimbursementAgent must both be present.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 142 March 2026
```

