---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["9 camt.068.001.02 IntraBalanceMovementConfirmationV02", "9.4 Message Building Blocks", "9.4.6 IntraBalance <IntraBal>", "9.4.6.5 BalanceFrom <BalFr>", "9.4.6.5.2 QuantityBreakdown <QtyBrkdwn>"]
file_pages: [144]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.068.001.02"]
---

# 9.4.6.5.2 QuantityBreakdown <QtyBrkdwn>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 144 to 144.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 144

```text
9.4.6.5.2  QuantityBreakdown <QtyBrkdwn>
Presence: [0..*]
Definition: Breakdown of a quantity into lots such as tax lots, instrument series.
QuantityBreakdown <QtyBrkdwn> contains the following AmountAndQuantityBreakdown1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 144
   LotAmount <LotAmt> [0..1] ± 144
   LotQuantity <LotQty> [0..1] ± 144
   CashSubBalanceType <CshSubBalTp> [0..1] ± 145
9.4.6.5.2.1  LotNumber <LotNb>
Presence: [0..1]
Definition: Identification, for tax purposes, of a lot of identical securities that are bought at a certain date
and at a certain price.
LotNumber <LotNb> contains the following elements (see "GenericIdentification37" on page 2965 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
9.4.6.5.2.2  LotAmount <LotAmt>
Presence: [0..1]
Definition: Amount of money that is part of the lot described.
LotAmount <LotAmt> contains the following elements (see "AmountAndDirection5" on page 2841 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C4 2841
   CreditDebit <CdtDbt> [0..1] CodeSet 2842
9.4.6.5.2.3  LotQuantity <LotQty>
Presence: [0..1]
Definition: Quantity of financial instruments that is part of the lot described.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.068.001.02
IntraBalanceMovementConfirmationV02
Target2-Securities 144 August 2026
```

