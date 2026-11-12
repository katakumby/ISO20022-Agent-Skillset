---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["9 camt.078.001.02 IntraBalanceMovementQueryV02", "9.4 Message Building Blocks", "9.4.2 QueryDefinition <QryDef>", "9.4.2.2 SearchCriteria <SchCrit>", "9.4.2.2.6 BalanceType <BalTp>", "9.4.2.2.6.1 BalanceFrom <BalFr>", "9.4.2.2.6.1.2 QuantityBreakdown <QtyBrkdwn>", "9.4.2.2.6.1.2.4 CashSubBalanceType <CshSubBalTp>"]
file_pages: [176]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 9.4.2.2.6.1.2.4 CashSubBalanceType <CshSubBalTp>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 176 to 176.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 176

```text
LotQuantity <LotQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 406 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 407
Or   FaceAmount <FaceAmt> [1..1] Amount 407
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 407
9.4.2.2.6.1.2.4  CashSubBalanceType <CshSubBalTp>
Presence: [0..1]
Definition: Specifies the securities sub balance type indicator (example restriction type for a market
infrastructure).
CashSubBalanceType <CshSubBalTp> contains the following elements (see
"GenericIdentification30" on page 409 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 409
   Issuer <Issr> [1..1] Text 409
   SchemeName <SchmeNm> [0..1] Text 409
9.4.2.2.6.2  BalanceTo <BalTo>
Presence: [0..1]
Definition: Balance to which the amount of money is moved.
BalanceTo <BalTo> contains the following CashSubBalanceTypeAndQuantityBreakdown3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  176
{Or     Code <Cd> [1..1] CodeSet 177
Or}     Proprietary <Prtry> [1..1] ± 177
   QuantityBreakdown <QtyBrkdwn> [0..*]  177
     LotNumber <LotNb> [0..1] ± 177
     LotAmount <LotAmt> [0..1] ± 178
     LotQuantity <LotQty> [0..1] ± 178
     CashSubBalanceType <CshSubBalTp> [0..1] ± 178
9.4.2.2.6.2.1  Type <Tp>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
176 March 2024
```

