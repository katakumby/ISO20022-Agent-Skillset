---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["21 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "21.4 Message Building Blocks", "21.4.4 ReportOrError <RptOrErr>", "21.4.4.1 Cancellations <Cxls>", "21.4.4.1.5 Cancellation <Cxl>", "21.4.4.1.5.5 RequestReference <ReqRef>"]
file_pages: [511]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 21.4.4.1.5.5 RequestReference <ReqRef>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 511 to 511.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 511

```text
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
21.4.4.1.5.5  RequestReference <ReqRef>
Presence: [1..1]
Definition: Unambiguous identification of the cancellation request.
Datatype: "Max35Text" on page 3328
21.4.4.1.5.6  StatusDate <StsDt>
Presence: [0..1]
Definition: Date and time at which the status was assigned.
Datatype: "ISODateTime" on page 3320
21.4.4.1.5.7  TransactionIdentification <TxId>
Presence: [0..1]
Definition: References of the transaction for which the intra-balance modification is requested.
TransactionIdentification <TxId> contains the following References14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
21.4.4.1.5.7.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 511 August 2026
```

