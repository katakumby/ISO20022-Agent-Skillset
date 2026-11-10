---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "8.2 Structure"]
file_pages: [1017]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.010.001.06"]
---

# 8.2 Structure

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1017 to 1017.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1017

```text
8.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FIDrctDbt> [1..1]  C18
   GroupHeader <GrpHdr> [1..1]  1020
     MessageIdentification <MsgId> [1..1] Text 1021
     CreationDateTime <CreDtTm> [1..1] DateTime 1021
     NumberOfTransactions <NbOfTxs> [1..1] Text 1021
     ControlSum <CtrlSum> [0..1] Quantity 1021
     InstructingAgent <InstgAgt> [0..1] ± 1021
     InstructedAgent <InstdAgt> [0..1] ± 1022
   CreditInstruction <CdtInstr> [1..*]  C5, C10,
C11,
C12,
C13,
C14,
C15,
C16,
C17,
C20,
C21,
C23
1023
     CreditIdentification <CdtId> [1..1] Text 1027
     BatchBooking <BtchBookg> [0..1] Indicator 1027
     PaymentTypeInformation <PmtTpInf> [0..1] ± 1027
     TotalInterbankSettlementAmount <TtlIntrBkSttlmAmt> [0..1] Amount C1, C6 1027
     InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 1028
     SettlementTimeIndication <SttlmTmIndctn> [0..1]  1028
       DebitDateTime <DbtDtTm> [0..1] DateTime 1028
       CreditDateTime <CdtDtTm> [0..1] DateTime 1028
     InstructingAgent <InstgAgt> [0..1] ± 1029
     InstructedAgent <InstdAgt> [0..1] ± 1029
     IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 1030
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1] ± C9, C8 1031
     IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 1032
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1] ± C9, C8 1032
     IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 1033
     IntermediaryAgent3Account <IntrmyAgt3Acct> [0..1] ± C9, C8 1034
Approved by the Payments SEG on 12 January 2026 pacs.010.001.06 FinancialInstitutionDirectDebitV06
Payments Clearing and Settlement - Maintenance 2025 -
2026
1017 March 2026
```

