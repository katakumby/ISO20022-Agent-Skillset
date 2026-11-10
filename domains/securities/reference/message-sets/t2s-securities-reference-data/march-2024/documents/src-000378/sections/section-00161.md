---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.68 MinimumQuantity <MinQty>"]
file_pages: [225]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.68 MinimumQuantity <MinQty>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 225 to 225.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 225

```text
MinimumIncrement <MinIncrmt> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 476
Or   FaceAmount <FaceAmt> [1..1] Amount 476
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 476
13.1.2.3.68  MinimumQuantity <MinQty>
Presence: [0..1]
Definition: Indicates the minimum tradable quantity of a security.
MinimumQuantity <MinQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 476
Or   FaceAmount <FaceAmt> [1..1] Amount 476
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 476
13.1.2.3.69  Production <Pdctn>
Presence: [0..1]
Definition: Indicates a search criterion used when looking to buy a bond, particularly an mortgage back
security (MBS), issued in a particular year.
Datatype: "Max35Text" on page 534
13.1.2.3.70  RestrictedIndicator <RstrctdInd>
Presence: [0..1]
Definition: Identifies if the securities is restricted or not (as per Rule 144).
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.2.3.71  PriceFrequency <PricFrqcy>
Presence: [0..1]
Definition: Indicates the frequency at which the bond is re-rated and therefore re-priced (bond attribute,
particularly of floating rate and index linked instruments).
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 225 March 2024
```

