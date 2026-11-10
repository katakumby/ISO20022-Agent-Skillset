---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.22 Price", "7.1.22.5 PriceInformation20"]
file_pages: [447]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.22.5 PriceInformation20

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 447 to 447.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 447

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.22.5  PriceInformation20
Definition: Amount of money for which goods or services are offered, sold, or bought.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 447
   Value <Val> [1..1] ± 447
   ValueType <ValTp> [1..1] ± 448
   SourceOfPrice <SrcOfPric> [0..1] ± 448
   QuotationDate <QtnDt> [0..1] ± 448
Constraints
• ValueRule
If TypeOfPriceCode is not MRKT, then Value may not be expressed with UnknownIndicator.
7.1.22.5.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of price and information about the price.
Type <Tp> contains one of the following elements (see "TypeOfPrice28Choice" on page 449 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 450
Or}   Proprietary <Prtry> [1..1] ± 451
7.1.22.5.2  Value <Val>
Presence: [1..1]
Definition: Value of the price, for example, as a currency and value.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 447 March 2026
```

