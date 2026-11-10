---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 semt.015.001.10 IntraPositionMovementConfirmationV10", "6.2 Structure"]
file_pages: [164]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.015.001.10"]
---

# 6.2 Structure

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 164 to 164.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 164

```text
6.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraPosMvmntConf> [1..1]  C18,
C19,
C20
   AdditionalParameters <AddtlParams> [0..1] ± 167
   Linkage <Lkg> [0..1]  167
     SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 167
   AccountOwner <AcctOwnr> [0..1] ± 168
   SafekeepingAccount <SfkpgAcct> [0..1] ± 168
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 168
   SafekeepingPlace <SfkpgPlc> [0..1] ± 168
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C10,
C11,
C14,
C15,
C16
169
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C3, C17 170
   IntraPositionDetails <IntraPosDtls> [1..1]  C4, C6 172
     SettledQuantity <SttldQty> [1..1] ± C12 173
     SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 174
     CollateralMonitorAmount <CollMntrAmt> [0..1] ± 174
     PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± C12 174
     RemainingToBeSettledQuantity <RmngToBeSttldQty> [0..1] ± C12 175
     SettlementDate <SttlmDt> [1..1] ± 175
     AvailableDate <AvlblDt> [0..1] ± 176
     CorporateActionEventType <CorpActnEvtTp> [0..1] ± C13 176
     BalanceFrom <BalFr> [1..1] ± 176
     BalanceTo <BalTo> [1..1] ± 177
     InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls> [0..1] Text 177
   SupplementaryData <SplmtryData> [0..*] ± C21 177
Approved by the Securities SEG on 27 January 2026 semt.015.001.10
IntraPositionMovementConfirmationV10
Settlement And Reconciliation - Maintenance 2025 - 2026 164 March 2026
```

