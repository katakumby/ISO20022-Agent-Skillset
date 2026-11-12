---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 camt.068.001.02 IntraBalanceMovementConfirmationV02", "4.4 Message Building Blocks", "4.4.6 IntraBalance <IntraBal>", "4.4.6.5 BalanceFrom <BalFr>", "4.4.6.5.1 Type <Tp>"]
file_pages: [60]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.068.001.02"]
---

# 4.4.6.5.1 Type <Tp>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 60 to 60.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 60

```text
BalanceFrom <BalFr> contains the following CashSubBalanceTypeAndQuantityBreakdown3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  60
{Or     Code <Cd> [1..1] CodeSet 60
Or}     Proprietary <Prtry> [1..1] ± 60
   QuantityBreakdown <QtyBrkdwn> [0..*]  61
     LotNumber <LotNb> [0..1] ± 61
     LotAmount <LotAmt> [0..1] ± 61
     LotQuantity <LotQty> [0..1] ± 61
     CashSubBalanceType <CshSubBalTp> [0..1] ± 62
4.4.6.5.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the securities sub balance type indicator (example restriction type for a market
infrastructure).
Type <Tp> contains one of the following CashBalanceType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 60
Or}   Proprietary <Prtry> [1..1] ± 60
4.4.6.5.1.1  Code <Cd>
Presence: [1..1]
Definition: Cash balance expressed in a coded form.
Datatype: "ExternalBalanceType1Code" on page 480
4.4.6.5.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Cash balance expressed in a proprietary form.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 409 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 409
   Issuer <Issr> [1..1] Text 409
   SchemeName <SchmeNm> [0..1] Text 409
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.068.001.02
IntraBalanceMovementConfirmationV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
60 March 2024
```

