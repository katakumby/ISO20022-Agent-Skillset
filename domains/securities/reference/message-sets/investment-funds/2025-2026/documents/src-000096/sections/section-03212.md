---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.8 Charge", "66.1.8.2 CostsAndCharges2", "66.1.8.2.2 IndividualCostOrCharge <IndvCostOrChrg>", "66.1.8.2.2.1 CostType <CostTp>", "66.1.8.2.2.1.2 Proprietary <Prtry>"]
file_pages: [4448]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.8.2.2.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4448 to 4448.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4448

```text
CodeName Name Definition
- 0 at maturity
Then maximum exit cost: 4%.
Typical cost : 0
OTES OneOffTypicalExitCostsStructured One-off typical exit cost linked to the
recommended holding period (RHP) for
a structured product. When used in
reference to MiFID, this is in the scope of
the European MiFID Template (EMT)
reference 07080 and may be specified
as an actual amount or a percentage of
the reference value, EMT reference
07150 or 07155.
OCAS OngoingCostsAccumulatedStructured Sum of daily recurring product costs
accumulated during the year until the ex
post reference date. This is typically
specified as an actual amount. When
used in reference to MiFID, this is in the
scope of the European MiFID Template
(EMT) reference 08040.
RPSS ReferencePrice Reference Price. When used in
reference to MiFID, this is in the scope of
the European MiFID Template (EMT)
reference 07150 and 08110 and is the
instrument price to which a unit
disclosed ex-post cost is based and to
which a percentage disclosed cost
should be multiplied in order to retrieve
the unit cost.
TRS1 TransactionCost Cost associated with the transaction.
When used in reference to MiFID, this is
in the scope of the European MiFID
Template (EMT) reference 07130 and
08070 and this is a percentage of the
NAV of the financial instrument
expressed in annualised terms (rate of
cost deduction to be applied).
66.1.8.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Cost or charge expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.8.2.2.2  ExAnteOrExPost <ExAnteOrExPst>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4448 May 2026
```

