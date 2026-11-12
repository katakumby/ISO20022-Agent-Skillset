---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.18 TransactionDetails <TxDtls>", "4.4.3.4.18.25 ValueDate <ValDt>"]
file_pages: [158]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.18.25 ValueDate <ValDt>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 158 to 158.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 158

```text
4.4.3.4.18.25  ValueDate <ValDt>
Presence: [0..1]
Definition: Date and time assets become available to the account owner (in a credit entry), or cease to
be available to the account owner (in a debit entry).
ValueDate <ValDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 321 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 321
Or}   DateTime <DtTm> [1..1] DateTime 321
4.4.3.4.18.26  StatusDate <StsDt>
Presence: [0..1]
Definition: Date and time at which the status was assigned.
Datatype: "ISODateTime" on page 551
4.4.3.4.18.27  AcknowledgedStatusTimeStamp <AckdStsTmStmp>
Presence: [0..1]
Definition: Time stamp on when the transaction is acknowledged.
Datatype: "ISODateTime" on page 551
4.4.3.4.18.28  MatchedStatusTimeStamp <MtchdStsTmStmp>
Presence: [0..1]
Definition: Time stamp on when the transaction is matched.
Datatype: "ISODateTime" on page 551
4.4.3.4.18.29  Linkages <Lnkgs>
Presence: [0..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 158 March 2026
```

