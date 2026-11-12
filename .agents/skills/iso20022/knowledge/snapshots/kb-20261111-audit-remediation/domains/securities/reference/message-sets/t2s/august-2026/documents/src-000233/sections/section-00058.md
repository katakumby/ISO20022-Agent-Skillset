---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["7 camt.066.001.02 IntraBalanceMovementInstructionV02", "7.2 Structure"]
file_pages: [95]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.066.001.02"]
---

# 7.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 95 to 95.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 95

```text
7.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntInstr> [1..1]  
   Identification <Id> [0..1]  98
     TransactionIdentification <TxId> [1..1] Text 98
     DocumentIdentification <DocId> [0..1] Text 98
     CreationDateTime <CreDtTm> [0..1] ± 99
     CopyDuplicate <CpyDplct> [0..1] CodeSet 99
     MessageOriginator <MsgOrgtr> [0..1] ± 99
     MessageRecipient <MsgRcpt> [0..1] ± 99
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 100
   NumberCounts <NbCounts> [0..1] ± C10 100
   Linkages <Lnkgs> [0..*]  100
     ProcessingPosition <PrcgPos> [0..1] ± C17 101
     MessageNumber <MsgNb> [0..1] ± C15 101
     Reference <Ref> [1..1]  102
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 102
Or       IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 103
Or       IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 103
Or       AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 103
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 103
Or       PoolIdentification <PoolId> [1..1] Text 103
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 103
     ReferenceOwner <RefOwnr> [0..1] ± 103
   CashAccount <CshAcct> [1..1] ± C14,
C13
104
   CashAccountOwner <CshAcctOwnr> [0..1] ± 104
   CashAccountServicer <CshAcctSvcr> [0..1] ± 105
   IntraBalance <IntraBal> [1..1]  C3, C5 105
     SettlementAmount <SttlmAmt> [1..1] ± 107
     SettlementDate <SttlmDt> [1..1] ± 107
     BalanceFrom <BalFr> [1..1]  107
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.066.001.02
IntraBalanceMovementInstructionV02
Target2-Securities 95 August 2026
```

