---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.4 Message Building Blocks", "9.4.1 GroupHeader <GrpHdr>", "9.4.3.11 OriginalTransactionReference <OrgnlTxRef>", "9.4.3.11.1 InterbankSettlementAmount <IntrBkSttlmAmt>"]
file_pages: [1077]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
---

# 9.4.3.11.1 InterbankSettlementAmount <IntrBkSttlmAmt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1077 to 1077.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1077

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         RemittedAmount <RmtdAmt> [0..1] Amount C2, C8 1144
         FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 1144
         EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 1144
       SecuritiesData <SctiesData> [0..*]  1144
         UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 1145
         Amount <Amt> [0..1] Amount C1, C9 1145
       AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 1145
   UltimateDebtor <UltmtDbtr> [0..1]  1145
{Or     Party <Pty> [1..1] ± 1146
Or}     Agent <Agt> [1..1] ± 1147
   Debtor <Dbtr> [0..1]  1148
{Or     Party <Pty> [1..1] ± 1148
Or}     Agent <Agt> [1..1] ± 1149
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
{Or     Party <Pty> [1..1] ± 1154
Or}     Agent <Agt> [1..1] ± 1155
   CreditorAccount <CdtrAcct> [0..1] ± C12,
C11
1156
   UltimateCreditor <UltmtCdtr> [0..1]  1157
{Or     Party <Pty> [1..1] ± 1157
Or}     Agent <Agt> [1..1] ± 1158
   Purpose <Purp> [0..1] ± 1159
9.4.3.11.1  InterbankSettlementAmount <IntrBkSttlmAmt>
Presence: [0..1]
Definition: Amount of money moved between the instructing agent and the instructed agent.
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1077 March 2026
```

