---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.3 Balance", "16.1.3.2 BalanceFormat11Choice", "16.1.3.2.1 Balance <Bal>"]
file_pages: [834]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.3.2.1 Balance <Bal>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 834 to 834.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 834

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
16.1.3.2.1  Balance <Bal>
Presence: [1..1]
Definition: Provides information about balance related to a corporate action.
Balance <Bal> contains the following elements (see "SignedQuantityFormat11" on page 1094 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1094
   QuantityChoice <QtyChc> [1..1]  1094
{Or     Quantity <Qty> [1..1] ± C13 1095
Or}     ProprietaryQuantity <PrtryQty> [1..1]  1095
       Quantity <Qty> [1..1] Quantity 1095
       QuantityType <QtyTp> [1..1] Text 1095
       Issuer <Issr> [1..1] Text 1095
       SchemeName <SchmeNm> [0..1] Text 1096
16.1.3.2.2  EligibleBalance <ElgblBal>
Presence: [1..1]
Definition: Provide eligible balance information in different formats.
EligibleBalance <ElgblBal> contains the following elements (see "SignedQuantityFormat10" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
16.1.3.2.3  NotEligibleBalance <NotElgblBal>
Presence: [1..1]
Definition: Provide not eligible balance information in different formats.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 834 February 2026
```

