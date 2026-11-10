---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 semt.013.001.07 IntraPositionMovementInstructionV07", "5.2 Structure"]
file_pages: [151]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.014.001.09"]
---

# 5.2 Structure

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 151 to 151.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 151

```text
Additional information that cannot be captured in the structured elements and/or any other specific
block.
5.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraPosMvmntStsAdvc> [1..1]  
   TransactionIdentification <TxId> [1..1] ± C8 0
   Linkage <Lkg> [0..1]  0
     SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 153
   ProcessingStatus <PrcgSts> [0..1]  0
{Or     Rejected <Rjctd> [1..1] ± 154
Or     Repair <Rpr> [1..1] ± 154
Or     Cancelled <Canc> [1..1] ± 155
Or     AcknowledgedAccepted <AckdAccptd> [1..1] ± 155
Or}     Proprietary <Prtry> [1..1] ± 155
   SettlementStatus <SttlmSts> [0..1] ± C10 155
   TransactionDetails <TxDtls> [0..1]  C11,
C12,
C13
156
     PoolIdentification <PoolId> [0..1] Text 157
     AccountOwner <AcctOwnr> [0..1] ± 158
     SafekeepingAccount <SfkpgAcct> [0..1] ± 158
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 158
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C3, C4,
C6, C7,
C9
158
     SettlementQuantity <SttlmQty> [1..1] ± C5 159
     LotNumber <LotNb> [0..1] ± 160
     SettlementDate <SttlmDt> [1..1] ± 160
     AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 160
     BalanceFrom <BalFr> [0..1] ± 161
     BalanceTo <BalTo> [0..1] ± 161
   SupplementaryData <SplmtryData> [0..*] ± C14 0
Approved by the Securities SEG on 27 January 2026 semt.014.001.09
IntraPositionMovementStatusAdviceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 151 March 2026
```

