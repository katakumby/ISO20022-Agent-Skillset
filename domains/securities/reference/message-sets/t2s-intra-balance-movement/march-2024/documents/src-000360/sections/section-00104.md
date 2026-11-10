---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02", "7.4 Message Building Blocks", "7.4.6 UnderlyingIntraBalance <UndrlygIntraBal>", "7.4.6.1 SettlementAmount <SttlmAmt>"]
file_pages: [125]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.074.001.02"]
---

# 7.4.6.1 SettlementAmount <SttlmAmt>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 125 to 125.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 125

```text
7.4.6.1  SettlementAmount <SttlmAmt>
Presence: [1..1]
Definition: Total amount of money to be settled.
SettlementAmount <SttlmAmt> contains one of the following elements (see "Amount2Choice" on
page 392 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 392
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C8 392
7.4.6.2  SettlementDate <SttlmDt>
Presence: [1..1]
Definition: Date and time at which the amount of money is to be moved.
SettlementDate <SttlmDt> contains one of the following elements (see "DateAndDateTime2Choice"
on page 398 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 398
Or}   DateTime <DtTm> [1..1] DateTime 398
7.4.6.3  BalanceFrom <BalFr>
Presence: [1..1]
Definition: Balance from which the amount of money is moved.
BalanceFrom <BalFr> contains the following CashSubBalanceTypeAndQuantityBreakdown3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  125
{Or     Code <Cd> [1..1] CodeSet 126
Or}     Proprietary <Prtry> [1..1] ± 126
   QuantityBreakdown <QtyBrkdwn> [0..*]  126
     LotNumber <LotNb> [0..1] ± 126
     LotAmount <LotAmt> [0..1] ± 127
     LotQuantity <LotQty> [0..1] ± 127
     CashSubBalanceType <CshSubBalTp> [0..1] ± 127
7.4.6.3.1  Type <Tp>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.074.001.02
IntraBalanceMovementCancellationRequestV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
125 March 2024
```

