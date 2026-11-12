---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["13 camt.075.001.02 IntraBalanceMovementCancellationRequestStatusAdviceV02", "13.4 Message Building Blocks", "13.4.8 UnderlyingIntraBalance <UndrlygIntraBal>", "13.4.8.1 SettlementAmount <SttlmAmt>"]
file_pages: [226]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.075.001.02"]
---

# 13.4.8.1 SettlementAmount <SttlmAmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 226 to 226.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 226

```text
13.4.8.1  SettlementAmount <SttlmAmt>
Presence: [1..1]
Definition: Total amount of money to be settled.
SettlementAmount <SttlmAmt> contains one of the following elements (see "Amount2Choice" on
page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 2840
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 2841
13.4.8.2  SettlementDate <SttlmDt>
Presence: [1..1]
Definition: Date and time at which the amount of money is to be moved.
SettlementDate <SttlmDt> contains one of the following elements (see "DateAndDateTime2Choice"
on page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
13.4.8.3  BalanceFrom <BalFr>
Presence: [1..1]
Definition: Balance from which the amount of money is moved.
BalanceFrom <BalFr> contains the following CashSubBalanceTypeAndQuantityBreakdown3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  226
{Or     Code <Cd> [1..1] CodeSet 227
Or}     Proprietary <Prtry> [1..1] ± 227
   QuantityBreakdown <QtyBrkdwn> [0..*]  227
     LotNumber <LotNb> [0..1] ± 227
     LotAmount <LotAmt> [0..1] ± 228
     LotQuantity <LotQty> [0..1] ± 228
     CashSubBalanceType <CshSubBalTp> [0..1] ± 228
13.4.8.3.1  Type <Tp>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.075.001.02
IntraBalanceMovementCancellationRequestStatusA
dviceV02
Target2-Securities 226 August 2026
```

