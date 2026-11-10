---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "3.4 Message Building Blocks", "3.4.8 BalanceForAccount <BalForAcct>", "3.4.8.17 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>"]
file_pages: [101]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.12"]
---

# 3.4.8.17 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 101 to 101.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 101

```text
Definition: Provides additional instrument sub-balance information on all or parts of the reported
financial instrument (unregistered, tax exempt, etc.).
Impacted by: C17 "EligibleForCollateralPurposesRule", C38 "SubBalanceAdditionalDetailsRule"
AdditionalBalanceBreakdown <AddtlBalBrkdwn> contains the following elements (see
"AdditionalBalanceInformation22" on page 1425 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SubBalanceType <SubBalTp> [1..1] ± 1425
   Quantity <Qty> [1..1] ± 1425
   SubBalanceAdditionalDetails <SubBalAddtlDtls> [0..1] Text 1426
Constraints
• EligibleForCollateralPurposesRule
If Subbalance type is EligibleForCollateralPurposes, then QuantityAndAvailability cannot be used.
On Condition
    /SubBalanceType/Code is equal to value 'EligibleForCollateralPurposes'
Following Must be True
    /Quantity/QuantityAndAvailability Must be absent
• SubBalanceAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
used, them it must not contain information that can be provided in a structured field.
3.4.8.17  BalanceAtSafekeepingPlace <BalAtSfkpgPlc>
Presence: [0..*]
Definition: Breakdown of positions per place of safekeeping (and optionally per place of listing).
Impacted by: C20 "HoldingAdditionalDetailsRule", C6 "AggregateBalanceGuideline"
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 101 March 2026
```

