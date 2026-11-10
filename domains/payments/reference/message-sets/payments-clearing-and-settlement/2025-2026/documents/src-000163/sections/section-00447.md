---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.21 OriginalTransactionReference <OrgnlTxRef>", "5.4.3.21.1 InterbankSettlementAmount <IntrBkSttlmAmt>"]
file_pages: [618]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.21.1 InterbankSettlementAmount <IntrBkSttlmAmt>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 618 to 618.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 618

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         RemittedAmount <RmtdAmt> [0..1] Amount C2, C11 685
         FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 685
         EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 685
       SecuritiesData <SctiesData> [0..*]  685
         UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 686
         Amount <Amt> [0..1] Amount C1, C10 686
       AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 686
   UltimateDebtor <UltmtDbtr> [0..1]  686
{Or     Party <Pty> [1..1] ± 687
Or}     Agent <Agt> [1..1] ± 688
   Debtor <Dbtr> [0..1]  689
{Or     Party <Pty> [1..1] ± 689
Or}     Agent <Agt> [1..1] ± 690
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
{Or     Party <Pty> [1..1] ± 695
Or}     Agent <Agt> [1..1] ± 696
   CreditorAccount <CdtrAcct> [0..1] ± C20,
C19
697
   UltimateCreditor <UltmtCdtr> [0..1]  698
{Or     Party <Pty> [1..1] ± 698
Or}     Agent <Agt> [1..1] ± 699
   Purpose <Purp> [0..1] ± 700
5.4.3.21.1  InterbankSettlementAmount <IntrBkSttlmAmt>
Presence: [0..1]
Definition: Amount of money moved between the instructing agent and the instructed agent.
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
618 March 2026
```

