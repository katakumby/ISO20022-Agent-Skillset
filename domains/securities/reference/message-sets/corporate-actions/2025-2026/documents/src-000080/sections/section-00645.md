---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.3 Balance", "16.1.3.3 TotalEligibleBalanceFormat10", "16.1.3.3.3 PartWayPeriodUnits <PartWayPrdUnits>"]
file_pages: [836]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.3.3.3 PartWayPeriodUnits <PartWayPrdUnits>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 836 to 836.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 836

```text
Definition: Number of units of a fund that were purchased in a previous distribution period and/or held at
the beginning of a distribution period, for example Group I Units in the UK.
FullPeriodUnits <FullPrdUnits> contains the following elements (see "SignedQuantityFormat10" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
16.1.3.3.3  PartWayPeriodUnits <PartWayPrdUnits>
Presence: [0..1]
Definition: Number of units of a fund that were purchased part way throughout a distribution period, for
example Group II Units in the U.K.
PartWayPeriodUnits <PartWayPrdUnits> contains the following elements (see
"SignedQuantityFormat10" on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
16.1.4 Date Period
16.1.4.1  CorporateActionPeriod17
Definition: Specifies periods of a corporate action.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 836 February 2026
```

