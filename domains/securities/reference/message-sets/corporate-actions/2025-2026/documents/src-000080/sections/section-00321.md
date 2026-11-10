---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.18 DateDetails <DtDtls>", "7.4.13.18.10 BorrowerStockLendingDeadline <BrrwrStockLndgDdln>"]
file_pages: [441]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.18.10 BorrowerStockLendingDeadline <BrrwrStockLndgDdln>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 441 to 441.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 441

```text
7.4.13.18.10  BorrowerStockLendingDeadline <BrrwrStockLndgDdln>
Presence: [0..*]
Definition: Specifies the party borrowing stocks and the associated stock lending deadline assigned to
the borrower.
BorrowerStockLendingDeadline <BrrwrStockLndgDdln> contains the following
BorrowerLendingDeadline5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StockLendingDeadline <StockLndgDdln> [1..1] ± 441
   Borrower <Brrwr> [1..1] ± 441
7.4.13.18.10.1  StockLendingDeadline <StockLndgDdln>
Presence: [1..1]
Definition: Date/time set as the deadline to respond, with instructions, to an outstanding event for which
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
7.4.13.18.10.2  Borrower <Brrwr>
Presence: [1..1]
Definition: Party who has borrowed stocks on loan.
Borrower <Brrwr> contains one of the following elements (see "PartyIdentification127Choice" on
page 1037 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1038
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 1038
7.4.13.18.11  DocumentationDeadline <DcmnttnDdln>
Presence: [0..1]
Definition: Date/Time by when the documentation must be provided.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 441 February 2026
```

