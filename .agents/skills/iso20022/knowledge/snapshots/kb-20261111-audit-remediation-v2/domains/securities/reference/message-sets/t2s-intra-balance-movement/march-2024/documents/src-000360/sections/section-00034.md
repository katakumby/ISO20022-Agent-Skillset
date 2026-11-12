---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02", "3.4 Message Building Blocks", "3.4.8 UnderlyingIntraBalance <UndrlygIntraBal>", "3.4.8.3 BalanceFrom <BalFr>", "3.4.8.3.2 QuantityBreakdown <QtyBrkdwn>", "3.4.8.3.2.2 LotAmount <LotAmt>"]
file_pages: [45]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.067.001.02"]
---

# 3.4.8.3.2.2 LotAmount <LotAmt>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 45 to 45.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 45

```text
LotNumber <LotNb> contains the following elements (see "GenericIdentification37" on page 408 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 408
   Issuer <Issr> [0..1] Text 408
3.4.8.3.2.2  LotAmount <LotAmt>
Presence: [0..1]
Definition: Amount of money that is part of the lot described.
LotAmount <LotAmt> contains the following elements (see "AmountAndDirection5" on page 393 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C8 393
   CreditDebit <CdtDbt> [0..1] CodeSet 393
3.4.8.3.2.3  LotQuantity <LotQty>
Presence: [0..1]
Definition: Quantity of financial instruments that is part of the lot described.
LotQuantity <LotQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 406 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 407
Or   FaceAmount <FaceAmt> [1..1] Amount 407
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 407
3.4.8.3.2.4  CashSubBalanceType <CshSubBalTp>
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
45 March 2024
```

