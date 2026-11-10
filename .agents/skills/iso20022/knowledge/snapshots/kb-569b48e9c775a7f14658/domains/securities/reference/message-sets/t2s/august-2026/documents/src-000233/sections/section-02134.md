---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.16 Balance30", "82.1.5.16.3 SubAccountDetails <SubAcctDtls>", "82.1.5.16.3.4 BalanceForSubAccount <BalForSubAcct>", "82.1.5.16.3.4.19 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>"]
file_pages: [2895]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.16.3.4.19 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2895 to 2895.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2895

```text
Impacted by: C21 "EligibleForCollateralPurposesRule", C37 "SubBalanceAdditionalDetailsRule"
AdditionalBalanceBreakdown <AddtlBalBrkdwn> contains the following elements (see
"AdditionalBalanceBreakdown1" on page 2845 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SubBalanceType <SubBalTp> [1..1] ± 2846
   Quantity <Qty> [1..1] ± 2846
   SubBalanceAdditionalDetails <SubBalAddtlDtls> [0..1] Text 2846
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 2847
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
82.1.5.16.3.4.19  BalanceAtSafekeepingPlace <BalAtSfkpgPlc>
Presence: [0..*]
Definition: Breakdown of positions per place of safekeeping (and optionally per place of listing).
Impacted by: C23 "HoldingAdditionalDetailsRule", C8 "AggregateBalanceGuideline"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2895 August 2026
```

