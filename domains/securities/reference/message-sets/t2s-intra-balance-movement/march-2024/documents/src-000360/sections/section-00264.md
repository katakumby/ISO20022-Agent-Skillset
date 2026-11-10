---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["14 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "14.4 Message Building Blocks", "14.4.4 ReportOrError <RptOrErr>", "14.4.4.1 Cancellations <Cxls>", "14.4.4.1.5 Cancellation <Cxl>", "14.4.4.1.5.5 RequestReference <ReqRef>"]
file_pages: [320]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 14.4.4.1.5.5 RequestReference <ReqRef>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 320 to 320.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 320

```text
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus69Choice" on page 452 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingCancellation <PdgCxl> [1..1] ± 453
Or   Rejected <Rjctd> [1..1] ± 453
Or   Repair <Rpr> [1..1] ± 453
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 454
Or   Proprietary <Prtry> [1..1] ± 454
Or   Denied <Dnd> [1..1] ± 454
Or}   Cancelled <Canc> [1..1] ± 455
14.4.4.1.5.5  RequestReference <ReqRef>
Presence: [1..1]
Definition: Unambiguous identification of the cancellation request.
Datatype: "Max35Text" on page 497
14.4.4.1.5.6  StatusDate <StsDt>
Presence: [0..1]
Definition: Date and time at which the status was assigned.
Datatype: "ISODateTime" on page 493
14.4.4.1.5.7  TransactionIdentification <TxId>
Presence: [0..1]
Definition: References of the transaction for which the intra-balance modification is requested.
TransactionIdentification <TxId> contains the following References14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
14.4.4.1.5.7.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
320 March 2024
```

