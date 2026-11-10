---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02", "8.2 Structure"]
file_pages: [116]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.067.001.02"]
---

# 8.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 116 to 116.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 116

```text
8.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntStsAdvc> [1..1]  
   Identification <Id> [0..1]  118
     Identification <Id> [1..1] Text 119
     CreationDateTime <CreDtTm> [0..1] ± 119
     CopyDuplicate <CpyDplct> [0..1] CodeSet 119
     MessageOriginator <MsgOrgtr> [0..1] ± 120
     MessageRecipient <MsgRcpt> [0..1] ± 120
   TransactionIdentification <TxId> [1..1]  C13 120
     AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 121
     AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 121
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 121
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 121
   ProcessingStatus <PrcgSts> [0..1] ± 121
   SettlementStatus <SttlmSts> [0..1] ± C14 122
   CashAccount <CshAcct> [1..1] ± C12,
C11
122
   CashAccountOwner <CshAcctOwnr> [0..1] ± 123
   CashAccountServicer <CshAcctSvcr> [0..1] ± 123
   UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C3, C6 124
     SettlementAmount <SttlmAmt> [1..1] ± 126
     SettlementDate <SttlmDt> [1..1] ± 126
     BalanceFrom <BalFr> [1..1]  126
       Type <Tp> [1..1]  126
{Or         Code <Cd> [1..1] CodeSet 127
Or}         Proprietary <Prtry> [1..1] ± 127
       QuantityBreakdown <QtyBrkdwn> [0..*]  127
         LotNumber <LotNb> [0..1] ± 127
         LotAmount <LotAmt> [0..1] ± 128
         LotQuantity <LotQty> [0..1] ± 128
         CashSubBalanceType <CshSubBalTp> [0..1] ± 128
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities 116 August 2026
```

