---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 camt.072.001.02 IntraBalanceMovementModificationRequestV02", "5.2 Structure"]
file_pages: [68, 69]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.072.001.02"]
---

# 5.2 Structure

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 68 to 69.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 68

```text
5.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntModReq> [1..1]  
   Identification <Id> [0..1]  71
     Identification <Id> [1..1] Text 71
     CreationDateTime <CreDtTm> [0..1] ± 72
     CopyDuplicate <CpyDplct> [0..1] CodeSet 72
     MessageOriginator <MsgOrgtr> [0..1] ± 72
     MessageRecipient <MsgRcpt> [0..1] ± 72
   CashAccount <CshAcct> [1..1] ± C11,
C10
73
   CashAccountOwner <CshAcctOwnr> [0..1] ± 73
   CashAccountServicer <CshAcctSvcr> [0..1] ± 74
   RequestDetails <ReqDtls> [1..*]  C12,
C13
74
     Reference <Ref> [1..1]  76
       AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 76
       AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 76
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 76
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 76
       PoolIdentification <PoolId> [0..1] Text 77
     Linkage <Lkg> [0..1] ± 77
     Priority <Prty> [0..1] ± 77
     OtherProcessing <OthrPrcg> [0..*] ± 77
     PartialSettlementIndicator <PrtlSttlmInd> [0..1] Indicator 77
     ClearingChannel <ClrChanl> [0..1] CodeSet 78
     Linkages <Lnkgs> [0..*]  78
       ProcessingPosition <PrcgPos> [0..1] ± C16 79
       MessageNumber <MsgNb> [0..1] ± C14 79
       Reference <Ref> [1..1]  79
{Or         SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 80
Or         IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 80
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
68 March 2024
```

## File page 69

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 80
Or         AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 80
Or         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 80
Or         PoolIdentification <PoolId> [1..1] Text 81
Or}         OtherTransactionIdentification <OthrTxId> [1..1] Text 81
       ReferenceOwner <RefOwnr> [0..1] ± 81
   UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C3, C5 81
     SettlementAmount <SttlmAmt> [1..1] ± 83
     SettlementDate <SttlmDt> [1..1] ± 83
     BalanceFrom <BalFr> [1..1]  83
       Type <Tp> [1..1]  83
{Or         Code <Cd> [1..1] CodeSet 84
Or}         Proprietary <Prtry> [1..1] ± 84
       QuantityBreakdown <QtyBrkdwn> [0..*]  84
         LotNumber <LotNb> [0..1] ± 84
         LotAmount <LotAmt> [0..1] ± 85
         LotQuantity <LotQty> [0..1] ± 85
         CashSubBalanceType <CshSubBalTp> [0..1] ± 85
     BalanceTo <BalTo> [1..1]  86
       Type <Tp> [1..1]  86
{Or         Code <Cd> [1..1] CodeSet 86
Or}         Proprietary <Prtry> [1..1] ± 86
       QuantityBreakdown <QtyBrkdwn> [0..*]  87
         LotNumber <LotNb> [0..1] ± 87
         LotAmount <LotAmt> [0..1] ± 87
         LotQuantity <LotQty> [0..1] ± 88
         CashSubBalanceType <CshSubBalTp> [0..1] ± 88
     CashSubBalanceIdentification <CshSubBalId> [0..1] ± 88
     Priority <Prty> [0..1] ± 88
     InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls> [0..1] Text 89
   SupplementaryData <SplmtryData> [0..*] ± C15 89
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
69 March 2024
```

