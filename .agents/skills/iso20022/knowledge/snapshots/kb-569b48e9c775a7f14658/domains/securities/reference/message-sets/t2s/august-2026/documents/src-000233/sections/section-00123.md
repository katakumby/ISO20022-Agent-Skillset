---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["10 camt.072.001.02 IntraBalanceMovementModificationRequestV02", "10.4 Message Building Blocks", "10.4.6 UnderlyingIntraBalance <UndrlygIntraBal>", "10.4.6.3 BalanceFrom <BalFr>", "10.4.6.3.2 QuantityBreakdown <QtyBrkdwn>", "10.4.6.3.2.2 LotAmount <LotAmt>"]
file_pages: [168]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.072.001.02"]
---

# 10.4.6.3.2.2 LotAmount <LotAmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 168 to 168.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 168

```text
LotNumber <LotNb> contains the following elements (see "GenericIdentification37" on page 2965 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
10.4.6.3.2.2  LotAmount <LotAmt>
Presence: [0..1]
Definition: Amount of money that is part of the lot described.
LotAmount <LotAmt> contains the following elements (see "AmountAndDirection5" on page 2841 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C4 2841
   CreditDebit <CdtDbt> [0..1] CodeSet 2842
10.4.6.3.2.3  LotQuantity <LotQty>
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
10.4.6.3.2.4  CashSubBalanceType <CshSubBalTp>
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities 168 August 2026
```

