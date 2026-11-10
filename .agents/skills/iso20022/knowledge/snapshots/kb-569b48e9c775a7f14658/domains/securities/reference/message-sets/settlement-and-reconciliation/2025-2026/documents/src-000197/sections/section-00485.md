---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12", "22.4 Message Building Blocks", "22.4.4 CounterpartyMarketInfrastructureTransactionIdentification <CtrPtyMktInfrstrctrTxId>", "22.4.5.8 TradeDate <TradDt>"]
file_pages: [742]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.028.001.12"]
---

# 22.4.5.8 TradeDate <TradDt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 742 to 742.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 742

```text
22.4.5.8  TradeDate <TradDt>
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
22.4.5.9  SettlementDate <SttlmDt>
Presence: [1..1]
Definition: Date and time at which the securities are to be delivered or received.
SettlementDate <SttlmDt> contains one of the following elements (see "SettlementDate17Choice" on
page 1438 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 1439
Or}   DateCode <DtCd> [1..1] ± 1439
22.4.5.10  DealPrice <DealPric>
Presence: [0..1]
Definition: Specifies the price of the traded financial instrument.
This is the deal price of the individual trade transaction.
If there is only one trade transaction for the execution of the trade, then the deal price could equal the
executed trade price (unless, for example, the price includes commissions or rounding, or some other
factor has been applied to the deal price or the executed trade price, or both).
DealPrice <DealPric> contains the following elements (see "Price10" on page 1712 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  1712
{Or     Yielded <Yldd> [1..1] Indicator 1712
Or}     ValueType <ValTp> [1..1] CodeSet 1712
   Value <Val> [1..1] ± 1713
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 742 March 2026
```

