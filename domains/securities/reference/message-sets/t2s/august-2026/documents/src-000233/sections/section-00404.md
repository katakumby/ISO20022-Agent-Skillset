---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["21 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "21.4 Message Building Blocks", "21.4.4 ReportOrError <RptOrErr>", "21.4.4.1 Cancellations <Cxls>", "21.4.4.1.5 Cancellation <Cxl>", "21.4.4.1.5.8 UnderlyingIntraBalance <UndrlygIntraBal>", "21.4.4.1.5.8.4 BalanceTo <BalTo>"]
file_pages: [517]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 21.4.4.1.5.8.4 BalanceTo <BalTo>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 517 to 517.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 517

```text
21.4.4.1.5.8.4  BalanceTo <BalTo>
Presence: [1..1]
Definition: Balance to which the amount of money is moved.
BalanceTo <BalTo> contains the following CashSubBalanceTypeAndQuantityBreakdown3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  517
{Or     Code <Cd> [1..1] CodeSet 517
Or}     Proprietary <Prtry> [1..1] ± 517
   QuantityBreakdown <QtyBrkdwn> [0..*]  518
     LotNumber <LotNb> [0..1] ± 518
     LotAmount <LotAmt> [0..1] ± 518
     LotQuantity <LotQty> [0..1] ± 519
     CashSubBalanceType <CshSubBalTp> [0..1] ± 519
21.4.4.1.5.8.4.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the securities sub balance type indicator (example restriction type for a market
infrastructure).
Type <Tp> contains one of the following CashBalanceType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 517
Or}   Proprietary <Prtry> [1..1] ± 517
21.4.4.1.5.8.4.1.1  Code <Cd>
Presence: [1..1]
Definition: Cash balance expressed in a coded form.
Datatype: "ExternalBalanceType1Code" on page 3240
21.4.4.1.5.8.4.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Cash balance expressed in a proprietary form.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 517 August 2026
```

