---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.4 Balance", "35.1.4.14 AdditionalBalanceInformation22"]
file_pages: [1425]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.4.14 AdditionalBalanceInformation22

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1425 to 1425.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1425

```text
Quantity <Qty> contains one of the following elements (see "BalanceQuantity14Choice" on page 1735
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C12 1735
Or}   Proprietary <Prtry> [1..1] ± 1736
35.1.4.14  AdditionalBalanceInformation22
Definition: Sub-balances providing additional information on a specific position but that is not to be
accounted for in the building of the aggregate balance, for example, registered.
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
35.1.4.14.1  SubBalanceType <SubBalTp>
Presence: [1..1]
Definition: Reason for the sub-balance.
SubBalanceType <SubBalTp> contains one of the following elements (see
"SubBalanceType12Choice" on page 1418 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1418
Or}   Proprietary <Prtry> [1..1] ± 1419
35.1.4.14.2  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1425 March 2026
```

