---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "7.4 Message Building Blocks", "7.4.3 Cancellations <Cxls>", "7.4.3.4 Cancellation <Cxl>", "7.4.3.4.4 RequestReference <ReqRef>"]
file_pages: [158]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
---

# 7.4.3.4.4 RequestReference <ReqRef>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 158 to 158.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 158

```text
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus69Choice" on page 298 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingCancellation <PdgCxl> [1..1] ± 298
Or   Rejected <Rjctd> [1..1] ± 299
Or   Repair <Rpr> [1..1] ± 299
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 299
Or   Proprietary <Prtry> [1..1] ± 300
Or   Denied <Dnd> [1..1] ± 300
Or}   Cancelled <Canc> [1..1] ± 300
7.4.3.4.4  RequestReference <ReqRef>
Presence: [1..1]
Definition: Unambiguous identification of the cancellation request.
Datatype: "Max35Text" on page 345
7.4.3.4.5  StatusDate <StsDt>
Presence: [0..1]
Definition: Date and time at which the status was assigned.
Datatype: "ISODateTime" on page 340
7.4.3.4.6  TransactionIdentification <TxId>
Presence: [0..1]
Definition: References of the transaction for which the intra-position modification is requested.
TransactionIdentification <TxId> contains the following References33 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 158
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 159
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 159
   CounterpartyMarketInfrastructureTransactionIdentific
ation <CtrPtyMktInfrstrctrTxId>
[0..1] Text 159
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 159
   PoolIdentification <PoolId> [0..1] Text 159
7.4.3.4.6.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Approved by the Securities SEG on 21 August 2025 semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities - Settlement Restrictions 158 September 2025
```

