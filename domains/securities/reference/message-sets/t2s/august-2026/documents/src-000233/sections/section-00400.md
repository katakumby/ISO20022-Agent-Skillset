---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["21 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "21.4 Message Building Blocks", "21.4.4 ReportOrError <RptOrErr>", "21.4.4.1 Cancellations <Cxls>", "21.4.4.1.5 Cancellation <Cxl>", "21.4.4.1.5.7 TransactionIdentification <TxId>", "21.4.4.1.5.7.2 AccountServicerTransactionIdentification <AcctSvcrTxId>"]
file_pages: [512, 513]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 21.4.4.1.5.7.2 AccountServicerTransactionIdentification <AcctSvcrTxId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 512 to 513.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 512

```text
Datatype: "Max35Text" on page 3328
21.4.4.1.5.7.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 3328
21.4.4.1.5.7.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 3328
21.4.4.1.5.7.4  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction as assigned by the processor.
Datatype: "Max35Text" on page 3328
21.4.4.1.5.7.5  PoolIdentification <PoolId>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 3328
21.4.4.1.5.8  UnderlyingIntraBalance <UndrlygIntraBal>
Presence: [0..1]
Definition: Identifies additional details of the transaction.
Impacted by: C5 "AdditionalDetailsRule", C8 "BalanceFromToRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 512 August 2026
```

## File page 513

```text
UnderlyingIntraBalance <UndrlygIntraBal> contains the following IntraBalance5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementAmount <SttlmAmt> [1..1] ± 514
   SettlementDate <SttlmDt> [1..1] ± 514
   BalanceFrom <BalFr> [1..1]  514
     Type <Tp> [1..1]  514
{Or       Code <Cd> [1..1] CodeSet 515
Or}       Proprietary <Prtry> [1..1] ± 515
     QuantityBreakdown <QtyBrkdwn> [0..*]  515
       LotNumber <LotNb> [0..1] ± 515
       LotAmount <LotAmt> [0..1] ± 516
       LotQuantity <LotQty> [0..1] ± 516
       CashSubBalanceType <CshSubBalTp> [0..1] ± 516
   BalanceTo <BalTo> [1..1]  517
     Type <Tp> [1..1]  517
{Or       Code <Cd> [1..1] CodeSet 517
Or}       Proprietary <Prtry> [1..1] ± 517
     QuantityBreakdown <QtyBrkdwn> [0..*]  518
       LotNumber <LotNb> [0..1] ± 518
       LotAmount <LotAmt> [0..1] ± 518
       LotQuantity <LotQty> [0..1] ± 519
       CashSubBalanceType <CshSubBalTp> [0..1] ± 519
   CashSubBalanceIdentification <CshSubBalId> [0..1] ± 519
   Priority <Prty> [0..1] ± 519
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 520
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the sender and the receiver, if
InstructionProcessingAdditionalDetails is present, then it must not contain information that can be
provided in a structured field.
• BalanceFromToRule
The cash balance type of BalanceFrom must be different from the cash balance type of BalanceTo.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 513 August 2026
```

