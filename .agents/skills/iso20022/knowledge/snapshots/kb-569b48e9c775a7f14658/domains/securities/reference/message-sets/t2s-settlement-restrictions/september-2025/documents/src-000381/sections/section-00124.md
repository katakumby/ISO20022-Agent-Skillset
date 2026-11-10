---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "7.4 Message Building Blocks", "7.4.3 Cancellations <Cxls>", "7.4.3.3 ProcessingStatus <PrcgSts>"]
file_pages: [155, 156]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
---

# 7.4.3.3 ProcessingStatus <PrcgSts>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 155 to 156.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 155

```text
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 193 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 193
   Type <Tp> [0..1] ± 193
   Name <Nm> [0..1] Text 193
7.4.3.3  ProcessingStatus <PrcgSts>
Presence: [0..1]
Definition: Status and status reason of the transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus69Choice" on page 298 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingCancellation <PdgCxl> [1..1] ± 298
Or   Rejected <Rjctd> [1..1] ± 299
Or   Repair <Rpr> [1..1] ± 299
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 299
Or   Proprietary <Prtry> [1..1] ± 300
Or   Denied <Dnd> [1..1] ± 300
Or}   Cancelled <Canc> [1..1] ± 300
7.4.3.4  Cancellation <Cxl>
Presence: [1..*]
Definition: Identifies the individual transaction.
Approved by the Securities SEG on 21 August 2025 semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities - Settlement Restrictions 155 September 2025
```

## File page 156

```text
Cancellation <Cxl> contains the following SecuritiesCancellationTransaction2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [0..1] ± 157
   SafekeepingAccount <SfkpgAcct> [0..1] ± 157
   ProcessingStatus <PrcgSts> [0..1] ± 157
   RequestReference <ReqRef> [1..1] Text 158
   StatusDate <StsDt> [0..1] DateTime 158
   TransactionIdentification <TxId> [0..1]  158
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 158
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 159
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 159
     CounterpartyMarketInfrastructureTransactionIdentifi
cation <CtrPtyMktInfrstrctrTxId>
[0..1] Text 159
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 159
     PoolIdentification <PoolId> [0..1] Text 159
   Underlying <Undrlyg> [0..1]  159
{Or     IntraPositionMovement <IntraPosMvmnt> [1..1]  160
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C15
161
       SettlementQuantity <SttlmQty> [1..1] ± 162
       SettlementDate <SttlmDt> [1..1] ± 162
       BalanceFrom <BalFr> [0..1] ± 162
       BalanceTo <BalTo> [0..1] ± 163
       SecuritiesSubBalanceIdentification
<SctiesSubBalId>
[0..1] ± 163
       Priority <Prty> [0..1] ± 163
Or}     SettlementTransaction <SttlmTx> [1..1]  163
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C15
164
       SettlementQuantity <SttlmQty> [1..1] ± 165
       SettlementAmount <SttlmAmt> [0..1] ± 165
Approved by the Securities SEG on 21 August 2025 semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities - Settlement Restrictions 156 September 2025
```

