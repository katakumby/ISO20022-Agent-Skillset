---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.3 Constraints"]
file_pages: [1056, 1057, 1058]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
topic_continuations: [{"constraint_ids": ["C23", "C24", "C25", "C26"], "until_heading": "9.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 1059, "topic": "9.3 Constraints", "reference_path": "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00788.md"}]
---

# 9.3 Constraints

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1056 to 1058.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 9.3 Constraints topic continues in [Constraints continuation C23–C26 (file p1059)](section-00788.md#file-page-1059). Read the text before **9.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 1056

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       UltimateDebtor <UltmtDbtr> [0..1]  1145
{Or         Party <Pty> [1..1] ± 1146
Or}         Agent <Agt> [1..1] ± 1147
       Debtor <Dbtr> [0..1]  1148
{Or         Party <Pty> [1..1] ± 1148
Or}         Agent <Agt> [1..1] ± 1149
       DebtorAccount <DbtrAcct> [0..1] ± C12,
C11
1150
       DebtorAgent <DbtrAgt> [0..1] ± 1151
       DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C12,
C11
1151
       CreditorAgent <CdtrAgt> [0..1] ± 1152
       CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C12,
C11
1153
       Creditor <Cdtr> [0..1]  1154
{Or         Party <Pty> [1..1] ± 1154
Or}         Agent <Agt> [1..1] ± 1155
       CreditorAccount <CdtrAcct> [0..1] ± C12,
C11
1156
       UltimateCreditor <UltmtCdtr> [0..1]  1157
{Or         Party <Pty> [1..1] ± 1157
Or}         Agent <Agt> [1..1] ± 1158
       Purpose <Purp> [0..1] ± 1159
     SupplementaryData <SplmtryData> [0..*] ± C24 1159
   SupplementaryData <SplmtryData> [0..*] ± C24 0
9.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1056 March 2026
```

## File page 1057

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
C10 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C11 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C12 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C13 InstructedReimbursementAgentAccountRule
If InstructedReimbursementAgentAccount is present, then InstructedReimbursementAgent
must be present.
C14 InstructingReimbursementAgentAccountRule
If InstructingReimbursementAgentAccount is present, then InstructingReimbursementAgent
must be present.
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1057 March 2026
```

## File page 1058

```text
C15 OriginalGroupInformationAbsenceRule
If OriginalGroupInformation is absent, then
TransactionInformation[*]/OriginalGroupInformation must be present.
On Condition
    /OriginalGroupInformation[1] is absent
Following Must be True
    /TransactionInformation[*]/OriginalGroupInformation Must be present
This constraint is defined at the MessageDefinition level.
C16 OriginalGroupInformationMultiplePresenceRule
If OriginalGroupInformation is present and multiple times (Occurrence > 1), then
TransactionInformation[*]/OriginalGroupInformation must be present.
On Condition
    /OriginalGroupInformation[2] is present
Following Must be True
    /TransactionInformation[*]/OriginalGroupInformation Must be present
This constraint is defined at the MessageDefinition level.
C17 OriginalGroupInformationSinglePresenceRule
If OriginalGroupInformationAndStatus is present and only once, then
TransactionInformationAndStatus[*]/OriginalGroupInformation must be absent.
On Condition
    /OriginalGroupInformation[1] is present
 And    /OriginalGroupInformation[2] is absent
Following Must be True
    /TransactionInformation[*]/OriginalGroupInformation Must be absent
This constraint is defined at the MessageDefinition level.
C18 RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
C19 SettlementMethodAgentRule
If SettlementMethod is equal to INDA or INGA, then ReimbursementAgent(s) and
ClearingSystem are not allowed.
C20 SettlementMethodClearingRule
If SettlementMethod is equal to CLRG, then SettlementAccount and ReimbursementAgent(s)
are not allowed.
C21 SettlementMethodCoverAgentRule
If SettlementMethod is equal to COVE, then InstructedReimbursementAgent or
InstructingReimbursementAgent must be present.
C22 SettlementMethodCoverRule
If SettlementMethod is equal to COVE, then SettlementAccount and ClearingSystem are not
allowed.
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1058 March 2026
```

