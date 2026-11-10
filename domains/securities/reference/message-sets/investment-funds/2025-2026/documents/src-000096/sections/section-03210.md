---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.8 Charge", "66.1.8.2 CostsAndCharges2", "66.1.8.2.1 ExAnteReferenceDate <ExAnteRefDt>"]
file_pages: [4442]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.8.2.1 ExAnteReferenceDate <ExAnteRefDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4442 to 4442.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4442

```text
Constraints
• ExAnteReferenceDateGuideline
The ex-ante reference date should not be confused with the reporting date as specified in the
European MiFID Template (EMT) reference 00050.
• IndividualCostAndCharge1Guideline
If ExAnteReferenceDate is present, then all repetitions of IndividualCostOrCharge must specify Ex
Ante costs
66.1.8.2.1  ExAnteReferenceDate <ExAnteRefDt>
Presence: [0..1]
Definition: Reference date applicable to all ex ante cost and charge disclosures. When used in
reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference 07160.
Datatype: "ISODate" on page 5388
66.1.8.2.2  IndividualCostOrCharge <IndvCostOrChrg>
Presence: [1..*]
Definition: Individual cost or charge associated with the distribution of selling of the financial instrument.
This may be one-off or recurring. This may be ex ante (intended) or post ante (actual).
Impacted by: C14 "ExAnteOrExPost1Guideline", C15 "ExAnteOrExPost2Guideline", C31
"SignAmount1Rule", C32 "SignAmount2Rule"
IndividualCostOrCharge <IndvCostOrChrg> contains the following IndividualCostOrCharge2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CostType <CostTp> [1..1]  4443
{Or     Code <Cd> [1..1] CodeSet 4443
Or}     Proprietary <Prtry> [1..1] ± 4448
   ExAnteOrExPost <ExAnteOrExPst> [1..1] CodeSet 4448
   Amount <Amt> [0..1] Amount C1 4449
   Sign <Sgn> [0..1] Indicator 4449
   Rate <Rate> [0..1] Rate 4449
   ReferencePeriod <RefPrd> [0..1]  4449
     StartDate <StartDt> [1..1] Date 4450
     EndDate <EndDt> [1..1] Date 4450
   AdditionalInformation <AddtlInf> [0..1] ± 4450
Constraints
• ExAnteOrExPost1Guideline
If ExAnteOrExPost contains ANTE then CostType must be an ex ante cost or charge.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4442 May 2026
```

