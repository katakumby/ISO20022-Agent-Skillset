---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["21 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "21.4 Message Building Blocks", "21.4.3 ReportGeneralDetails <RptGnlDtls>", "21.4.3.9 ActivityIndicator <ActvtyInd>"]
file_pages: [501, 502]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 21.4.3.9 ActivityIndicator <ActvtyInd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 501 to 502.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 501

```text
21.4.3.9  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
21.4.4 ReportOrError <RptOrErr>
Presence: [0..1]
Definition: Provides information on report or error resulting from the originating query message.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 501 August 2026
```

## File page 502

```text
ReportOrError <RptOrErr> contains one of the following IntraBalanceOrOperationalError10Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Cancellations <Cxls> [1..*]  C10,
C11,
C12,
C18
503
     CashAccount <CshAcct> [0..1] ± C17,
C16
505
     CashAccountOwner <CshAcctOwnr> [0..1] ± 506
     CashAccountServicer <CshAcctSvcr> [0..1] ± 506
     ProcessingStatus <PrcgSts> [0..1] ± 507
     Cancellation <Cxl> [1..*]  507
       CashAccount <CshAcct> [0..1] ± C17,
C16
509
       CashAccountOwner <CshAcctOwnr> [0..1] ± 509
       CashAccountServicer <CshAcctSvcr> [0..1] ± 510
       ProcessingStatus <PrcgSts> [0..1] ± 510
       RequestReference <ReqRef> [1..1] Text 511
       StatusDate <StsDt> [0..1] DateTime 511
       TransactionIdentification <TxId> [0..1]  511
         AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 511
         AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 512
         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 512
         ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 512
         PoolIdentification <PoolId> [0..1] Text 512
       UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C5, C8 512
         SettlementAmount <SttlmAmt> [1..1] ± 514
         SettlementDate <SttlmDt> [1..1] ± 514
         BalanceFrom <BalFr> [1..1]  514
           Type <Tp> [1..1]  514
{Or             Code <Cd> [1..1] CodeSet 515
Or}             Proprietary <Prtry> [1..1] ± 515
           QuantityBreakdown <QtyBrkdwn> [0..*]  515
             LotNumber <LotNb> [0..1] ± 515
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 502 August 2026
```

