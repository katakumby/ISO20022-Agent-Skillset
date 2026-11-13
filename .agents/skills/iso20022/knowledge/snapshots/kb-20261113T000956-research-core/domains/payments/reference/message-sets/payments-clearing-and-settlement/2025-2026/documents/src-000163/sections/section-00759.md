---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "8.3 Constraints"]
file_pages: [1018, 1019]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.010.001.06"]
topic_continuations: [{"constraint_ids": ["C15", "C16", "C17", "C18", "C19", "C20", "C21", "C22", "C23", "C24"], "until_heading": "8.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 1020, "topic": "8.3 Constraints", "reference_path": "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00760.md"}]
---

# 8.3 Constraints

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1018 to 1019.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 8.3 Constraints topic continues in [Constraints continuation C15–C24 (file p1020)](section-00760.md#file-page-1020). Read the text before **8.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 1018

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     CreditorAgent <CdtrAgt> [0..1] ± 1035
     CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C9, C8 1035
     Creditor <Cdtr> [1..1] ± 1036
     CreditorAccount <CdtrAcct> [0..1] ± C9, C8 1037
     UltimateCreditor <UltmtCdtr> [0..1] ± 1038
     InstructionForCreditorAgent <InstrForCdtrAgt> [0..*] ± 1038
     DirectDebitTransactionInformation <DrctDbtTxInf> [1..*]  C24 1039
       PaymentIdentification <PmtId> [1..1] ± C22 1040
       PaymentTypeInformation <PmtTpInf> [0..1] ± 1040
       InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount C1, C6 1041
       InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 1041
       SettlementPriority <SttlmPrty> [0..1] CodeSet 1042
       SettlementTimeIndication <SttlmTmIndctn> [0..1]  1042
         DebitDateTime <DbtDtTm> [0..1] DateTime 1042
         CreditDateTime <CdtDtTm> [0..1] DateTime 1042
       SettlementTimeRequest <SttlmTmReq> [0..1] ± 1042
       UltimateDebtor <UltmtDbtr> [0..1] ± 1043
       Debtor <Dbtr> [1..1] ± 1043
       DebtorAccount <DbtrAcct> [0..1] ± C9, C8 1044
       DebtorAgent <DbtrAgt> [0..1] ± 1045
       DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C9, C8 1045
       InstructionForDebtorAgent <InstrForDbtrAgt> [0..1] Text 1046
       Purpose <Purp> [0..1] ± 1046
       RemittanceInformation <RmtInf> [0..1] ± 1047
     SupplementaryData <SplmtryData> [0..*] ± C19 1047
   SupplementaryData <SplmtryData> [0..*] ± C19 1047
8.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
Approved by the Payments SEG on 12 January 2026 pacs.010.001.06 FinancialInstitutionDirectDebitV06
Payments Clearing and Settlement - Maintenance 2025 -
2026
1018 March 2026
```

## File page 1019

```text
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C4 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C5 CreditorAgentAccountRule
If CreditorAgentAccount is present, then CreditorAgent must be present.
C6 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C7 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C8 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C9 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C10 InterbankSettlementDateRule
If InterbankSettlementDate is present, then DirectDebitTransactionInformation/
InterbankSettlementDate is not allowed.
C11 IntermediaryAgent1AccountRule
If IntermediaryAgent1Account is present, then IntermediaryAgent1 must be present.
C12 IntermediaryAgent1Rule
If IntermediaryAgent1 is present, then CreditorAgent must be present.
C13 IntermediaryAgent2AccountRule
If IntermediaryAgent2Account is present, then IntermediaryAgent2 must be present.
C14 IntermediaryAgent2Rule
If IntermediaryAgent2 is present, then IntermediaryAgent1 must be present.
Approved by the Payments SEG on 12 January 2026 pacs.010.001.06 FinancialInstitutionDirectDebitV06
Payments Clearing and Settlement - Maintenance 2025 -
2026
1019 March 2026
```

