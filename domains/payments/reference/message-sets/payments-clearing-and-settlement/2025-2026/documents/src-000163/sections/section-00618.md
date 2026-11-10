---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: []
file_pages: [841]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# Continuation at file page 841

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 841 to 841.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 841

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1] ± C16,
C15
999
       IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 1000
       IntermediaryAgent3Account <IntrmyAgt3Acct> [0..1] ± C16,
C15
1001
       UltimateDebtor <UltmtDbtr> [0..1] ± 1002
       Debtor <Dbtr> [1..1] ± 1002
       DebtorAccount <DbtrAcct> [0..1] ± C16,
C15
1003
       DebtorAgent <DbtrAgt> [0..1] ± 1004
       DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C16,
C15
1004
       CreditorAgent <CdtrAgt> [0..1] ± 1005
       CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C16,
C15
1006
       Creditor <Cdtr> [1..1] ± 1007
       CreditorAccount <CdtrAcct> [0..1] ± C16,
C15
1007
       UltimateCreditor <UltmtCdtr> [0..1] ± 1008
       InstructionForCreditorAgent <InstrForCdtrAgt> [0..*] ± 1009
       InstructionForNextAgent <InstrForNxtAgt> [0..*]  1009
         Code <Cd> [0..1] CodeSet 1010
         InstructionInformation <InstrInf> [0..1] Text 1010
       Purpose <Purp> [0..1] ± 1010
       RegulatoryReporting <RgltryRptg> [0..10] ± 1010
       RemittanceInformation <RmtInf> [0..1] ± 1011
       UnderlyingAllocation <UndrlygAllcn> [0..*]  C78 1011
         Amount <Amt> [1..1] Amount C2, C9 1012
         CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 1012
         Account <Acct> [1..1] ± C16,
C15
1013
         Purpose <Purp> [1..1] ± 1013
         Reference <Ref> [1..1] Text 1013
         RelatedReferences <RltdRefs> [0..*] ± 1014
     SupplementaryData <SplmtryData> [0..*] ± C64 1014
   SupplementaryData <SplmtryData> [0..*] ± C64 1015
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
841 March 2026
```

