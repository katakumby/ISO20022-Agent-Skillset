---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["22 camt.084.001.02 IntraBalanceMovementPostingReportV02", "22.4 Message Building Blocks", "22.4.7 SubBalance <SubBal>", "22.4.7.2 Movement <Mvmnt>", "22.4.7.2.5 PoolIdentification <PoolId>"]
file_pages: [540]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 22.4.7.2.5 PoolIdentification <PoolId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 540 to 540.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 540

```text
Datatype: "Max35Text" on page 3328
22.4.7.2.5  PoolIdentification <PoolId>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 3328
22.4.7.2.6  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [0..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 3328
22.4.7.2.7  BalanceTo <BalTo>
Presence: [1..1]
Definition: Balance to which the amount of money is moved.
BalanceTo <BalTo> contains the following CashSubBalanceTypeAndQuantityBreakdown3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  540
{Or     Code <Cd> [1..1] CodeSet 541
Or}     Proprietary <Prtry> [1..1] ± 541
   QuantityBreakdown <QtyBrkdwn> [0..*]  541
     LotNumber <LotNb> [0..1] ± 541
     LotAmount <LotAmt> [0..1] ± 542
     LotQuantity <LotQty> [0..1] ± 542
     CashSubBalanceType <CshSubBalTp> [0..1] ± 542
22.4.7.2.7.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the securities sub balance type indicator (example restriction type for a market
infrastructure).
Type <Tp> contains one of the following CashBalanceType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 541
Or}   Proprietary <Prtry> [1..1] ± 541
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities 540 August 2026
```

