---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.3 Balance"]
file_pages: [832]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.3 Balance

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 832 to 832.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 832

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.3 Balance
16.1.3.1  BalanceFormat12Choice
Definition: Choice between balance, eligible balance and not eligible balance formats.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 832
Or   EligibleBalance <ElgblBal> [1..1] ± 832
Or   NotEligibleBalance <NotElgblBal> [1..1] ± 833
Or   FullPeriodUnits <FullPrdUnits> [1..1] ± 833
Or}   PartWayPeriodUnits <PartWayPrdUnits> [1..1] ± 833
16.1.3.1.1  Balance <Bal>
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
16.1.3.1.2  EligibleBalance <ElgblBal>
Presence: [1..1]
Definition: Provide eligible balance information in different formats.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 832 February 2026
```

