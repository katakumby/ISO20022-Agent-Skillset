---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["21 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "21.4 Message Building Blocks", "21.4.4 ReportOrError <RptOrErr>", "21.4.4.1 Cancellations <Cxls>", "21.4.4.1.5 Cancellation <Cxl>", "21.4.4.1.5.8 UnderlyingIntraBalance <UndrlygIntraBal>", "21.4.4.1.5.8.4 BalanceTo <BalTo>", "21.4.4.1.5.8.4.2 QuantityBreakdown <QtyBrkdwn>", "21.4.4.1.5.8.4.2.3 LotQuantity <LotQty>"]
file_pages: [519]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 21.4.4.1.5.8.4.2.3 LotQuantity <LotQty>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 519 to 519.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 519

```text
21.4.4.1.5.8.4.2.3  LotQuantity <LotQty>
Presence: [0..1]
Definition: Quantity of financial instruments that is part of the lot described.
LotQuantity <LotQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
21.4.4.1.5.8.4.2.4  CashSubBalanceType <CshSubBalTp>
Presence: [0..1]
Definition: Specifies the securities sub balance type indicator (example restriction type for a market
infrastructure).
CashSubBalanceType <CshSubBalTp> contains the following elements (see
"GenericIdentification30" on page 2966 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
21.4.4.1.5.8.5  CashSubBalanceIdentification <CshSubBalId>
Presence: [0..1]
Definition: Number identifying a lot constituting the sub-balance.
CashSubBalanceIdentification <CshSubBalId> contains the following elements (see
"GenericIdentification37" on page 2965 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
21.4.4.1.5.8.6  Priority <Prty>
Presence: [0..1]
Definition: Specifies whether the transaction is to be executed with a high priority.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 519 August 2026
```

