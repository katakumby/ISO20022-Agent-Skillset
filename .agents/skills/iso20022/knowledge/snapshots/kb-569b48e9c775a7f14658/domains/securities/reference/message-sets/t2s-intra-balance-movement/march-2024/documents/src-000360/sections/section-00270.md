---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["14 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "14.4 Message Building Blocks", "14.4.4 ReportOrError <RptOrErr>", "14.4.4.1 Cancellations <Cxls>", "14.4.4.1.5 Cancellation <Cxl>", "14.4.4.1.5.8 UnderlyingIntraBalance <UndrlygIntraBal>", "14.4.4.1.5.8.4 BalanceTo <BalTo>", "14.4.4.1.5.8.4.2 QuantityBreakdown <QtyBrkdwn>"]
file_pages: [327]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 14.4.4.1.5.8.4.2 QuantityBreakdown <QtyBrkdwn>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 327 to 327.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 327

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 409 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 409
   Issuer <Issr> [1..1] Text 409
   SchemeName <SchmeNm> [0..1] Text 409
14.4.4.1.5.8.4.2  QuantityBreakdown <QtyBrkdwn>
Presence: [0..*]
Definition: Breakdown of a quantity into lots such as tax lots, instrument series.
QuantityBreakdown <QtyBrkdwn> contains the following AmountAndQuantityBreakdown1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 327
   LotAmount <LotAmt> [0..1] ± 327
   LotQuantity <LotQty> [0..1] ± 328
   CashSubBalanceType <CshSubBalTp> [0..1] ± 328
14.4.4.1.5.8.4.2.1  LotNumber <LotNb>
Presence: [0..1]
Definition: Identification, for tax purposes, of a lot of identical securities that are bought at a certain date
and at a certain price.
LotNumber <LotNb> contains the following elements (see "GenericIdentification37" on page 408 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 408
   Issuer <Issr> [0..1] Text 408
14.4.4.1.5.8.4.2.2  LotAmount <LotAmt>
Presence: [0..1]
Definition: Amount of money that is part of the lot described.
LotAmount <LotAmt> contains the following elements (see "AmountAndDirection5" on page 393 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C8 393
   CreditDebit <CdtDbt> [0..1] CodeSet 393
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
327 March 2024
```

