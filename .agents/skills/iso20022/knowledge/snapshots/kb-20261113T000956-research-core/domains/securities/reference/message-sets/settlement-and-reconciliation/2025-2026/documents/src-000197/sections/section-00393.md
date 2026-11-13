---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "18.4 Message Building Blocks", "18.4.4 InferredMatchingStatus <IfrrdMtchgSts>", "18.4.7.24 SettlementDate <SttlmDt>"]
file_pages: [592]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.024.001.14"]
---

# 18.4.7.24 SettlementDate <SttlmDt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 592 to 592.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 592

```text
ExpectedValueDate <XpctdValDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
18.4.7.24  SettlementDate <SttlmDt>
Presence: [1..1]
Definition: Date and time at which the securities are to be delivered or received.
SettlementDate <SttlmDt> contains one of the following elements (see "SettlementDate19Choice" on
page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 1441
Or}   DateCode <DtCd> [1..1] ± 1441
18.4.7.25  TradeDate <TradDt>
Presence: [0..1]
Definition: Specifies the date/time on which the trade was executed.
TradeDate <TradDt> contains one of the following elements (see "TradeDate8Choice" on page 1435
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 1435
Or}   DateCode <DtCd> [1..1]  1436
{Or     Code <Cd> [1..1] CodeSet 1436
Or}     Proprietary <Prtry> [1..1] ± 1436
18.4.7.26  AcknowledgedStatusTimeStamp <AckdStsTmStmp>
Presence: [0..1]
Definition: Time stamp on when the transaction is acknowledged.
Datatype: "ISODateTime" on page 2185
18.4.7.27  MatchedStatusTimeStamp <MtchdStsTmStmp>
Presence: [0..1]
Definition: Time stamp on when the transaction is matched.
Datatype: "ISODateTime" on page 2185
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 592 March 2026
```

