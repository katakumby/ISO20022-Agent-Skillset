---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.15 WithdrawalAllowedIndicator <WdrwlAllwdInd>"]
file_pages: [146]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.15 WithdrawalAllowedIndicator <WdrwlAllwdInd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 146 to 146.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 146

```text
No: no certification required.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
3.4.11.15  WithdrawalAllowedIndicator <WdrwlAllwdInd>
Presence: [0..1]
Definition: Indicates whether withdrawal of instruction is allowed.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
3.4.11.16  ChangeAllowedIndicator <ChngAllwdInd>
Presence: [0..1]
Definition: Indicates whether change of instruction is allowed.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
3.4.11.17  AppliedOptionIndicator <ApldOptnInd>
Presence: [0..1]
Definition: Indicates whether the option, different from the default one, shall be applied by the account
owner.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
3.4.11.18  FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..1]
Definition: Identifies the financial instrument.
Impacted by: C23 "DescriptionPresenceRule", C24 "DescriptionUsageRule", C61 "ISINGuideline", C62
"ISINPresenceRule", C91 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 146 February 2026
```

