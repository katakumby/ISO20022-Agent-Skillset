---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08", "33.2 Structure"]
file_pages: [1302]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.039.001.08"]
---

# 33.2 Structure

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1302 to 1302.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1302

```text
33.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmTxModReqStsAdvc> [1..1]  C20,
C22,
C24
   ModificationRequestReference <ModReqRef> [1..1] Text 1305
   AccountOwner <AcctOwnr> [0..1] ± 1305
   SafekeepingAccount <SfkpgAcct> [0..1] ± 1306
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1306
   TransactionIdentification <TxId> [0..1] ± C1, C14 1306
   ModificationProcessingStatus <ModPrcgSts> [1..1]  1307
{Or     AcknowledgedAccepted <AckdAccptd> [1..1] ± 1308
Or     PendingProcessing <PdgPrcg> [1..1] ± 1308
Or     Denied <Dnd> [1..1] ± 1309
Or     Rejected <Rjctd> [1..1] ± 1309
Or     Repaired <Rprd> [1..1] ± 1309
Or     Modified <Modfd> [1..1]  1310
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1310
Or}       Reason <Rsn> [1..*]  1310
         Code <Cd> [1..1]  1311
{Or           Code <Cd> [1..1] CodeSet 1311
Or}           Proprietary <Prtry> [1..1] ± 1311
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1312
Or}     Proprietary <Prtry> [1..1] ± 1312
   TransactionDetails <TxDtls> [0..1]  1312
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C9, C10,
C12,
C13,
C15
1313
     SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1314
     Payment <Pmt> [1..1] CodeSet 1315
     SettlementQuantity <SttlmQty> [1..1] ± 1315
     SettlementAmount <SttlmAmt> [0..1] ± 1315
     DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  1316
Approved by the Securities SEG on 27 January 2026 sese.039.001.08
SecuritiesSettlementTransactionModificationReques
tStatusAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 1302 March 2026
```

