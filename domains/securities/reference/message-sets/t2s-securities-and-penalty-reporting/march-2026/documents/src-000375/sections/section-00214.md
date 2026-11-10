---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.14 Balance30", "7.1.5.14.2 BalanceForAccount <BalForAcct>", "7.1.5.14.2.19 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>"]
file_pages: [287]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.14.2.19 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 287 to 287.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 287

```text
Impacted by: C21 "EligibleForCollateralPurposesRule", C37 "SubBalanceAdditionalDetailsRule"
AdditionalBalanceBreakdown <AddtlBalBrkdwn> contains the following elements (see
"AdditionalBalanceBreakdown1" on page 256 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SubBalanceType <SubBalTp> [1..1] ± 257
   Quantity <Qty> [1..1] ± 257
   SubBalanceAdditionalDetails <SubBalAddtlDtls> [0..1] Text 257
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 258
Constraints
• EligibleForCollateralPurposesRule
If Subbalance type is EligibleForCollateralPurposes, then QuantityAndAvailability cannot be used.
On Condition
    /SubBalanceType/Code is equal to value 'EligibleForCollateralPurposes'
Following Must be True
    /Quantity/Quantity/QuantityAndAvailability Must be absent
• SubBalanceAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
used, them it must not contain information that can be provided in a structured field.
7.1.5.14.2.19  BalanceAtSafekeepingPlace <BalAtSfkpgPlc>
Presence: [0..*]
Definition: Breakdown of positions per place of safekeeping (and optionally per place of listing).
Impacted by: C23 "HoldingAdditionalDetailsRule", C8 "AggregateBalanceGuideline"
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 287 March 2026
```

