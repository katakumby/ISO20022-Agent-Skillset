---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.4 Balance", "35.1.4.5 SubBalanceInformation20", "35.1.4.5.5 AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls>"]
file_pages: [1416]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.4.5.5 AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1416 to 1416.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1416

```text
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown57" on
page 1722 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 1722
   LotQuantity <LotQty> [0..1] ± 1723
   LotDateTime <LotDtTm> [0..1] ± 1723
   LotPrice <LotPric> [0..1] ± 1723
   TypeOfPrice <TpOfPric> [0..1] ± 1723
35.1.4.5.5  AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls>
Presence: [0..*]
Definition: Provides additional instrument sub-balance information on all or parts of the reported
financial instrument (unregistered, tax exempt, etc.).
Impacted by: C19 "EligibleForCollateralPurposesRule", C40 "SubBalanceAdditionalDetailsRule"
AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls> contains the following elements (see
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
35.1.4.6  SecuritiesBalanceType7Choice
Definition: Choice of format for the balance type.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1416 March 2026
```

