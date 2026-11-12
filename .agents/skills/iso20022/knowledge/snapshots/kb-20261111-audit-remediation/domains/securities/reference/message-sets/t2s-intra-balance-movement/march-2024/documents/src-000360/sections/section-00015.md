---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 camt.066.001.02 IntraBalanceMovementInstructionV02", "2.4 Message Building Blocks", "2.4.8 IntraBalance <IntraBal>", "2.4.8.1 SettlementAmount <SttlmAmt>"]
file_pages: [24]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.066.001.02"]
---

# 2.4.8.1 SettlementAmount <SttlmAmt>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 24 to 24.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 24

```text
2.4.8.1  SettlementAmount <SttlmAmt>
Presence: [1..1]
Definition: Total amount of money to be settled.
SettlementAmount <SttlmAmt> contains one of the following elements (see "Amount2Choice" on
page 392 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 392
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C8 392
2.4.8.2  SettlementDate <SttlmDt>
Presence: [1..1]
Definition: Date and time at which the amount of money is to be moved.
SettlementDate <SttlmDt> contains one of the following elements (see "DateAndDateTime2Choice"
on page 398 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 398
Or}   DateTime <DtTm> [1..1] DateTime 398
2.4.8.3  BalanceFrom <BalFr>
Presence: [1..1]
Definition: Balance from which the amount of money is moved.
BalanceFrom <BalFr> contains the following CashSubBalanceTypeAndQuantityBreakdown3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  24
{Or     Code <Cd> [1..1] CodeSet 25
Or}     Proprietary <Prtry> [1..1] ± 25
   QuantityBreakdown <QtyBrkdwn> [0..*]  25
     LotNumber <LotNb> [0..1] ± 25
     LotAmount <LotAmt> [0..1] ± 26
     LotQuantity <LotQty> [0..1] ± 26
     CashSubBalanceType <CshSubBalTp> [0..1] ± 26
2.4.8.3.1  Type <Tp>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.066.001.02
IntraBalanceMovementInstructionV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
24 March 2024
```

