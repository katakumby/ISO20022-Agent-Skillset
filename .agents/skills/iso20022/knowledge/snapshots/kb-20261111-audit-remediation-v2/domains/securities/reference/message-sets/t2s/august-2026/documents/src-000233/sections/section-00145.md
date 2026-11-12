---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["11 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02", "11.4 Message Building Blocks", "11.4.8 UnderlyingIntraBalance <UndrlygIntraBal>", "11.4.8.4 BalanceTo <BalTo>"]
file_pages: [194]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.073.001.02"]
---

# 11.4.8.4 BalanceTo <BalTo>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 194 to 194.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 194

```text
11.4.8.4  BalanceTo <BalTo>
Presence: [1..1]
Definition: Balance to which the amount of money is moved.
BalanceTo <BalTo> contains the following CashSubBalanceTypeAndQuantityBreakdown3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  194
{Or     Code <Cd> [1..1] CodeSet 194
Or}     Proprietary <Prtry> [1..1] ± 194
   QuantityBreakdown <QtyBrkdwn> [0..*]  195
     LotNumber <LotNb> [0..1] ± 195
     LotAmount <LotAmt> [0..1] ± 195
     LotQuantity <LotQty> [0..1] ± 196
     CashSubBalanceType <CshSubBalTp> [0..1] ± 196
11.4.8.4.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the securities sub balance type indicator (example restriction type for a market
infrastructure).
Type <Tp> contains one of the following CashBalanceType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 194
Or}   Proprietary <Prtry> [1..1] ± 194
11.4.8.4.1.1  Code <Cd>
Presence: [1..1]
Definition: Cash balance expressed in a coded form.
Datatype: "ExternalBalanceType1Code" on page 3240
11.4.8.4.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Cash balance expressed in a proprietary form.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities 194 August 2026
```

