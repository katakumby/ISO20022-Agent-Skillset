---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13", "19.4 Message Building Blocks", "19.4.2 Linkages <Lnkgs>", "19.4.4.6 TradeDate <TradDt>"]
file_pages: [618]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.025.001.13"]
---

# 19.4.4.6 TradeDate <TradDt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 618 to 618.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 618

```text
19.4.4.6  TradeDate <TradDt>
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
19.4.4.7  SettlementDate <SttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are to be delivered or received.
SettlementDate <SttlmDt> contains one of the following elements (see "SettlementDate17Choice" on
page 1438 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 1439
Or}   DateCode <DtCd> [1..1] ± 1439
19.4.4.8  EffectiveSettlementDate <FctvSttlmDt>
Presence: [1..1]
Definition: Date and time at which a transaction is completed and cleared, for example, payment is
effected and securities are delivered.
EffectiveSettlementDate <FctvSttlmDt> contains one of the following elements (see
"SettlementDate18Choice" on page 1440 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 1440
Or}   DateCode <DtCd> [1..1] ± 1440
19.4.4.9  DealPrice <DealPric>
Presence: [0..1]
Definition: Specifies the price of the traded financial instrument.
This is the deal price of the individual trade transaction.
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 618 March 2026
```

