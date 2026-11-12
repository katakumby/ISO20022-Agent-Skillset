---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "7.2 Structure"]
file_pages: [180]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.016.001.10"]
---

# 7.2 Structure

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 180 to 180.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 180

```text
7.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraPosMvmntPstngRpt> [1..1]  C19,
C20,
C21
   Pagination <Pgntn> [1..1] ± 183
   StatementGeneralDetails <StmtGnlDtls> [1..1] ± C18 183
   AccountOwner <AcctOwnr> [0..1] ± 184
   SafekeepingAccount <SfkpgAcct> [0..1] ± 184
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 185
   FinancialInstrument <FinInstrm> [0..*]  185
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C10,
C11,
C14,
C15,
C16
186
     FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C3, C17 187
     SubBalance <SubBal> [1..*]  C6 190
       SafekeepingPlace <SfkpgPlc> [0..1] ± 191
       BalanceFrom <BalFr> [1..1] ± 192
       IntraPositionMovement <IntraPosMvmnt> [1..*]  C4 192
         Identification <Id> [0..1] ± 193
         SettledQuantity <SttldQty> [1..1] ± C12 194
         PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± C12 194
         RemainingToBeSettledQuantity <RmngToBeSttldQty> [0..1] ± C12 194
         SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 195
         BalanceTo <BalTo> [1..1] ± 195
         SettlementDate <SttlmDt> [1..1] ± 195
         AvailableDate <AvlblDt> [0..1] ± 196
         AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 196
         CorporateActionEventType <CorpActnEvtTp> [0..1] ± C13 196
         CollateralMonitorAmount <CollMntrAmt> [0..1] ± 197
         InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 197
         SupplementaryData <SplmtryData> [0..*] ± C22 197
Approved by the Securities SEG on 27 January 2026 semt.016.001.10
IntraPositionMovementPostingReportV10
Settlement And Reconciliation - Maintenance 2025 - 2026 180 March 2026
```

