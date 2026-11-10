---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.16 Balance30", "82.1.5.16.4 AccountBaseCurrencyTotalAmounts <AcctBaseCcyTtlAmts>"]
file_pages: [2897]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.16.4 AccountBaseCurrencyTotalAmounts <AcctBaseCcyTtlAmts>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2897 to 2897.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2897

```text
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C6 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 3011 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 3011
   Envelope <Envlp> [1..1] (External Schema) 3012
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
82.1.5.16.4  AccountBaseCurrencyTotalAmounts <AcctBaseCcyTtlAmts>
Presence: [0..1]
Definition: Total valuation amounts provided in the base currency of the account.
Impacted by: C40 "TotalEligibleCollateralValueRule"
AccountBaseCurrencyTotalAmounts <AcctBaseCcyTtlAmts> contains the following
TotalValueInPageAndStatement1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalHoldingsValueOfPage <TtlHldgsValOfPg> [0..1] ± 2897
   TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> [1..1] ± 2898
   TotalBookValueOfStatement <TtlBookValOfStmt> [0..1] ± 2898
   TotalEligibleCollateralValue <TtlElgblCollVal> [0..1] ± 2898
Constraints
• TotalEligibleCollateralValueRule
Total eligible collateral value is only to be used in (I)CSD-participant communication or if bilaterally
agreed between the sender and receiver.
82.1.5.16.4.1  TotalHoldingsValueOfPage <TtlHldgsValOfPg>
Presence: [0..1]
Definition: Total value of positions reported in this message.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2897 August 2026
```

