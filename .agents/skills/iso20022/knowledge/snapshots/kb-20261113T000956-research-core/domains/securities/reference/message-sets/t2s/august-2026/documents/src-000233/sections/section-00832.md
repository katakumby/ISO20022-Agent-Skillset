---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.2.1.3 Debt <Debt>", "28.4.2.1.2.1.3.52 YieldCalculation <YldClctn>", "28.4.2.1.2.1.3.52.2 CalculationType <ClctnTp>", "28.4.2.1.2.1.3.52.2.2 Proprietary <Prtry>"]
file_pages: [1239]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.1.3.52.2.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1239 to 1239.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1239

```text
CodeName Name Definition
TRYL True The yield calculated with coupon dates
moved from a weekend or holiday to the
next valid settlement date.
WRST ToWorstConvention The lowest yield to all possible
redemption date scenarios.
28.4.2.1.2.1.3.52.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Calculation type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
28.4.2.1.2.1.3.52.3  RedemptionPrice <RedPric>
Presence: [0..1]
Definition: Price to which the yield has been calculated.
RedemptionPrice <RedPric> contains the following Price8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValueType <ValTp> [0..1] CodeSet 1239
   Value <Val> [1..1] ± 1240
   PriceType <PricTp> [0..1] CodeSet 1240
28.4.2.1.2.1.3.52.3.1  ValueType <ValTp>
Presence: [0..1]
Definition: Type of value in which the price is expressed.
Datatype: "PriceValueType3Code" on page 3281
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1239 August 2026
```

