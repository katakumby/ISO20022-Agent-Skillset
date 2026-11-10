---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["9 camt.078.001.02 IntraBalanceMovementQueryV02", "9.4 Message Building Blocks", "9.4.2 QueryDefinition <QryDef>", "9.4.2.2 SearchCriteria <SchCrit>", "9.4.2.2.6 BalanceType <BalTp>", "9.4.2.2.6.1 BalanceFrom <BalFr>"]
file_pages: [173]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 9.4.2.2.6.1 BalanceFrom <BalFr>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 173 to 173.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 173

```text
BalanceType <BalTp> contains the following IntraBalanceType3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BalanceFrom <BalFr> [0..1]  173
     Type <Tp> [1..1]  174
{Or       Code <Cd> [1..1] CodeSet 174
Or}       Proprietary <Prtry> [1..1] ± 174
     QuantityBreakdown <QtyBrkdwn> [0..*]  175
       LotNumber <LotNb> [0..1] ± 175
       LotAmount <LotAmt> [0..1] ± 175
       LotQuantity <LotQty> [0..1] ± 175
       CashSubBalanceType <CshSubBalTp> [0..1] ± 176
   BalanceTo <BalTo> [0..1]  176
     Type <Tp> [1..1]  176
{Or       Code <Cd> [1..1] CodeSet 177
Or}       Proprietary <Prtry> [1..1] ± 177
     QuantityBreakdown <QtyBrkdwn> [0..*]  177
       LotNumber <LotNb> [0..1] ± 177
       LotAmount <LotAmt> [0..1] ± 178
       LotQuantity <LotQty> [0..1] ± 178
       CashSubBalanceType <CshSubBalTp> [0..1] ± 178
Constraints
• BalanceFromToRule
The cash balance type of BalanceFrom must be different from the cash balance type of BalanceTo.
9.4.2.2.6.1  BalanceFrom <BalFr>
Presence: [0..1]
Definition: Balance from which the amount of money is moved.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
173 March 2024
```

