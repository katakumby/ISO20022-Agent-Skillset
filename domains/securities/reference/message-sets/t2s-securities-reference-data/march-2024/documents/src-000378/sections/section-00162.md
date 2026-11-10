---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.72 Sector <Sctr>"]
file_pages: [226]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.72 Sector <Sctr>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 226 to 226.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 226

```text
PriceFrequency <PricFrqcy> contains one of the following elements (see "Frequency35Choice" on
page 477 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 477
Or}   Proprietary <Prtry> [1..1] ± 477
13.1.2.3.72  Sector <Sctr>
Presence: [0..1]
Definition: Indicates the market sector the security is classified as for example pharmaceuticals,
automobile, housing, etc.
Datatype: "Max35Text" on page 534
13.1.2.3.73  SubstitutionFrequency <SbstitnFrqcy>
Presence: [0..1]
Definition: Indicates the maximum number of times collateral can be substituted.
SubstitutionFrequency <SbstitnFrqcy> contains one of the following elements (see
"Frequency35Choice" on page 477 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 477
Or}   Proprietary <Prtry> [1..1] ± 477
13.1.2.3.74  SubstitutionLeft <SbstitnLft>
Presence: [0..1]
Definition: Number of remaining times the collateral can be substitute.
Datatype: "Number" on page 532
13.1.2.3.75  WholePoolIndicator <WhlPoolInd>
Presence: [0..1]
Definition: Indicates a search criterion when looking to buy a mortgaged backed security that either is
[yes] or is not [no] an entire pool.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.2.3.76  PriceSource <PricSrc>
Presence: [0..1]
Definition: Identifies the Benchmark source price (eg. BB Generic, BB Fairvalue, Brokertec.).
Datatype: "Max35Text" on page 534
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 226 March 2024
```

