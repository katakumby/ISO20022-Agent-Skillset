---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.4 Balance", "35.1.4.17 SubBalanceInformation22", "35.1.4.17.2 Quantity <Qty>"]
file_pages: [1430]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.4.17.2 Quantity <Qty>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1430 to 1430.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1430

```text
SubBalanceType <SubBalTp> contains one of the following elements (see
"SubBalanceType11Choice" on page 1411 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1412
Or}   Proprietary <Prtry> [1..1] ± 1413
35.1.4.17.2  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Quantity <Qty> contains one of the following elements (see "SubBalanceQuantity8Choice" on
page 1730 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C12 1730
Or   Proprietary <Prtry> [1..1] ± 1731
Or}   QuantityAndAvailability <QtyAndAvlbty> [1..1] ± 1731
35.1.4.17.3  SubBalanceAdditionalDetails <SubBalAddtlDtls>
Presence: [0..1]
Definition: Provides additional subbalance information.
Datatype: "Max140Text" on page 2191
35.1.4.17.4  AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls>
Presence: [0..*]
Definition: Provides additional instrument sub-balance information on all or parts of the reported
financial instrument (unregistered, tax exempt, etc.).
Impacted by: C17 "EligibleForCollateralPurposesRule", C38 "SubBalanceAdditionalDetailsRule"
AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls> contains the following elements (see
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1430 March 2026
```

