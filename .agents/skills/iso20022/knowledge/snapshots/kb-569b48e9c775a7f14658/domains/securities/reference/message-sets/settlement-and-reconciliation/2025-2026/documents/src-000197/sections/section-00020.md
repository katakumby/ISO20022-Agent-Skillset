---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.8 BalanceForAccount <BalForAcct>", "2.4.8.17 AdditionalBalanceBreakdown <AddtlBalBrkdwn>"]
file_pages: [43]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.8.17 AdditionalBalanceBreakdown <AddtlBalBrkdwn>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 43 to 43.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 43

```text
Following Must be True
    /Quantity/Quantity/QuantityAndAvailability Must be absent
• SubBalanceAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
used, them it must not contain information that can be provided in a structured field.
2.4.8.17  AdditionalBalanceBreakdown <AddtlBalBrkdwn>
Presence: [0..*]
Definition: Provides additional instrument sub-balance information on all or parts of the reported
financial instrument (unregistered, tax exempt, etc.).
Impacted by: C19 "EligibleForCollateralPurposesRule", C40 "SubBalanceAdditionalDetailsRule"
AdditionalBalanceBreakdown <AddtlBalBrkdwn> contains the following elements (see
"AdditionalBalanceInformation20" on page 1408 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SubBalanceType <SubBalTp> [1..1] ± 1409
   Quantity <Qty> [1..1] ± 1409
   SubBalanceAdditionalDetails <SubBalAddtlDtls> [0..1] Text 1409
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 1409
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
2.4.8.18  BalanceAtSafekeepingPlace <BalAtSfkpgPlc>
Presence: [0..*]
Definition: Breakdown of positions per place of safekeeping (and optionally per place of listing).
Impacted by: C22 "HoldingAdditionalDetailsRule", C7 "AggregateBalanceGuideline"
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 43 March 2026
```

