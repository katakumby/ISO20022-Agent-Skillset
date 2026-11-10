---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.6.2 Transaction <Tx>", "9.4.6.2.15 TransactionDetails <TxDtls>", "9.4.6.2.15.17 LateDeliveryDate <LateDlvryDt>"]
file_pages: [323]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.6.2.15.17 LateDeliveryDate <LateDlvryDt>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 323 to 323.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 323

```text
SettlementDate <SttlmDt> contains one of the following elements (see "SettlementDate19Choice" on
page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 1441
Or}   DateCode <DtCd> [1..1] ± 1441
9.4.6.2.15.17  LateDeliveryDate <LateDlvryDt>
Presence: [0..1]
Definition: Date and time after the settlement date specified in the trade, used for pool trades resulting
from the original To Be Assigned (TBA) securities.
LateDeliveryDate <LateDlvryDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
9.4.6.2.15.18  ExpectedValueDate <XpctdValDt>
Presence: [0..1]
Definition: For against payment transactions, the value date/time at which the account servicer expects
the settlement amount to be credited or debited.
ExpectedValueDate <XpctdValDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
9.4.6.2.15.19  AcknowledgedStatusTimeStamp <AckdStsTmStmp>
Presence: [0..1]
Definition: Time stamp on when the transaction is acknowledged.
Datatype: "ISODateTime" on page 2185
9.4.6.2.15.20  MatchedStatusTimeStamp <MtchdStsTmStmp>
Presence: [0..1]
Definition: Time stamp on when the transaction is matched.
Datatype: "ISODateTime" on page 2185
9.4.6.2.15.21  DeliveringSettlementParties <DlvrgSttlmPties>
Presence: [0..1]
Definition: Identifies the chain of delivering settlement parties.
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 323 March 2026
```

