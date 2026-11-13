---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.17 SwitchProcessingCharacteristics <SwtchPrcgChrtcs>"]
file_pages: [328]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.17 SwitchProcessingCharacteristics <SwtchPrcgChrtcs>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 328 to 328.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 328

```text
Constraints
• DealingCutOffTimeFrameRule
If DealingCutOffTimeFrame is present, then DealingCutOffTimeFrame/OtherTimeFrameDescription
or DealingCutOffTimeFrame/ReferToOrderDesk or DealingCutOffTimeFrame/TradeMinus must be
present.
On Condition
    /DealingCutOffTimeFrame is present
Following Must be True
    /DealingCutOffTimeFrame/OtherTimeFrameDescription Must be present
 Or    /DealingCutOffTimeFrame/TradeMinus Must be present
 Or    /DealingCutOffTimeFrame/ReferToOrderDesk Must be present
15.4.5.17  SwitchProcessingCharacteristics <SwtchPrcgChrtcs>
Presence: [0..1]
Definition: Processing characteristics linked to a switch of the investment fund or alternative/hedge
fund.
Impacted by: C10 "DealingCutOffTimeFrameRule"
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 328 May 2026
```

