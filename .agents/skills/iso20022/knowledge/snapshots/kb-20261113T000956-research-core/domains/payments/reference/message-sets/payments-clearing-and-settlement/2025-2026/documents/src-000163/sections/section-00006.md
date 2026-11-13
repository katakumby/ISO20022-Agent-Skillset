---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.3 Constraints"]
file_pages: [14, 15, 16, 17]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
topic_continuations: [{"constraint_ids": ["C27", "C28", "C29", "C30", "C31", "C32", "C33"], "until_heading": "2.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 18, "topic": "2.3 Constraints", "reference_path": "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00007.md"}]
---

# 2.3 Constraints

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 14 to 17.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 2.3 Constraints topic continues in [Constraints continuation C27–C33 (file p18)](section-00007.md#file-page-18). Read the text before **2.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 14

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 116
       UltimateDebtor <UltmtDbtr> [0..1]  116
{Or         Party <Pty> [1..1] ± 117
Or}         Agent <Agt> [1..1] ± 118
       Debtor <Dbtr> [0..1]  119
{Or         Party <Pty> [1..1] ± 119
Or}         Agent <Agt> [1..1] ± 120
       DebtorAccount <DbtrAcct> [0..1] ± C16,
C15
121
       DebtorAgent <DbtrAgt> [0..1] ± 122
       DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C16,
C15
122
       CreditorAgent <CdtrAgt> [0..1] ± 123
       CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C16,
C15
124
       Creditor <Cdtr> [0..1]  125
{Or         Party <Pty> [1..1] ± 125
Or}         Agent <Agt> [1..1] ± 126
       CreditorAccount <CdtrAcct> [0..1] ± C16,
C15
127
       UltimateCreditor <UltmtCdtr> [0..1]  128
{Or         Party <Pty> [1..1] ± 128
Or}         Agent <Agt> [1..1] ± 129
       Purpose <Purp> [0..1] ± 130
     SupplementaryData <SplmtryData> [0..*] ± C31 130
   SupplementaryData <SplmtryData> [0..*] ± C31 0
2.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
14 March 2026
```

## File page 15

```text
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
(AcceptedWithChange), then TransactionInformationAndStatus/TransactionStatus must be
different from RJCT (Rejected).
On Condition
    /OriginalGroupInformationAndStatus[*]/GroupStatus is present
 And    /OriginalGroupInformationAndStatus[*]/GroupStatus is within DataType 
<<Code>> ValidationRuleStatus1Code
 And    /TransactionInformationAndStatus[*]/TransactionStatus is present
Following Must be True
    /TransactionInformationAndStatus[*]/TransactionStatus Must not be within 
DataType <<Code>> ValidationRuleRejected1Code
This constraint is defined at the MessageDefinition level.
C11 GroupStatusPendingRule
If OriginalGroupInformationAndStatus/GroupStatus is present and is equal to PDNG (Pending),
then TransactionInformationAndStatus/TransactionStatus must be different from RJCT
(Rejected).
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
15 March 2026
```

## File page 16

```text
On Condition
    /OriginalGroupInformationAndStatus[*]/GroupStatus is present
 And    /OriginalGroupInformationAndStatus[*]/GroupStatus is within DataType 
<<Code>> ValidationRulePending1Code
 And    /TransactionInformationAndStatus[*]/TransactionStatus is present
Following Must be True
    /TransactionInformationAndStatus[*]/TransactionStatus Must not be within 
DataType <<Code>> ValidationRuleRejected1Code
This constraint is defined at the MessageDefinition level.
C12 GroupStatusReceivedRule
If OriginalGroupInformationAndStatus/GroupStatus is present and is equal to RCVD
(Received), then TransactionInformationAndStatus/TransactionStatus is not allowed.
On Condition
    /OriginalGroupInformationAndStatus[*]/GroupStatus is present
 And    /OriginalGroupInformationAndStatus[*]/GroupStatus is within DataType 
<<Code>> ValidationRuleReceived1Code
 And    /TransactionInformationAndStatus[1] is present
Following Must be True
    /TransactionInformationAndStatus[*]/TransactionStatus Must be absent
This constraint is defined at the MessageDefinition level.
C13 GroupStatusRejectedRule
If OriginalGroupInformationAndStatus/GroupStatus is present and is equal to RJCT (Rejected),
then TransactionInformationAndStatus/TransactionStatus, if present, must be equal to RJCT
(Rejected).
On Condition
    /OriginalGroupInformationAndStatus[*]/GroupStatus is present
 And    /OriginalGroupInformationAndStatus[*]/GroupStatus is within DataType 
<<Code>> ValidationRuleRejected1Code
 And    /TransactionInformationAndStatus[*]/TransactionStatus is present
Following Must be True
    /TransactionInformationAndStatus[*]/TransactionStatus Must be within 
DataType <<Code>> ValidationRuleRejected1Code
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
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
16 March 2026
```

## File page 17

```text
C19 NumberOfTransactionPerStatusGuideline
OriginalGroupInformationAndStatus/NumberOfTransactionsPerStatus should only be present if
GroupStatus equals 'PART'.
C20 OriginalGroupInformationAbsenceRule
If OriginalGroupInformationAndStatus is absent, then
TransactionInformationAndStatus[*]/OriginalGroupInformation must be present.
On Condition
    /OriginalGroupInformationAndStatus[1] is absent
Following Must be True
    /TransactionInformationAndStatus[*]/OriginalGroupInformation Must be 
present
This constraint is defined at the MessageDefinition level.
C21 OriginalGroupInformationMultiplePresenceRule
If OriginalGroupInformationAndStatus is present and multiple times (Occurrence > 1), then
TransactionInformationAndStatus[*]/OriginalGroupInformation must be present.
On Condition
    /OriginalGroupInformationAndStatus[2] is present
Following Must be True
    /TransactionInformationAndStatus[*]/OriginalGroupInformation Must be 
present
This constraint is defined at the MessageDefinition level.
C22 OriginalGroupInformationSinglePresenceRule
If OriginalGroupInformationAndStatus is present and only once, then
TransactionInformationAndStatus[*]/OriginalGroupInformation must be absent.
On Condition
    /OriginalGroupInformationAndStatus[1] is present
 And    /OriginalGroupInformationAndStatus[2] is absent
Following Must be True
    /TransactionInformationAndStatus[*]/OriginalGroupInformation Must be 
absent
This constraint is defined at the MessageDefinition level.
C23 RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
C24 SettlementMethodAgentRule
If SettlementMethod is equal to INDA or INGA, then ReimbursementAgent(s) and
ClearingSystem are not allowed.
C25 SettlementMethodClearingRule
If SettlementMethod is equal to CLRG, then SettlementAccount and ReimbursementAgent(s)
are not allowed.
C26 SettlementMethodCoverAgentRule
If SettlementMethod is equal to COVE, then InstructedReimbursementAgent or
InstructingReimbursementAgent must be present.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
17 March 2026
```

