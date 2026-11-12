---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.46 Statement72", "16.1.15.46.8 UpdateType <UpdTp>"]
file_pages: [968]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.46.8 UpdateType <UpdTp>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 968 to 968.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 968

```text
16.1.15.46.8  UpdateType <UpdTp>
Presence: [1..1]
Definition: Indicates whether the report is complete or contains changes only.
UpdateType <UpdTp> contains one of the following elements (see "UpdateType15Choice" on
page 981 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 981
Or}   Proprietary <Prtry> [1..1] ± 981
16.1.15.46.9  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
16.1.15.46.10  NotificationDeadlinePeriod <NtfctnDdlnPrd>
Presence: [0..1]
Definition: Period during which identification deadline has been set.
NotificationDeadlinePeriod <NtfctnDdlnPrd> contains one of the following elements (see
"DateOrDateTimePeriod1Choice" on page 853 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 854
Or}   DateTime <DtTm> [1..1] ± 854
16.1.15.47  CorporateActionEventStageFormat14Choice
Definition: Choice between a standard code or proprietary code to specify the event stage type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 968
Or}   Proprietary <Prtry> [1..1] ± 969
16.1.15.47.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the stage of the corporate action event.
Datatype: "CorporateActionEventStage4Code" on page 1169
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 968 February 2026
```

