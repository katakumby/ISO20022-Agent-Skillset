---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["8 semt.034.001.01 IntraPositionMovementPendingReportV01", "8.4 Message Building Blocks", "8.4.5 Movements <Mvmnts>"]
file_pages: [177, 178]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.034.001.01"]
---

# 8.4.5 Movements <Mvmnts>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 177 to 178.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 177

```text
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 193 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 193
   Type <Tp> [0..1] ± 193
   Name <Nm> [0..1] Text 193
8.4.5 Movements <Mvmnts>
Presence: [0..*]
Definition: Identifies the transactions.
Impacted by: C19 "StatusAndReasonRule"
Approved by the Securities SEG on 21 August 2025 semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities - Settlement Restrictions 177 September 2025
```

## File page 178

```text
Movements <Mvmnts> contains the following IntraPositionPending11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatusAndReason <StsAndRsn> [0..1] ± 179
   Movement <Mvmnt> [1..*]  C13 179
     StatusAndReason <StsAndRsn> [0..1] ± 181
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 181
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 181
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 181
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 182
     CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 182
     PoolIdentification <PoolId> [0..1] Text 182
     BalanceFrom <BalFr> [1..1] ± 182
     BalanceTo <BalTo> [1..1] ± 182
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C11,
C12,
C14
182
     FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C4, C16 184
     SettlementQuantity <SttlmQty> [1..1] ± 186
     IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 186
     StatusDate <StsDt> [0..1] DateTime 187
     AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 187
     Linkages <Lnkgs> [0..*]  187
       ProcessingPosition <PrcgPos> [0..1] ± C21 188
       MessageNumber <MsgNb> [0..1] ± C18 188
       Reference <Ref> [1..1]  188
{Or         SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 189
Or         IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 189
Or         IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 189
Or         AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 189
Or         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 189
Approved by the Securities SEG on 21 August 2025 semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities - Settlement Restrictions 178 September 2025
```

