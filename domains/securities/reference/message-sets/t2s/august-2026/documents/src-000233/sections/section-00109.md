---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["10 camt.072.001.02 IntraBalanceMovementModificationRequestV02", "10.2 Structure"]
file_pages: [151, 152]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.072.001.02"]
---

# 10.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 151 to 152.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 151

```text
10.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntModReq> [1..1]  
   Identification <Id> [0..1]  154
     Identification <Id> [1..1] Text 154
     CreationDateTime <CreDtTm> [0..1] ± 155
     CopyDuplicate <CpyDplct> [0..1] CodeSet 155
     MessageOriginator <MsgOrgtr> [0..1] ± 155
     MessageRecipient <MsgRcpt> [0..1] ± 155
   CashAccount <CshAcct> [1..1] ± C11,
C10
156
   CashAccountOwner <CshAcctOwnr> [0..1] ± 156
   CashAccountServicer <CshAcctSvcr> [0..1] ± 157
   RequestDetails <ReqDtls> [1..*]  C12,
C13
157
     Reference <Ref> [1..1]  159
       AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 159
       AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 159
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 159
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 159
       PoolIdentification <PoolId> [0..1] Text 160
     Linkage <Lkg> [0..1] ± 160
     Priority <Prty> [0..1] ± 160
     OtherProcessing <OthrPrcg> [0..*] ± 160
     PartialSettlementIndicator <PrtlSttlmInd> [0..1] Indicator 160
     ClearingChannel <ClrChanl> [0..1] CodeSet 161
     Linkages <Lnkgs> [0..*]  161
       ProcessingPosition <PrcgPos> [0..1] ± C16 162
       MessageNumber <MsgNb> [0..1] ± C14 162
       Reference <Ref> [1..1]  162
{Or         SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 163
Or         IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 163
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities 151 August 2026
```

## File page 152

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 163
Or         AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 163
Or         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 163
Or         PoolIdentification <PoolId> [1..1] Text 164
Or}         OtherTransactionIdentification <OthrTxId> [1..1] Text 164
       ReferenceOwner <RefOwnr> [0..1] ± 164
   UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C3, C5 164
     SettlementAmount <SttlmAmt> [1..1] ± 166
     SettlementDate <SttlmDt> [1..1] ± 166
     BalanceFrom <BalFr> [1..1]  166
       Type <Tp> [1..1]  166
{Or         Code <Cd> [1..1] CodeSet 167
Or}         Proprietary <Prtry> [1..1] ± 167
       QuantityBreakdown <QtyBrkdwn> [0..*]  167
         LotNumber <LotNb> [0..1] ± 167
         LotAmount <LotAmt> [0..1] ± 168
         LotQuantity <LotQty> [0..1] ± 168
         CashSubBalanceType <CshSubBalTp> [0..1] ± 168
     BalanceTo <BalTo> [1..1]  169
       Type <Tp> [1..1]  169
{Or         Code <Cd> [1..1] CodeSet 169
Or}         Proprietary <Prtry> [1..1] ± 169
       QuantityBreakdown <QtyBrkdwn> [0..*]  170
         LotNumber <LotNb> [0..1] ± 170
         LotAmount <LotAmt> [0..1] ± 170
         LotQuantity <LotQty> [0..1] ± 171
         CashSubBalanceType <CshSubBalTp> [0..1] ± 171
     CashSubBalanceIdentification <CshSubBalId> [0..1] ± 171
     Priority <Prty> [0..1] ± 171
     InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls> [0..1] Text 172
   SupplementaryData <SplmtryData> [0..*] ± C15 172
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities 152 August 2026
```

