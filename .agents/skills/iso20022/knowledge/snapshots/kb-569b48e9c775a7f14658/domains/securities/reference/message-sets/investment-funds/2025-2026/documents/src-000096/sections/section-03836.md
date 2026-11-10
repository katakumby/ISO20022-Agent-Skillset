---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.34 Price", "66.1.34.10 UnitPrice23"]
file_pages: [5125]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.34.10 UnitPrice23

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5125 to 5125.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5125

```text
66.1.34.10  UnitPrice23
Definition: Amount of money for which goods or services are offered, sold, or bought.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 5125
   Value <Val> [1..1] ± 5125
   PriceMethod <PricMtd> [0..1] CodeSet 5125
   AccruedInterestNAV <AcrdIntrstNAV> [0..1] Amount C2, C10 5126
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity 5126
   TaxableIncomePerShare <TaxblIncmPerShr> [0..1] Amount C1 5126
   TaxableIncomePerShareCalculated
<TaxblIncmPerShrClctd>
[0..1]  5127
{Or     Code <Cd> [1..1] CodeSet 5127
Or}     Proprietary <Prtry> [1..1] ± 5127
66.1.34.10.1  Type <Tp>
Presence: [1..1]
Definition: Type and information about a price.
Type <Tp> contains one of the following elements (see "TypeOfPrice46Choice" on page 5114 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5114
Or}   Proprietary <Prtry> [1..1] ± 5115
66.1.34.10.2  Value <Val>
Presence: [1..1]
Definition: Value of the price.
Value <Val> contains the following elements (see "PriceValue1" on page 5127 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1 5128
66.1.34.10.3  PriceMethod <PricMtd>
Presence: [0..1]
Definition: Type of pricing calculation method.
Datatype: "PriceMethod1Code" on page 5343
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5125 May 2026
```

