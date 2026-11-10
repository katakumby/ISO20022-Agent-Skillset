---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["14 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "14.4 Message Building Blocks", "14.4.4 ReportOrError <RptOrErr>", "14.4.4.1 Cancellations <Cxls>", "14.4.4.1.5 Cancellation <Cxl>", "14.4.4.1.5.7 TransactionIdentification <TxId>", "14.4.4.1.5.7.2 AccountServicerTransactionIdentification <AcctSvcrTxId>"]
file_pages: [321, 322]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 14.4.4.1.5.7.2 AccountServicerTransactionIdentification <AcctSvcrTxId>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 321 to 322.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 321

```text
Datatype: "Max35Text" on page 497
14.4.4.1.5.7.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 497
14.4.4.1.5.7.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 497
14.4.4.1.5.7.4  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction as assigned by the processor.
Datatype: "Max35Text" on page 497
14.4.4.1.5.7.5  PoolIdentification <PoolId>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 497
14.4.4.1.5.8  UnderlyingIntraBalance <UndrlygIntraBal>
Presence: [0..1]
Definition: Identifies additional details of the transaction.
Impacted by: C5 "AdditionalDetailsRule", C8 "BalanceFromToRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
321 March 2024
```

## File page 322

```text
UnderlyingIntraBalance <UndrlygIntraBal> contains the following IntraBalance5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementAmount <SttlmAmt> [1..1] ± 323
   SettlementDate <SttlmDt> [1..1] ± 323
   BalanceFrom <BalFr> [1..1]  323
     Type <Tp> [1..1]  323
{Or       Code <Cd> [1..1] CodeSet 324
Or}       Proprietary <Prtry> [1..1] ± 324
     QuantityBreakdown <QtyBrkdwn> [0..*]  324
       LotNumber <LotNb> [0..1] ± 324
       LotAmount <LotAmt> [0..1] ± 325
       LotQuantity <LotQty> [0..1] ± 325
       CashSubBalanceType <CshSubBalTp> [0..1] ± 325
   BalanceTo <BalTo> [1..1]  326
     Type <Tp> [1..1]  326
{Or       Code <Cd> [1..1] CodeSet 326
Or}       Proprietary <Prtry> [1..1] ± 326
     QuantityBreakdown <QtyBrkdwn> [0..*]  327
       LotNumber <LotNb> [0..1] ± 327
       LotAmount <LotAmt> [0..1] ± 327
       LotQuantity <LotQty> [0..1] ± 328
       CashSubBalanceType <CshSubBalTp> [0..1] ± 328
   CashSubBalanceIdentification <CshSubBalId> [0..1] ± 328
   Priority <Prty> [0..1] ± 328
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 329
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the sender and the receiver, if
InstructionProcessingAdditionalDetails is present, then it must not contain information that can be
provided in a structured field.
• BalanceFromToRule
The cash balance type of BalanceFrom must be different from the cash balance type of BalanceTo.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
322 March 2024
```

