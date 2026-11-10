---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.77 PriceRange <PricRg>"]
file_pages: [227]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.77 PriceRange <PricRg>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 227 to 227.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 227

```text
13.1.2.3.77  PriceRange <PricRg>
Presence: [0..1]
Definition: Indicates a search criterion used when looking to buy a bond within a particular price range.
PriceRange <PricRg> contains the following elements (see "AmountOrPercentageRange1" on
page 483 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Operation <Opr> [0..1] CodeSet 483
   Term <Term> [0..10]  483
     Operator <Oprtr> [1..1] CodeSet 484
     Value <Val> [1..1]  484
{Or       RateValue <RateVal> [1..1] Rate 484
Or}       AbsoluteValue <AbsVal> [1..1] Quantity 484
13.1.2.4  Warrant4
Definition: Financial instrument that gives the holder the right to purchase shares or bonds at a given
price within a specified time.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 227 March 2024
```

