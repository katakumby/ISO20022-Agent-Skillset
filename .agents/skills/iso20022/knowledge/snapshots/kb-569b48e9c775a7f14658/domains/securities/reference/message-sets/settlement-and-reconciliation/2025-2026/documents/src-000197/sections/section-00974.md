---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.4 Balance", "35.1.4.2 BalanceAmounts1"]
file_pages: [1410]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.4.2 BalanceAmounts1

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1410 to 1410.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1410

```text
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown57" on
page 1722 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 1722
   LotQuantity <LotQty> [0..1] ± 1723
   LotDateTime <LotDtTm> [0..1] ± 1723
   LotPrice <LotPric> [0..1] ± 1723
   TypeOfPrice <TpOfPric> [0..1] ± 1723
35.1.4.2  BalanceAmounts1
Definition: Posting of an item to a cash account, in the context of a cash transaction, that results in an
increase or decrease to the balance of the account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldingValue <HldgVal> [1..1] ± 1410
   PreviousHoldingValue <PrvsHldgVal> [0..1] ± 1410
   BookValue <BookVal> [0..1] ± 1411
   UnrealisedGainLoss <UrlsdGnLoss> [0..1] ± 1411
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 1411
35.1.4.2.1  HoldingValue <HldgVal>
Presence: [1..1]
Definition: Value of an individual financial instrument holding within a safekeeping account.
HoldingValue <HldgVal> contains the following elements (see "AmountAndDirection6" on page 1361
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1362
   Sign <Sgn> [1..1] Indicator 1362
35.1.4.2.2  PreviousHoldingValue <PrvsHldgVal>
Presence: [0..1]
Definition: Previous value of an individual financial instrument holding within a safekeeping account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1410 March 2026
```

