---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["13 camt.075.001.02 IntraBalanceMovementCancellationRequestStatusAdviceV02", "13.2 Structure"]
file_pages: [217]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.075.001.02"]
---

# 13.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 217 to 217.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 217

```text
13.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntCxlReqStsAdvc> [1..1]  
   Identification <Id> [0..1]  219
     Identification <Id> [1..1] Text 220
     CreationDateTime <CreDtTm> [0..1] ± 220
     CopyDuplicate <CpyDplct> [0..1] CodeSet 220
     MessageOriginator <MsgOrgtr> [0..1] ± 221
     MessageRecipient <MsgRcpt> [0..1] ± 221
   RequestReference <ReqRef> [1..1] Text 221
   TransactionIdentification <TxId> [1..1]  221
     AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 222
     AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 222
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 222
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 222
     PoolIdentification <PoolId> [0..1] Text 222
   ProcessingStatus <PrcgSts> [1..1] ± 222
   CashAccount <CshAcct> [1..1] ± C12,
C11
223
   CashAccountOwner <CshAcctOwnr> [0..1] ± 223
   CashAccountServicer <CshAcctSvcr> [0..1] ± 224
   UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C3, C6 224
     SettlementAmount <SttlmAmt> [1..1] ± 226
     SettlementDate <SttlmDt> [1..1] ± 226
     BalanceFrom <BalFr> [1..1]  226
       Type <Tp> [1..1]  226
{Or         Code <Cd> [1..1] CodeSet 227
Or}         Proprietary <Prtry> [1..1] ± 227
       QuantityBreakdown <QtyBrkdwn> [0..*]  227
         LotNumber <LotNb> [0..1] ± 227
         LotAmount <LotAmt> [0..1] ± 228
         LotQuantity <LotQty> [0..1] ± 228
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.075.001.02
IntraBalanceMovementCancellationRequestStatusA
dviceV02
Target2-Securities 217 August 2026
```

