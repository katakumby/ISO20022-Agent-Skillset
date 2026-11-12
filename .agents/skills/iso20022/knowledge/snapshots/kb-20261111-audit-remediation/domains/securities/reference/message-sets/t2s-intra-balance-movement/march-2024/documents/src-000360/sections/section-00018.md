---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 camt.066.001.02 IntraBalanceMovementInstructionV02", "2.4 Message Building Blocks", "2.4.8 IntraBalance <IntraBal>", "2.4.8.4 BalanceTo <BalTo>"]
file_pages: [27]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.066.001.02"]
---

# 2.4.8.4 BalanceTo <BalTo>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 27 to 27.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 27

```text
2.4.8.4  BalanceTo <BalTo>
Presence: [1..1]
Definition: Balance to which the amount of money is moved.
BalanceTo <BalTo> contains the following CashSubBalanceTypeAndQuantityBreakdown3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  27
{Or     Code <Cd> [1..1] CodeSet 27
Or}     Proprietary <Prtry> [1..1] ± 27
   QuantityBreakdown <QtyBrkdwn> [0..*]  28
     LotNumber <LotNb> [0..1] ± 28
     LotAmount <LotAmt> [0..1] ± 28
     LotQuantity <LotQty> [0..1] ± 29
     CashSubBalanceType <CshSubBalTp> [0..1] ± 29
2.4.8.4.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the securities sub balance type indicator (example restriction type for a market
infrastructure).
Type <Tp> contains one of the following CashBalanceType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 27
Or}   Proprietary <Prtry> [1..1] ± 27
2.4.8.4.1.1  Code <Cd>
Presence: [1..1]
Definition: Cash balance expressed in a coded form.
Datatype: "ExternalBalanceType1Code" on page 480
2.4.8.4.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Cash balance expressed in a proprietary form.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.066.001.02
IntraBalanceMovementInstructionV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
27 March 2024
```

