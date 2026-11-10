---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.2.1.3 Debt <Debt>", "28.4.2.2.1.3.72 Sector <Sctr>"]
file_pages: [1625]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.1.3.72 Sector <Sctr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1625 to 1625.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1625

```text
PriceFrequency <PricFrqcy> contains one of the following elements (see "Frequency35Choice" on
page 2960 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2960
Or}   Proprietary <Prtry> [1..1] ± 2960
28.4.2.2.1.3.72  Sector <Sctr>
Presence: [0..1]
Definition: Indicates the market sector the security is classified as for example pharmaceuticals,
automobile, housing, etc.
Datatype: "Max35Text" on page 3328
28.4.2.2.1.3.73  SubstitutionFrequency <SbstitnFrqcy>
Presence: [0..1]
Definition: Indicates the maximum number of times collateral can be substituted.
SubstitutionFrequency <SbstitnFrqcy> contains one of the following elements (see
"Frequency35Choice" on page 2960 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2960
Or}   Proprietary <Prtry> [1..1] ± 2960
28.4.2.2.1.3.74  SubstitutionLeft <SbstitnLft>
Presence: [0..1]
Definition: Number of remaining times the collateral can be substitute.
Datatype: "Number" on page 3324
28.4.2.2.1.3.75  WholePoolIndicator <WhlPoolInd>
Presence: [0..1]
Definition: Indicates a search criterion when looking to buy a mortgaged backed security that either is
[yes] or is not [no] an entire pool.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
28.4.2.2.1.3.76  PriceSource <PricSrc>
Presence: [0..1]
Definition: Identifies the Benchmark source price (eg. BB Generic, BB Fairvalue, Brokertec.).
Datatype: "Max35Text" on page 3328
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1625 August 2026
```

