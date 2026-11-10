---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02", "12.2 Structure"]
file_pages: [200]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.074.001.02"]
---

# 12.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 200 to 200.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 200

```text
12.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntCxlReq> [1..1]  
   Identification <Id> [0..1]  202
     Identification <Id> [1..1] Text 203
     CreationDateTime <CreDtTm> [0..1] ± 203
     CopyDuplicate <CpyDplct> [0..1] CodeSet 203
     MessageOriginator <MsgOrgtr> [0..1] ± 203
     MessageRecipient <MsgRcpt> [0..1] ± 204
   TransactionIdentification <TxId> [1..1]  204
     AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 204
     AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 204
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 204
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 205
     PoolIdentification <PoolId> [0..1] Text 205
   CashAccount <CshAcct> [1..1] ± C11,
C10
205
   CashAccountOwner <CshAcctOwnr> [0..1] ± 205
   CashAccountServicer <CshAcctSvcr> [0..1] ± 206
   UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C3, C5 206
     SettlementAmount <SttlmAmt> [1..1] ± 208
     SettlementDate <SttlmDt> [1..1] ± 208
     BalanceFrom <BalFr> [1..1]  208
       Type <Tp> [1..1]  208
{Or         Code <Cd> [1..1] CodeSet 209
Or}         Proprietary <Prtry> [1..1] ± 209
       QuantityBreakdown <QtyBrkdwn> [0..*]  209
         LotNumber <LotNb> [0..1] ± 209
         LotAmount <LotAmt> [0..1] ± 210
         LotQuantity <LotQty> [0..1] ± 210
         CashSubBalanceType <CshSubBalTp> [0..1] ± 210
     BalanceTo <BalTo> [1..1]  211
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.074.001.02
IntraBalanceMovementCancellationRequestV02
Target2-Securities 200 August 2026
```

