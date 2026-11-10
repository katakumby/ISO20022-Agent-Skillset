---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.14 Balance30", "7.1.5.14.4 AccountBaseCurrencyTotalAmounts <AcctBaseCcyTtlAmts>"]
file_pages: [305]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.14.4 AccountBaseCurrencyTotalAmounts <AcctBaseCcyTtlAmts>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 305 to 305.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 305

```text
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C12 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 375 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 375
   Envelope <Envlp> [1..1] (External Schema) 376
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
7.1.5.14.4  AccountBaseCurrencyTotalAmounts <AcctBaseCcyTtlAmts>
Presence: [0..1]
Definition: Total valuation amounts provided in the base currency of the account.
Impacted by: C40 "TotalEligibleCollateralValueRule"
AccountBaseCurrencyTotalAmounts <AcctBaseCcyTtlAmts> contains the following
TotalValueInPageAndStatement1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalHoldingsValueOfPage <TtlHldgsValOfPg> [0..1] ± 305
   TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> [1..1] ± 306
   TotalBookValueOfStatement <TtlBookValOfStmt> [0..1] ± 306
   TotalEligibleCollateralValue <TtlElgblCollVal> [0..1] ± 306
Constraints
• TotalEligibleCollateralValueRule
Total eligible collateral value is only to be used in (I)CSD-participant communication or if bilaterally
agreed between the sender and receiver.
7.1.5.14.4.1  TotalHoldingsValueOfPage <TtlHldgsValOfPg>
Presence: [0..1]
Definition: Total value of positions reported in this message.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 305 March 2026
```

