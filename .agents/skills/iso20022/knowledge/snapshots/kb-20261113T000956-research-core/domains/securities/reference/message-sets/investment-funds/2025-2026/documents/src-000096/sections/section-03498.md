---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.11 ModificationScope41", "66.1.26.11.2 InvestmentPlan <InvstmtPlan>", "66.1.26.11.2.10 SecurityDetails <SctyDtls>", "66.1.26.11.2.10.1 Quantity <Qty>"]
file_pages: [4748]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.11.2.10.1 Quantity <Qty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4748 to 4748.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4748

```text
SecurityDetails <SctyDtls> contains the following Repartition6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] ± 4748
   FinancialInstrument <FinInstrm> [1..1] ± C20 4748
   CurrencyOfPlan <CcyOfPlan> [0..1] CodeSet C2 4749
66.1.26.11.2.10.1  Quantity <Qty>
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
66.1.26.11.2.10.2  FinancialInstrument <FinInstrm>
Presence: [1..1]
Definition: Detailed information about the security or investment fund.
Impacted by: C20 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4748 May 2026
```

