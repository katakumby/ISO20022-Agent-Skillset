---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["11 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02", "11.2 Structure"]
file_pages: [175, 176]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.073.001.02"]
---

# 11.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 175 to 176.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 175

```text
11.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntModReqStsAdvc> [1..1]  
   Identification <Id> [0..1]  178
     Identification <Id> [1..1] Text 179
     CreationDateTime <CreDtTm> [0..1] ± 179
     CopyDuplicate <CpyDplct> [0..1] CodeSet 179
     MessageOriginator <MsgOrgtr> [0..1] ± 180
     MessageRecipient <MsgRcpt> [0..1] ± 180
   RequestReference <ReqRef> [1..1] Text 180
   CashAccount <CshAcct> [1..1] ± C12,
C11
180
   CashAccountOwner <CshAcctOwnr> [0..1] ± 181
   CashAccountServicer <CshAcctSvcr> [0..1] ± 181
   RequestDetails <ReqDtls> [0..1]  C13,
C14
182
     Reference <Ref> [1..1]  184
       AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 184
       AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 184
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 184
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 184
       PoolIdentification <PoolId> [0..1] Text 185
     Linkage <Lkg> [0..1] ± 185
     Priority <Prty> [0..1] ± 185
     OtherProcessing <OthrPrcg> [0..*] ± 185
     PartialSettlementIndicator <PrtlSttlmInd> [0..1] Indicator 185
     ClearingChannel <ClrChanl> [0..1] CodeSet 186
     Linkages <Lnkgs> [0..*]  186
       ProcessingPosition <PrcgPos> [0..1] ± C17 187
       MessageNumber <MsgNb> [0..1] ± C15 187
       Reference <Ref> [1..1]  187
{Or         SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 188
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities 175 August 2026
```

## File page 176

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 188
Or         IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 188
Or         AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 188
Or         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 188
Or         PoolIdentification <PoolId> [1..1] Text 189
Or}         OtherTransactionIdentification <OthrTxId> [1..1] Text 189
       ReferenceOwner <RefOwnr> [0..1] ± 189
   ProcessingStatus <PrcgSts> [1..1] ± 189
   UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C3, C6 189
     SettlementAmount <SttlmAmt> [1..1] ± 191
     SettlementDate <SttlmDt> [1..1] ± 191
     BalanceFrom <BalFr> [1..1]  191
       Type <Tp> [1..1]  191
{Or         Code <Cd> [1..1] CodeSet 192
Or}         Proprietary <Prtry> [1..1] ± 192
       QuantityBreakdown <QtyBrkdwn> [0..*]  192
         LotNumber <LotNb> [0..1] ± 192
         LotAmount <LotAmt> [0..1] ± 193
         LotQuantity <LotQty> [0..1] ± 193
         CashSubBalanceType <CshSubBalTp> [0..1] ± 193
     BalanceTo <BalTo> [1..1]  194
       Type <Tp> [1..1]  194
{Or         Code <Cd> [1..1] CodeSet 194
Or}         Proprietary <Prtry> [1..1] ± 194
       QuantityBreakdown <QtyBrkdwn> [0..*]  195
         LotNumber <LotNb> [0..1] ± 195
         LotAmount <LotAmt> [0..1] ± 195
         LotQuantity <LotQty> [0..1] ± 196
         CashSubBalanceType <CshSubBalTp> [0..1] ± 196
     CashSubBalanceIdentification <CshSubBalId> [0..1] ± 196
     Priority <Prty> [0..1] ± 196
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities 176 August 2026
```

