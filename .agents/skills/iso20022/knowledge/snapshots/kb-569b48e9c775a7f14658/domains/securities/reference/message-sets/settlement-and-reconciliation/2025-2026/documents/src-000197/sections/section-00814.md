---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.2 Deletion <Deltn>", "32.4.2.2.3 TradeDetails <TradDtls>", "32.4.2.2.3.6 TradeDate <TradDt>"]
file_pages: [1222]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.2.3.6 TradeDate <TradDt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1222 to 1222.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1222

```text
PlaceOfClearing <PlcOfClr> contains the following elements (see "PlaceOfClearingIdentification2" on
page 1434 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] IdentifierSet C5 1434
   LEI <LEI> [0..1] IdentifierSet 1434
32.4.2.2.3.6  TradeDate <TradDt>
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
32.4.2.2.3.7  LateDeliveryDate <LateDlvryDt>
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
32.4.2.2.3.8  DealPrice <DealPric>
Presence: [0..1]
Definition: Specifies the price of the traded financial instrument.
This is the deal price of the individual trade transaction.
If there is only one trade transaction for the execution of the trade, then the deal price could equal the
executed trade price (unless, for example, the price includes commissions or rounding, or some other
factor has been applied to the deal price or the executed trade price, or both).
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1222 March 2026
```

