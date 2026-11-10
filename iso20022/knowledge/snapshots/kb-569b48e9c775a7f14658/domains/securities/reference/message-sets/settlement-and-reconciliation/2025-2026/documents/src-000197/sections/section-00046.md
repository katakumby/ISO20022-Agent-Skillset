---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.9 SubAccountDetails <SubAcctDtls>", "2.4.9.5 BalanceForSubAccount <BalForSubAcct>", "2.4.9.5.18 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>", "2.4.9.5.18.15 AdditionalBalanceBreakdown <AddtlBalBrkdwn>"]
file_pages: [74]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.9.5.18.15 AdditionalBalanceBreakdown <AddtlBalBrkdwn>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 74 to 74.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 74

```text
Definition: Breakdown of the aggregate balance per meaningful sub-balances and availability.
Impacted by: C9 "AvailableWithNoStatusRule", C39 "SubBalanceAdditionalDetailsRule"
BalanceBreakdown <BalBrkdwn> contains the following elements (see "SubBalanceInformation20"
on page 1414 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SubBalanceType <SubBalTp> [1..1] ± 1415
   Quantity <Qty> [1..1] ± 1415
   SubBalanceAdditionalDetails <SubBalAddtlDtls> [0..1] Text 1415
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 1415
   AdditionalBalanceBreakdownDetails
<AddtlBalBrkdwnDtls>
[0..*] ± C19,
C40
1416
Constraints
• AvailableWithNoStatusRule
If Subbalance type is AvailableWithNoStatus, then QuantityAndAvailability cannot be used.
On Condition
    /SubBalanceType/Code is equal to value 'AvailableWithNoAdditionalStatus'
Following Must be True
    /Quantity/Quantity/QuantityAndAvailability Must be absent
• SubBalanceAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
used, them it must not contain information that can be provided in a structured field.
2.4.9.5.18.15  AdditionalBalanceBreakdown <AddtlBalBrkdwn>
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
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 74 March 2026
```

