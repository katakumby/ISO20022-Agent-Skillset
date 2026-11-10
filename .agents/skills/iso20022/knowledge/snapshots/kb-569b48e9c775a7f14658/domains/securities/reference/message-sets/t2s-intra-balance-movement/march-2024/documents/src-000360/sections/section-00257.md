---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["14 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "14.4 Message Building Blocks", "14.4.3 ReportGeneralDetails <RptGnlDtls>", "14.4.3.9 ActivityIndicator <ActvtyInd>"]
file_pages: [310, 311]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 14.4.3.9 ActivityIndicator <ActvtyInd>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 310 to 311.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 310

```text
14.4.3.9  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 495):
• Meaning When True: Yes
• Meaning When False: No
14.4.4 ReportOrError <RptOrErr>
Presence: [0..1]
Definition: Provides information on report or error resulting from the originating query message.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
310 March 2024
```

## File page 311

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
312
     CashAccount <CshAcct> [0..1] ± C17,
C16
314
     CashAccountOwner <CshAcctOwnr> [0..1] ± 315
     CashAccountServicer <CshAcctSvcr> [0..1] ± 315
     ProcessingStatus <PrcgSts> [0..1] ± 316
     Cancellation <Cxl> [1..*]  316
       CashAccount <CshAcct> [0..1] ± C17,
C16
318
       CashAccountOwner <CshAcctOwnr> [0..1] ± 318
       CashAccountServicer <CshAcctSvcr> [0..1] ± 319
       ProcessingStatus <PrcgSts> [0..1] ± 319
       RequestReference <ReqRef> [1..1] Text 320
       StatusDate <StsDt> [0..1] DateTime 320
       TransactionIdentification <TxId> [0..1]  320
         AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 320
         AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 321
         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 321
         ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 321
         PoolIdentification <PoolId> [0..1] Text 321
       UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C5, C8 321
         SettlementAmount <SttlmAmt> [1..1] ± 323
         SettlementDate <SttlmDt> [1..1] ± 323
         BalanceFrom <BalFr> [1..1]  323
           Type <Tp> [1..1]  323
{Or             Code <Cd> [1..1] CodeSet 324
Or}             Proprietary <Prtry> [1..1] ± 324
           QuantityBreakdown <QtyBrkdwn> [0..*]  324
             LotNumber <LotNb> [0..1] ± 324
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
311 March 2024
```

