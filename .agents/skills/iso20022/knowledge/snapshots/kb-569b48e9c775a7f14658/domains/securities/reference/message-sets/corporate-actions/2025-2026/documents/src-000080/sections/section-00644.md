---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.3 Balance", "16.1.3.3 TotalEligibleBalanceFormat10"]
file_pages: [835]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.3.3 TotalEligibleBalanceFormat10

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 835 to 835.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 835

```text
NotEligibleBalance <NotElgblBal> contains the following elements (see "SignedQuantityFormat10"
on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
16.1.3.3  TotalEligibleBalanceFormat10
Definition: Total eligible balance for the corporate action and full and part way period units.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Balance <Bal> [0..1] ± 835
   FullPeriodUnits <FullPrdUnits> [0..1] ± 835
   PartWayPeriodUnits <PartWayPrdUnits> [0..1] ± 836
16.1.3.3.1  Balance <Bal>
Presence: [0..1]
Definition: Provides information about balance related to a corporate action.
Balance <Bal> contains one of the following elements (see "Quantity49Choice" on page 1086 for
details)
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
16.1.3.3.2  FullPeriodUnits <FullPrdUnits>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 835 February 2026
```

