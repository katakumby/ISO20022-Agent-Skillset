---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "78.4 Message Building Blocks", "78.4.3 Cancellations <Cxls>", "78.4.3.3 ProcessingStatus <PrcgSts>"]
file_pages: [2710, 2711]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
---

# 78.4.3.3 ProcessingStatus <PrcgSts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2710 to 2711.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2710

```text
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
78.4.3.3  ProcessingStatus <PrcgSts>
Presence: [0..1]
Definition: Status and status reason of the transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus69Choice" on page 3185 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingCancellation <PdgCxl> [1..1] ± 3185
Or   Rejected <Rjctd> [1..1] ± 3185
Or   Repair <Rpr> [1..1] ± 3186
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 3186
Or   Proprietary <Prtry> [1..1] ± 3187
Or   Denied <Dnd> [1..1] ± 3187
Or}   Cancelled <Canc> [1..1] ± 3187
78.4.3.4  Cancellation <Cxl>
Presence: [1..*]
Definition: Identifies the individual transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities 2710 August 2026
```

## File page 2711

```text
Cancellation <Cxl> contains the following SecuritiesCancellationTransaction2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [0..1] ± 2712
   SafekeepingAccount <SfkpgAcct> [0..1] ± 2712
   ProcessingStatus <PrcgSts> [0..1] ± 2712
   RequestReference <ReqRef> [1..1] Text 2713
   StatusDate <StsDt> [0..1] DateTime 2713
   TransactionIdentification <TxId> [0..1]  2713
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 2713
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 2714
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 2714
     CounterpartyMarketInfrastructureTransactionIdentifi
cation <CtrPtyMktInfrstrctrTxId>
[0..1] Text 2714
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 2714
     PoolIdentification <PoolId> [0..1] Text 2714
   Underlying <Undrlyg> [0..1]  2714
{Or     IntraPositionMovement <IntraPosMvmnt> [1..1]  2715
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C15
2716
       SettlementQuantity <SttlmQty> [1..1] ± 2717
       SettlementDate <SttlmDt> [1..1] ± 2717
       BalanceFrom <BalFr> [0..1] ± 2717
       BalanceTo <BalTo> [0..1] ± 2718
       SecuritiesSubBalanceIdentification
<SctiesSubBalId>
[0..1] ± 2718
       Priority <Prty> [0..1] ± 2718
Or}     SettlementTransaction <SttlmTx> [1..1]  2718
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C15
2719
       SettlementQuantity <SttlmQty> [1..1] ± 2720
       SettlementAmount <SttlmAmt> [0..1] ± 2720
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities 2711 August 2026
```

