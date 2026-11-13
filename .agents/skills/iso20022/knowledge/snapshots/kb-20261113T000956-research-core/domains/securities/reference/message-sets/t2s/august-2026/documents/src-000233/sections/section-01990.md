---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "78.4 Message Building Blocks", "78.4.3 Cancellations <Cxls>", "78.4.3.4 Cancellation <Cxl>", "78.4.3.4.4 RequestReference <ReqRef>"]
file_pages: [2713]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
---

# 78.4.3.4.4 RequestReference <ReqRef>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2713 to 2713.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2713

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
78.4.3.4.4  RequestReference <ReqRef>
Presence: [1..1]
Definition: Unambiguous identification of the cancellation request.
Datatype: "Max35Text" on page 3328
78.4.3.4.5  StatusDate <StsDt>
Presence: [0..1]
Definition: Date and time at which the status was assigned.
Datatype: "ISODateTime" on page 3320
78.4.3.4.6  TransactionIdentification <TxId>
Presence: [0..1]
Definition: References of the transaction for which the intra-position modification is requested.
TransactionIdentification <TxId> contains the following References33 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 2713
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 2714
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 2714
   CounterpartyMarketInfrastructureTransactionIdentific
ation <CtrPtyMktInfrstrctrTxId>
[0..1] Text 2714
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 2714
   PoolIdentification <PoolId> [0..1] Text 2714
78.4.3.4.6.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities 2713 August 2026
```

