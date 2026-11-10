---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.7 AccountDetails <AcctDtls>", "5.4.7.5 Balance <Bal>", "5.4.7.5.1 TotalEligibleBalance <TtlElgblBal>"]
file_pages: [296]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.7.5.1 TotalEligibleBalance <TtlElgblBal>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 296 to 296.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 296

```text
5.4.7.5.1  TotalEligibleBalance <TtlElgblBal>
Presence: [0..1]
Definition: Total quantity of financial instruments of the balance.
TotalEligibleBalance <TtlElgblBal> contains one of the following elements (see "Quantity49Choice"
on page 1086 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QuantityChoice <QtyChc> [1..1]  1087
{Or     OriginalAndCurrentFaceAmount
<OrgnlAndCurFaceAmt>
[1..1]  1087
       ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1088
       FaceAmount <FaceAmt> [1..1] Amount 1088
       AmortisedValue <AmtsdVal> [1..1] Amount 1088
Or}     SignedQuantity <SgndQty> [1..1] ± 1088
Or}   ProprietaryQuantity <PrtryQty> [1..1]  1088
     ShortLongPosition <ShrtLngPos> [0..1] CodeSet 1089
     Quantity <Qty> [1..1] Quantity 1089
     QuantityType <QtyTp> [1..1] Text 1089
     Issuer <Issr> [1..1] Text 1089
     SchemeName <SchmeNm> [0..1] Text 1089
5.4.7.5.2  BlockedBalance <BlckdBal>
Presence: [0..1]
Definition: Balance of financial instruments that are blocked.
BlockedBalance <BlckdBal> contains one of the following elements (see "BalanceFormat11Choice"
on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
5.4.7.5.3  BorrowedBalance <BrrwdBal>
Presence: [0..1]
Definition: Balance of financial instruments that have been borrowed from another party.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 296 February 2026
```

