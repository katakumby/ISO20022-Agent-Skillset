---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "78.4 Message Building Blocks", "78.4.2 ReportGeneralDetails <RptGnlDtls>", "78.4.2.7 Frequency <Frqcy>"]
file_pages: [2707, 2708]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
---

# 78.4.2.7 Frequency <Frqcy>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2707 to 2708.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2707

```text
Datatype: "MovementResponseType1Code" on page 3264
CodeName Name Definition
FULL Full Response will include full details on the
movements reported.
STTS Status Response will include limited details
including the status on the movements
reported.
78.4.2.7  Frequency <Frqcy>
Presence: [0..1]
Definition: Frequency of the statement.
Frequency <Frqcy> contains one of the following elements (see "Frequency22Choice" on page 2958
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2958
Or}   Proprietary <Prtry> [1..1] ± 2959
78.4.2.8  UpdateType <UpdTp>
Presence: [1..1]
Definition: Indicates whether the statement is complete or contains changes only.
UpdateType <UpdTp> contains one of the following elements (see "UpdateType15Choice" on
page 3045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3045
Or}   Proprietary <Prtry> [1..1] ± 3045
78.4.2.9  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
78.4.3 Cancellations <Cxls>
Presence: [0..*]
Definition: Report on the transaction cancellation requests.
Impacted by: C1 "AccountOwnerRule", C20 "ProcessingStatusRule", C22 "SafekeepingAccountRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities 2707 August 2026
```

## File page 2708

```text
Cancellations <Cxls> contains the following SecuritiesCancellation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [0..1] ± 2709
   SafekeepingAccount <SfkpgAcct> [0..1] ± 2709
   ProcessingStatus <PrcgSts> [0..1] ± 2710
   Cancellation <Cxl> [1..*]  2710
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
       CounterpartyMarketInfrastructureTransactionIdenti
fication <CtrPtyMktInfrstrctrTxId>
[0..1] Text 2714
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 2714
       PoolIdentification <PoolId> [0..1] Text 2714
     Underlying <Undrlyg> [0..1]  2714
{Or       IntraPositionMovement <IntraPosMvmnt> [1..1]  2715
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
Or}       SettlementTransaction <SttlmTx> [1..1]  2718
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities 2708 August 2026
```

