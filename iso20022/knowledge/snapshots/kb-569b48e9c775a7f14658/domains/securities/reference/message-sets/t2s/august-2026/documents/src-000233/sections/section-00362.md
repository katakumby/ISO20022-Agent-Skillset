---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["19 camt.081.001.02 IntraBalanceMovementModificationReportV02", "19.4 Message Building Blocks", "19.4.4 ReportOrError <RptOrErr>", "19.4.4.1 Modifications <Mods>", "19.4.4.1.5 Modification <Mod>", "19.4.4.1.5.8 UnderlyingIntraBalance <UndrlygIntraBal>", "19.4.4.1.5.8.1 SettlementAmount <SttlmAmt>"]
file_pages: [469]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 19.4.4.1.5.8.1 SettlementAmount <SttlmAmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 469 to 469.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 469

```text
19.4.4.1.5.8.1  SettlementAmount <SttlmAmt>
Presence: [1..1]
Definition: Total amount of money to be settled.
SettlementAmount <SttlmAmt> contains one of the following elements (see "Amount2Choice" on
page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 2840
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 2841
19.4.4.1.5.8.2  SettlementDate <SttlmDt>
Presence: [1..1]
Definition: Date and time at which the amount of money is to be moved.
SettlementDate <SttlmDt> contains one of the following elements (see "DateAndDateTime2Choice"
on page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
19.4.4.1.5.8.3  BalanceFrom <BalFr>
Presence: [1..1]
Definition: Balance from which the amount of money is moved.
BalanceFrom <BalFr> contains the following CashSubBalanceTypeAndQuantityBreakdown3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  469
{Or     Code <Cd> [1..1] CodeSet 470
Or}     Proprietary <Prtry> [1..1] ± 470
   QuantityBreakdown <QtyBrkdwn> [0..*]  470
     LotNumber <LotNb> [0..1] ± 470
     LotAmount <LotAmt> [0..1] ± 471
     LotQuantity <LotQty> [0..1] ± 471
     CashSubBalanceType <CshSubBalTp> [0..1] ± 471
19.4.4.1.5.8.3.1  Type <Tp>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 469 August 2026
```

