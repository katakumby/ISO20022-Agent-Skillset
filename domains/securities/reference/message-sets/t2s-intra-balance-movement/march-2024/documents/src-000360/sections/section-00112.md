---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["8 camt.075.001.02 IntraBalanceMovementCancellationRequestStatusAdviceV02", "8.2 Structure"]
file_pages: [134]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.075.001.02"]
---

# 8.2 Structure

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 134 to 134.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 134

```text
8.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntCxlReqStsAdvc> [1..1]  
   Identification <Id> [0..1]  136
     Identification <Id> [1..1] Text 137
     CreationDateTime <CreDtTm> [0..1] ± 137
     CopyDuplicate <CpyDplct> [0..1] CodeSet 137
     MessageOriginator <MsgOrgtr> [0..1] ± 138
     MessageRecipient <MsgRcpt> [0..1] ± 138
   RequestReference <ReqRef> [1..1] Text 138
   TransactionIdentification <TxId> [1..1]  138
     AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 139
     AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 139
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 139
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 139
     PoolIdentification <PoolId> [0..1] Text 139
   ProcessingStatus <PrcgSts> [1..1] ± 139
   CashAccount <CshAcct> [1..1] ± C12,
C11
140
   CashAccountOwner <CshAcctOwnr> [0..1] ± 140
   CashAccountServicer <CshAcctSvcr> [0..1] ± 141
   UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C3, C6 141
     SettlementAmount <SttlmAmt> [1..1] ± 143
     SettlementDate <SttlmDt> [1..1] ± 143
     BalanceFrom <BalFr> [1..1]  143
       Type <Tp> [1..1]  143
{Or         Code <Cd> [1..1] CodeSet 144
Or}         Proprietary <Prtry> [1..1] ± 144
       QuantityBreakdown <QtyBrkdwn> [0..*]  144
         LotNumber <LotNb> [0..1] ± 144
         LotAmount <LotAmt> [0..1] ± 145
         LotQuantity <LotQty> [0..1] ± 145
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.075.001.02
IntraBalanceMovementCancellationRequestStatusA
dviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
134 March 2024
```

