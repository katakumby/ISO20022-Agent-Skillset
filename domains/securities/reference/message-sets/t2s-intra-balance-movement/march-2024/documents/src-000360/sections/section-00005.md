---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 camt.066.001.02 IntraBalanceMovementInstructionV02", "2.2 Structure"]
file_pages: [12]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.066.001.02"]
---

# 2.2 Structure

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 12 to 12.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 12

```text
2.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntInstr> [1..1]  
   Identification <Id> [0..1]  15
     TransactionIdentification <TxId> [1..1] Text 15
     DocumentIdentification <DocId> [0..1] Text 15
     CreationDateTime <CreDtTm> [0..1] ± 16
     CopyDuplicate <CpyDplct> [0..1] CodeSet 16
     MessageOriginator <MsgOrgtr> [0..1] ± 16
     MessageRecipient <MsgRcpt> [0..1] ± 16
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 17
   NumberCounts <NbCounts> [0..1] ± C10 17
   Linkages <Lnkgs> [0..*]  17
     ProcessingPosition <PrcgPos> [0..1] ± C17 18
     MessageNumber <MsgNb> [0..1] ± C15 18
     Reference <Ref> [1..1]  19
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 19
Or       IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 20
Or       IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 20
Or       AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 20
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 20
Or       PoolIdentification <PoolId> [1..1] Text 20
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 20
     ReferenceOwner <RefOwnr> [0..1] ± 20
   CashAccount <CshAcct> [1..1] ± C14,
C13
21
   CashAccountOwner <CshAcctOwnr> [0..1] ± 21
   CashAccountServicer <CshAcctSvcr> [0..1] ± 22
   IntraBalance <IntraBal> [1..1]  C3, C5 22
     SettlementAmount <SttlmAmt> [1..1] ± 24
     SettlementDate <SttlmDt> [1..1] ± 24
     BalanceFrom <BalFr> [1..1]  24
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.066.001.02
IntraBalanceMovementInstructionV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
12 March 2024
```

