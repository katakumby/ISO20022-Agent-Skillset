---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["6 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02", "6.2 Structure"]
file_pages: [92, 93]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.073.001.02"]
---

# 6.2 Structure

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 92 to 93.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 92

```text
6.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntModReqStsAdvc> [1..1]  
   Identification <Id> [0..1]  95
     Identification <Id> [1..1] Text 96
     CreationDateTime <CreDtTm> [0..1] ± 96
     CopyDuplicate <CpyDplct> [0..1] CodeSet 96
     MessageOriginator <MsgOrgtr> [0..1] ± 97
     MessageRecipient <MsgRcpt> [0..1] ± 97
   RequestReference <ReqRef> [1..1] Text 97
   CashAccount <CshAcct> [1..1] ± C12,
C11
97
   CashAccountOwner <CshAcctOwnr> [0..1] ± 98
   CashAccountServicer <CshAcctSvcr> [0..1] ± 98
   RequestDetails <ReqDtls> [0..1]  C13,
C14
99
     Reference <Ref> [1..1]  101
       AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 101
       AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 101
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 101
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 101
       PoolIdentification <PoolId> [0..1] Text 102
     Linkage <Lkg> [0..1] ± 102
     Priority <Prty> [0..1] ± 102
     OtherProcessing <OthrPrcg> [0..*] ± 102
     PartialSettlementIndicator <PrtlSttlmInd> [0..1] Indicator 102
     ClearingChannel <ClrChanl> [0..1] CodeSet 103
     Linkages <Lnkgs> [0..*]  103
       ProcessingPosition <PrcgPos> [0..1] ± C17 104
       MessageNumber <MsgNb> [0..1] ± C15 104
       Reference <Ref> [1..1]  104
{Or         SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 105
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
92 March 2024
```

## File page 93

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 105
Or         IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 105
Or         AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 105
Or         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 105
Or         PoolIdentification <PoolId> [1..1] Text 106
Or}         OtherTransactionIdentification <OthrTxId> [1..1] Text 106
       ReferenceOwner <RefOwnr> [0..1] ± 106
   ProcessingStatus <PrcgSts> [1..1] ± 106
   UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C3, C6 106
     SettlementAmount <SttlmAmt> [1..1] ± 108
     SettlementDate <SttlmDt> [1..1] ± 108
     BalanceFrom <BalFr> [1..1]  108
       Type <Tp> [1..1]  108
{Or         Code <Cd> [1..1] CodeSet 109
Or}         Proprietary <Prtry> [1..1] ± 109
       QuantityBreakdown <QtyBrkdwn> [0..*]  109
         LotNumber <LotNb> [0..1] ± 109
         LotAmount <LotAmt> [0..1] ± 110
         LotQuantity <LotQty> [0..1] ± 110
         CashSubBalanceType <CshSubBalTp> [0..1] ± 110
     BalanceTo <BalTo> [1..1]  111
       Type <Tp> [1..1]  111
{Or         Code <Cd> [1..1] CodeSet 111
Or}         Proprietary <Prtry> [1..1] ± 111
       QuantityBreakdown <QtyBrkdwn> [0..*]  112
         LotNumber <LotNb> [0..1] ± 112
         LotAmount <LotAmt> [0..1] ± 112
         LotQuantity <LotQty> [0..1] ± 113
         CashSubBalanceType <CshSubBalTp> [0..1] ± 113
     CashSubBalanceIdentification <CshSubBalId> [0..1] ± 113
     Priority <Prty> [0..1] ± 113
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
93 March 2024
```

