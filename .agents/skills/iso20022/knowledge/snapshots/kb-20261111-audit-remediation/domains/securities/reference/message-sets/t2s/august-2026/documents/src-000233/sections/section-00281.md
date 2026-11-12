---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["16 camt.078.001.02 IntraBalanceMovementQueryV02", "16.4 Message Building Blocks", "16.4.2 QueryDefinition <QryDef>", "16.4.2.2 SearchCriteria <SchCrit>", "16.4.2.2.6 BalanceType <BalTp>", "16.4.2.2.6.2 BalanceTo <BalTo>", "16.4.2.2.6.2.1 Type <Tp>", "16.4.2.2.6.2.1.1 Code <Cd>"]
file_pages: [368]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 16.4.2.2.6.2.1.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 368 to 368.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 368

```text
Definition: Specifies the securities sub balance type indicator (example restriction type for a market
infrastructure).
Type <Tp> contains one of the following CashBalanceType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 368
Or}   Proprietary <Prtry> [1..1] ± 368
16.4.2.2.6.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Cash balance expressed in a coded form.
Datatype: "ExternalBalanceType1Code" on page 3240
16.4.2.2.6.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Cash balance expressed in a proprietary form.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
16.4.2.2.6.2.2  QuantityBreakdown <QtyBrkdwn>
Presence: [0..*]
Definition: Breakdown of a quantity into lots such as tax lots, instrument series.
QuantityBreakdown <QtyBrkdwn> contains the following AmountAndQuantityBreakdown1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 368
   LotAmount <LotAmt> [0..1] ± 369
   LotQuantity <LotQty> [0..1] ± 369
   CashSubBalanceType <CshSubBalTp> [0..1] ± 369
16.4.2.2.6.2.2.1  LotNumber <LotNb>
Presence: [0..1]
Definition: Identification, for tax purposes, of a lot of identical securities that are bought at a certain date
and at a certain price.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities 368 August 2026
```

