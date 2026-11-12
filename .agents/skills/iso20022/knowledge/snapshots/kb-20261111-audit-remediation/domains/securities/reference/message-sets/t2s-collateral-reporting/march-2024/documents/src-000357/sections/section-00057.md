---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.7 Miscellaneous", "4.1.7.3 YieldedOrValueType1Choice", "4.1.7.3.1 Yielded <Yldd>"]
file_pages: [61]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.7.3.1 Yielded <Yldd>

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 61 to 61.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 61

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Yielded <Yldd> [1..1] Indicator 61
Or}   ValueType <ValTp> [1..1] CodeSet 61
4.1.7.3.1  Yielded <Yldd>
Presence: [1..1]
Definition: Indicates whether the price is expressed as a yield.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 81):
• Meaning When True: Yes
• Meaning When False: No
4.1.7.3.2  ValueType <ValTp>
Presence: [1..1]
Definition: Type of value in which the price is expressed.
Datatype: "PriceValueType1Code" on page 77
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
4.1.7.4  SupplementaryData1
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 61
   Envelope <Envlp> [1..1] (External Schema) 62
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
4.1.7.4.1  PlaceAndName <PlcAndNm>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
61 March 2024
```

