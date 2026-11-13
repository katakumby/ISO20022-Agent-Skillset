---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["14 sese.020.001.09 SecuritiesTransactionCancellationRequestV09", "14.4 Message Building Blocks", "14.4.9 TransactionDetails <TxDtls>", "14.4.9.3 SettlementDate <SttlmDt>"]
file_pages: [468]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.020.001.09"]
---

# 14.4.9.3 SettlementDate <SttlmDt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 468 to 468.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 468

```text
TradeDate <TradDt> contains one of the following elements (see "TradeDate8Choice" on page 1435 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 1435
Or}   DateCode <DtCd> [1..1]  1436
{Or     Code <Cd> [1..1] CodeSet 1436
Or}     Proprietary <Prtry> [1..1] ± 1436
14.4.9.3  SettlementDate <SttlmDt>
Presence: [1..1]
Definition: Date and time at which the securities are to be delivered or received.
SettlementDate <SttlmDt> contains one of the following elements (see "SettlementDate17Choice" on
page 1438 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 1439
Or}   DateCode <DtCd> [1..1] ± 1439
14.4.9.4  SettlementQuantity <SttlmQty>
Presence: [1..1]
Definition: Total quantity of securities to be settled.
SettlementQuantity <SttlmQty> contains one of the following elements (see "Quantity51Choice" on
page 1725 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C12 1725
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 1726
14.4.9.5  SettlementAmount <SttlmAmt>
Presence: [0..1]
Definition: Total amount of money to be paid or received in exchange for the securities.
Approved by the Securities SEG on 27 January 2026 sese.020.001.09
SecuritiesTransactionCancellationRequestV09
Settlement And Reconciliation - Maintenance 2025 - 2026 468 March 2026
```

