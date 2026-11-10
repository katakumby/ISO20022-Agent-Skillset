---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02", "7.2 Structure"]
file_pages: [117]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.074.001.02"]
---

# 7.2 Structure

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 117 to 117.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 117

```text
7.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntCxlReq> [1..1]  
   Identification <Id> [0..1]  119
     Identification <Id> [1..1] Text 120
     CreationDateTime <CreDtTm> [0..1] ± 120
     CopyDuplicate <CpyDplct> [0..1] CodeSet 120
     MessageOriginator <MsgOrgtr> [0..1] ± 120
     MessageRecipient <MsgRcpt> [0..1] ± 121
   TransactionIdentification <TxId> [1..1]  121
     AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 121
     AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 121
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 121
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 122
     PoolIdentification <PoolId> [0..1] Text 122
   CashAccount <CshAcct> [1..1] ± C11,
C10
122
   CashAccountOwner <CshAcctOwnr> [0..1] ± 122
   CashAccountServicer <CshAcctSvcr> [0..1] ± 123
   UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C3, C5 123
     SettlementAmount <SttlmAmt> [1..1] ± 125
     SettlementDate <SttlmDt> [1..1] ± 125
     BalanceFrom <BalFr> [1..1]  125
       Type <Tp> [1..1]  125
{Or         Code <Cd> [1..1] CodeSet 126
Or}         Proprietary <Prtry> [1..1] ± 126
       QuantityBreakdown <QtyBrkdwn> [0..*]  126
         LotNumber <LotNb> [0..1] ± 126
         LotAmount <LotAmt> [0..1] ± 127
         LotQuantity <LotQty> [0..1] ± 127
         CashSubBalanceType <CshSubBalTp> [0..1] ± 127
     BalanceTo <BalTo> [1..1]  128
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.074.001.02
IntraBalanceMovementCancellationRequestV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
117 March 2024
```

