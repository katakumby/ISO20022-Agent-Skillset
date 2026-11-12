---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.15 ShareholderRightsDirectiveIndicator <ShrhldrRghtsDrctvInd>"]
file_pages: [121]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.15 ShareholderRightsDirectiveIndicator <ShrhldrRghtsDrctvInd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 121 to 121.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 121

```text
• Meaning When True: Yes
• Meaning When False: No
3.4.10.15  ShareholderRightsDirectiveIndicator <ShrhldrRghtsDrctvInd>
Presence: [0..1]
Definition: Indicates whether the announcement was initiated by the first intermediary in the custody
chain in accordance with SRD II.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
3.4.10.16  DividendType <DvddTp>
Presence: [0..1]
Definition: Specifies the conditions in which a dividend is paid.
DividendType <DvddTp> contains one of the following elements (see "DividendTypeFormat9Choice"
on page 922 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 922
Or}   Proprietary <Prtry> [1..1] ± 923
3.4.10.17  EventSequenceType <EvtSeqTp>
Presence: [0..1]
Definition: Specifies whether the event is an interim or a final event in a series of predefined or planned
events of the same type and for the same underlying instrument.
EventSequenceType <EvtSeqTp> contains one of the following elements (see
"EventSequenceTypeFormat1Choice" on page 922 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 922
Or}   Proprietary <Prtry> [1..1] ± 922
3.4.10.18  OccurrenceType <OcrncTp>
Presence: [0..1]
Definition: Specifies the conditions in which the instructions and/or payment of the proceeds occurs.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 121 February 2026
```

