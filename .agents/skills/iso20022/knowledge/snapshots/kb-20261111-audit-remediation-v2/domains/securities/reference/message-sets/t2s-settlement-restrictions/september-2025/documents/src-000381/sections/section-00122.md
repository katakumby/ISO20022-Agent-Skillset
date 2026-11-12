---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "7.4 Message Building Blocks", "7.4.2 ReportGeneralDetails <RptGnlDtls>", "7.4.2.7 Frequency <Frqcy>"]
file_pages: [152, 153]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
---

# 7.4.2.7 Frequency <Frqcy>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 152 to 153.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 152

```text
Datatype: "MovementResponseType1Code" on page 331
CodeName Name Definition
FULL Full Response will include full details on the
movements reported.
STTS Status Response will include limited details
including the status on the movements
reported.
7.4.2.7  Frequency <Frqcy>
Presence: [0..1]
Definition: Frequency of the statement.
Frequency <Frqcy> contains one of the following elements (see "Frequency22Choice" on page 222 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 222
Or}   Proprietary <Prtry> [1..1] ± 223
7.4.2.8  UpdateType <UpdTp>
Presence: [1..1]
Definition: Indicates whether the statement is complete or contains changes only.
UpdateType <UpdTp> contains one of the following elements (see "UpdateType15Choice" on
page 250 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 250
Or}   Proprietary <Prtry> [1..1] ± 250
7.4.2.9  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 342):
• Meaning When True: Yes
• Meaning When False: No
7.4.3 Cancellations <Cxls>
Presence: [0..*]
Definition: Report on the transaction cancellation requests.
Impacted by: C1 "AccountOwnerRule", C20 "ProcessingStatusRule", C22 "SafekeepingAccountRule"
Approved by the Securities SEG on 21 August 2025 semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities - Settlement Restrictions 152 September 2025
```

## File page 153

```text
Cancellations <Cxls> contains the following SecuritiesCancellation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [0..1] ± 154
   SafekeepingAccount <SfkpgAcct> [0..1] ± 154
   ProcessingStatus <PrcgSts> [0..1] ± 155
   Cancellation <Cxl> [1..*]  155
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
       CounterpartyMarketInfrastructureTransactionIdenti
fication <CtrPtyMktInfrstrctrTxId>
[0..1] Text 159
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 159
       PoolIdentification <PoolId> [0..1] Text 159
     Underlying <Undrlyg> [0..1]  159
{Or       IntraPositionMovement <IntraPosMvmnt> [1..1]  160
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
Or}       SettlementTransaction <SttlmTx> [1..1]  163
Approved by the Securities SEG on 21 August 2025 semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities - Settlement Restrictions 153 September 2025
```

