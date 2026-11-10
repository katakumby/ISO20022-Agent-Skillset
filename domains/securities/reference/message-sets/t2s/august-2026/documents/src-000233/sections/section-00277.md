---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["16 camt.078.001.02 IntraBalanceMovementQueryV02", "16.4 Message Building Blocks", "16.4.2 QueryDefinition <QryDef>", "16.4.2.2 SearchCriteria <SchCrit>", "16.4.2.2.6 BalanceType <BalTp>", "16.4.2.2.6.1 BalanceFrom <BalFr>"]
file_pages: [364]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 16.4.2.2.6.1 BalanceFrom <BalFr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 364 to 364.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 364

```text
BalanceType <BalTp> contains the following IntraBalanceType3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BalanceFrom <BalFr> [0..1]  364
     Type <Tp> [1..1]  365
{Or       Code <Cd> [1..1] CodeSet 365
Or}       Proprietary <Prtry> [1..1] ± 365
     QuantityBreakdown <QtyBrkdwn> [0..*]  366
       LotNumber <LotNb> [0..1] ± 366
       LotAmount <LotAmt> [0..1] ± 366
       LotQuantity <LotQty> [0..1] ± 366
       CashSubBalanceType <CshSubBalTp> [0..1] ± 367
   BalanceTo <BalTo> [0..1]  367
     Type <Tp> [1..1]  367
{Or       Code <Cd> [1..1] CodeSet 368
Or}       Proprietary <Prtry> [1..1] ± 368
     QuantityBreakdown <QtyBrkdwn> [0..*]  368
       LotNumber <LotNb> [0..1] ± 368
       LotAmount <LotAmt> [0..1] ± 369
       LotQuantity <LotQty> [0..1] ± 369
       CashSubBalanceType <CshSubBalTp> [0..1] ± 369
Constraints
• BalanceFromToRule
The cash balance type of BalanceFrom must be different from the cash balance type of BalanceTo.
16.4.2.2.6.1  BalanceFrom <BalFr>
Presence: [0..1]
Definition: Balance from which the amount of money is moved.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities 364 August 2026
```

