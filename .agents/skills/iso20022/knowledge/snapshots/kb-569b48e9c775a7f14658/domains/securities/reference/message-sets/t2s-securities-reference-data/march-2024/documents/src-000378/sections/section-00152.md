---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.52 YieldCalculation <YldClctn>", "13.1.2.3.52.2 CalculationType <ClctnTp>", "13.1.2.3.52.2.2 Proprietary <Prtry>"]
file_pages: [216]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.52.2.2 Proprietary <Prtry>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 216 to 216.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 216

```text
CodeName Name Definition
TRYL True The yield calculated with coupon dates
moved from a weekend or holiday to the
next valid settlement date.
WRST ToWorstConvention The lowest yield to all possible
redemption date scenarios.
13.1.2.3.52.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Calculation type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.2.3.52.3  RedemptionPrice <RedPric>
Presence: [0..1]
Definition: Price to which the yield has been calculated.
RedemptionPrice <RedPric> contains the following Price8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValueType <ValTp> [0..1] CodeSet 216
   Value <Val> [1..1] ± 217
   PriceType <PricTp> [0..1] CodeSet 217
13.1.2.3.52.3.1  ValueType <ValTp>
Presence: [0..1]
Definition: Type of value in which the price is expressed.
Datatype: "PriceValueType3Code" on page 521
CodeName Name Definition
DISC Discount Price expressed as a number of
percentage points below par, for
example, a discount price of 2.0%
equals a price of 98 when par is 100.
PREM Premium Price expressed as a number of
percentage points above par, for
example, a premium price of 2.0%
equals a price of 102 when par is 100.
PARV Par Price is the face amount.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 216 March 2024
```

