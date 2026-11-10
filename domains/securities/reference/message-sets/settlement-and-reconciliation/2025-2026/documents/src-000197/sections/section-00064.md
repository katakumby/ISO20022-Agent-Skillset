---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "3.4 Message Building Blocks", "3.4.8 BalanceForAccount <BalForAcct>", "3.4.8.15 BalanceBreakdown <BalBrkdwn>"]
file_pages: [100]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.12"]
---

# 3.4.8.15 BalanceBreakdown <BalBrkdwn>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 100 to 100.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 100

```text
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown58" on
page 1728 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 1728
   LotQuantity <LotQty> [0..1] ± 1728
   LotDateTime <LotDtTm> [0..1] ± 1728
   LotPrice <LotPric> [0..1] ± 1729
   TypeOfPrice <TpOfPric> [0..1] ± 1729
   AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [0..1] ± 1729
   InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± 1729
   AlternateReportingCurrencyAmounts
<AltrnRptgCcyAmts>
[0..1] ± 1730
3.4.8.15  BalanceBreakdown <BalBrkdwn>
Presence: [0..*]
Definition: Breakdown of the aggregate balance per meaningful sub-balances and availability.
Impacted by: C8 "AvailableWithNoStatusRule", C37 "SubBalanceAdditionalDetailsRule"
BalanceBreakdown <BalBrkdwn> contains the following elements (see "SubBalanceInformation22"
on page 1429 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SubBalanceType <SubBalTp> [1..1] ± 1429
   Quantity <Qty> [1..1] ± 1430
   SubBalanceAdditionalDetails <SubBalAddtlDtls> [0..1] Text 1430
   AdditionalBalanceBreakdownDetails
<AddtlBalBrkdwnDtls>
[0..*] ± C17,
C38
1430
Constraints
• AvailableWithNoStatusRule
If Subbalance type is AvailableWithNoStatus, then QuantityAndAvailability cannot be used.
On Condition
    /SubBalanceType/Code is equal to value 'AvailableWithNoAdditionalStatus'
Following Must be True
    /Quantity/QuantityAndAvailability Must be absent
• SubBalanceAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
used, them it must not contain information that can be provided in a structured field.
3.4.8.16  AdditionalBalanceBreakdown <AddtlBalBrkdwn>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 100 March 2026
```

