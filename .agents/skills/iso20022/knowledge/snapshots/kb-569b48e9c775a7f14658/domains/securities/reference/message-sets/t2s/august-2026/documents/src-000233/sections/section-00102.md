---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["9 camt.068.001.02 IntraBalanceMovementConfirmationV02", "9.4 Message Building Blocks", "9.4.6 IntraBalance <IntraBal>", "9.4.6.5 BalanceFrom <BalFr>", "9.4.6.5.1 Type <Tp>"]
file_pages: [143]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.068.001.02"]
---

# 9.4.6.5.1 Type <Tp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 143 to 143.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 143

```text
BalanceFrom <BalFr> contains the following CashSubBalanceTypeAndQuantityBreakdown3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  143
{Or     Code <Cd> [1..1] CodeSet 143
Or}     Proprietary <Prtry> [1..1] ± 143
   QuantityBreakdown <QtyBrkdwn> [0..*]  144
     LotNumber <LotNb> [0..1] ± 144
     LotAmount <LotAmt> [0..1] ± 144
     LotQuantity <LotQty> [0..1] ± 144
     CashSubBalanceType <CshSubBalTp> [0..1] ± 145
9.4.6.5.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the securities sub balance type indicator (example restriction type for a market
infrastructure).
Type <Tp> contains one of the following CashBalanceType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 143
Or}   Proprietary <Prtry> [1..1] ± 143
9.4.6.5.1.1  Code <Cd>
Presence: [1..1]
Definition: Cash balance expressed in a coded form.
Datatype: "ExternalBalanceType1Code" on page 3240
9.4.6.5.1.2  Proprietary <Prtry>
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.068.001.02
IntraBalanceMovementConfirmationV02
Target2-Securities 143 August 2026
```

