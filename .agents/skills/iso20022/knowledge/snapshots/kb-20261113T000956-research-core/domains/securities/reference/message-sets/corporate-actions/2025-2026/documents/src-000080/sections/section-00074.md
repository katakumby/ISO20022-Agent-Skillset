---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.10 ChargesAppliedIndicator <ChrgsApldInd>"]
file_pages: [120]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.10 ChargesAppliedIndicator <ChrgsApldInd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 120 to 120.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 120

```text
• Meaning When True: Yes
• Meaning When False: No
3.4.10.10  ChargesAppliedIndicator <ChrgsApldInd>
Presence: [0..1]
Definition: Indicates whether charges apply to the holder, for instance redemption charges.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
3.4.10.11  RestrictionIndicator <RstrctnInd>
Presence: [0..1]
Definition: Indicates whether restrictions apply to the corporate action event or not.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
3.4.10.12  AccruedInterestIndicator <AcrdIntrstInd>
Presence: [0..1]
Definition: Indicates whether the holder is entitled to accrued interest.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
3.4.10.13  ForfeitureOfInterestIndicator <FrftrOfIntrstInd>
Presence: [0..1]
Definition: Indicates that bondholders who convert between record date and payable date will forfeit
their interest.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
3.4.10.14  LetterOfGuaranteedDeliveryIndicator <LttrOfGrntedDlvryInd>
Presence: [0..1]
Definition: Indicates whether a letter of guaranteed delivery can be submitted in order to participate in
the offer on full eligible position. It is not intended for use in situations arising from failed or late trades.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 120 February 2026
```

