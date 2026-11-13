---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.37 Statement58", "82.1.19.37.1 QueryReference <QryRef>"]
file_pages: [3020]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.37.1 QueryReference <QryRef>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3020 to 3020.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3020

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueryReference <QryRef> [0..1] Text 3020
   ReportIdentification <RptId> [0..1] Text 3020
   HistoricData <HstrcData> [1..1] Indicator 3020
   ActivityIndicator <ActvtyInd> [1..1] Indicator 3020
   SubAccountIndicator <SubAcctInd> [1..1] Indicator 3021
Constraints
• ReportNumberRule
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different ReportNumbers. For example, a daily report sent on day 1
would have ReportNumber 001, on day 2, 002, etc.
82.1.19.37.1  QueryReference <QryRef>
Presence: [0..1]
Definition: Identification of the SecuritiesStatementQuery message sent to request this statement.
Datatype: "Max35Text" on page 3328
82.1.19.37.2  ReportIdentification <RptId>
Presence: [0..1]
Definition: Reference common to all pages of a report.
Datatype: "Max35Text" on page 3328
82.1.19.37.3  HistoricData <HstrcData>
Presence: [1..1]
Definition: Specifies whether the data is either historical (true) or current (false).
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 3323):
• Meaning When True: True
• Meaning When False: False
82.1.19.37.4  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3020 August 2026
```

