---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "8.4 Message Building Blocks", "8.4.2 CreditInstruction <CdtInstr>", "8.4.2.21 DirectDebitTransactionInformation <DrctDbtTxInf>"]
file_pages: [1039]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.010.001.06"]
---

# 8.4.2.21 DirectDebitTransactionInformation <DrctDbtTxInf>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1039 to 1039.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1039

```text
InstructionForCreditorAgent <InstrForCdtrAgt> contains the following elements (see
"InstructionForCreditorAgent3" on page 1203 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [0..1] CodeSet 1203
   InstructionInformation <InstrInf> [0..1] Text 1203
8.4.2.21  DirectDebitTransactionInformation <DrctDbtTxInf>
Presence: [1..*]
Definition: Provides information on the individual debit transaction(s) included in the message.
Impacted by: C24 "UltimateDebtorGuideline"
DirectDebitTransactionInformation <DrctDbtTxInf> contains the following
DirectDebitTransactionInformation33 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Payments SEG on 12 January 2026 pacs.010.001.06 FinancialInstitutionDirectDebitV06
Payments Clearing and Settlement - Maintenance 2025 -
2026
1039 March 2026
```

