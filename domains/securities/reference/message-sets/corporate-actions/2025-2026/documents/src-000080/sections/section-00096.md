---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.19 DateDetails <DtDtls>", "3.4.11.19.8 DepositoryCoverExpirationDate <DpstryCoverXprtnDt>"]
file_pages: [151]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.19.8 DepositoryCoverExpirationDate <DpstryCoverXprtnDt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 151 to 151.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 151

```text
3.4.11.19.8  DepositoryCoverExpirationDate <DpstryCoverXprtnDt>
Presence: [0..1]
Definition: Last day that a participant of the depository can deliver securities that it had elected on
and/or previously protected.
DepositoryCoverExpirationDate <DpstryCoverXprtnDt> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
3.4.11.19.9  StockLendingDeadline <StockLndgDdln>
Presence: [0..1]
Definition: Date/time set as the deadline to respond, with instructions, to an outstanding event, for which
the underlying security is out on loan.
StockLendingDeadline <StockLndgDdln> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
3.4.11.19.10  BorrowerStockLendingDeadline <BrrwrStockLndgDdln>
Presence: [0..*]
Definition: Specifies the party borrowing stocks and the associated stock lending deadline assigned to
the borrower.
BorrowerStockLendingDeadline <BrrwrStockLndgDdln> contains the following
BorrowerLendingDeadline5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StockLendingDeadline <StockLndgDdln> [1..1] ± 151
   Borrower <Brrwr> [1..1] ± 152
3.4.11.19.10.1  StockLendingDeadline <StockLndgDdln>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 151 February 2026
```

