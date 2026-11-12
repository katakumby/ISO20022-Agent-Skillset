---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.31 InvestmentPlan17", "66.1.26.31.10 SecurityDetails <SctyDtls>"]
file_pages: [4795]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.31.10 SecurityDetails <SctyDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4795 to 4795.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4795

```text
CodeName Name Definition
STAN RoundToNearest Round up or down to the nearest whole
number.
DIST IssueFraction Do not round.
66.1.26.31.10  SecurityDetails <SctyDtls>
Presence: [1..50]
Definition: Security that an investment plan invests in, or from which the investment plan divests.
SecurityDetails <SctyDtls> contains the following Repartition6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] ± 4795
   FinancialInstrument <FinInstrm> [1..1] ± C20 4795
   CurrencyOfPlan <CcyOfPlan> [0..1] CodeSet C2 4796
66.1.26.31.10.1  Quantity <Qty>
Presence: [1..1]
Definition: Amount, units or percentage of financial instrument invested or withdrawn.
Quantity <Qty> contains one of the following elements (see "UnitsOrAmountOrPercentage1Choice" on
page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1, C13 5143
Or   Unit <Unit> [1..1] Quantity 5143
Or}   Percentage <Pctg> [1..1] Rate 5143
66.1.26.31.10.2  FinancialInstrument <FinInstrm>
Presence: [1..1]
Definition: Detailed information about the security or investment fund.
Impacted by: C20 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4795 May 2026
```

