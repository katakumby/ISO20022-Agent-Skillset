---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02", "3.2 Structure"]
file_pages: [33]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.067.001.02"]
---

# 3.2 Structure

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 33 to 33.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 33

```text
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntStsAdvc> [1..1]  
   Identification <Id> [0..1]  35
     Identification <Id> [1..1] Text 36
     CreationDateTime <CreDtTm> [0..1] ± 36
     CopyDuplicate <CpyDplct> [0..1] CodeSet 36
     MessageOriginator <MsgOrgtr> [0..1] ± 37
     MessageRecipient <MsgRcpt> [0..1] ± 37
   TransactionIdentification <TxId> [1..1]  C13 37
     AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 38
     AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 38
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 38
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 38
   ProcessingStatus <PrcgSts> [0..1] ± 38
   SettlementStatus <SttlmSts> [0..1] ± C14 39
   CashAccount <CshAcct> [1..1] ± C12,
C11
39
   CashAccountOwner <CshAcctOwnr> [0..1] ± 40
   CashAccountServicer <CshAcctSvcr> [0..1] ± 40
   UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C3, C6 41
     SettlementAmount <SttlmAmt> [1..1] ± 43
     SettlementDate <SttlmDt> [1..1] ± 43
     BalanceFrom <BalFr> [1..1]  43
       Type <Tp> [1..1]  43
{Or         Code <Cd> [1..1] CodeSet 44
Or}         Proprietary <Prtry> [1..1] ± 44
       QuantityBreakdown <QtyBrkdwn> [0..*]  44
         LotNumber <LotNb> [0..1] ± 44
         LotAmount <LotAmt> [0..1] ± 45
         LotQuantity <LotQty> [0..1] ± 45
         CashSubBalanceType <CshSubBalTp> [0..1] ± 45
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
33 March 2024
```

