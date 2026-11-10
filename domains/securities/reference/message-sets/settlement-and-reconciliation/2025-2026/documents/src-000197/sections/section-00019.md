---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.8 BalanceForAccount <BalForAcct>", "2.4.8.15 QuantityBreakdown <QtyBrkdwn>"]
file_pages: [42]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.8.15 QuantityBreakdown <QtyBrkdwn>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 42 to 42.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 42

```text
Constraints
• EligibleCollateralValueRule
EligibleCollateralValue is only to be used in (I)CSD-participant communication or if bilaterally agreed
between the sender and receiver.
2.4.8.15  QuantityBreakdown <QtyBrkdwn>
Presence: [0..*]
Definition: Breakdown of the aggregate quantity reported into significant lots, for example, tax lots.
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
2.4.8.16  BalanceBreakdown <BalBrkdwn>
Presence: [0..*]
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
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 42 March 2026
```

