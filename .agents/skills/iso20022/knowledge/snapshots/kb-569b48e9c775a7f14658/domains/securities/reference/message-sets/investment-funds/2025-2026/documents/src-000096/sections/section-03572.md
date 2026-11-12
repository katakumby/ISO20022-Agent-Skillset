---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.8 FundCashInBreakdown3", "66.1.28.8.4 InvestmentFundTransactionInType <InvstmtFndTxInTp>", "66.1.28.8.4.2 Proprietary <Prtry>"]
file_pages: [4822]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.8.4.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4822 to 4822.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4822

```text
CodeName Name Definition
CROI CrossIn Transaction is a cross-in.
RDIV ReinvestmentOfDividend Transaction is a reinvestment of
dividend.
66.1.28.8.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Transaction type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.28.8.5  OriginalOrderQuantityType <OrgnlOrdrQtyTp>
Presence: [1..1]
Definition: Specifies how the original order was expressed that resulted in the cash-in movement, that is
cash or units.
OriginalOrderQuantityType <OrgnlOrdrQtyTp> contains one of the following QuantityType1Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4822
Or}   Proprietary <Prtry> [1..1] ± 4822
66.1.28.8.5.1  Code <Cd>
Presence: [1..1]
Definition: Quantity type expressed as a code.
Datatype: "OrderQuantityType2Code" on page 5333
CodeName Name Definition
UNIT Unit Order is placed by unit.
CASH Amount Order is placed by amount of money.
66.1.28.8.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Quantity type expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4822 May 2026
```

