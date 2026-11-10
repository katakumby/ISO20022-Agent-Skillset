---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.4 Transaction <Tx>", "72.4.3.4.18 TransactionDetails <TxDtls>", "72.4.3.4.18.25 ValueDate <ValDt>"]
file_pages: [2554]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.4.18.25 ValueDate <ValDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2554 to 2554.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2554

```text
72.4.3.4.18.25  ValueDate <ValDt>
Presence: [0..1]
Definition: Date and time assets become available to the account owner (in a credit entry), or cease to
be available to the account owner (in a debit entry).
ValueDate <ValDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
72.4.3.4.18.26  StatusDate <StsDt>
Presence: [0..1]
Definition: Date and time at which the status was assigned.
Datatype: "ISODateTime" on page 3320
72.4.3.4.18.27  AcknowledgedStatusTimeStamp <AckdStsTmStmp>
Presence: [0..1]
Definition: Time stamp on when the transaction is acknowledged.
Datatype: "ISODateTime" on page 3320
72.4.3.4.18.28  MatchedStatusTimeStamp <MtchdStsTmStmp>
Presence: [0..1]
Definition: Time stamp on when the transaction is matched.
Datatype: "ISODateTime" on page 3320
72.4.3.4.18.29  Linkages <Lnkgs>
Presence: [0..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2554 August 2026
```

