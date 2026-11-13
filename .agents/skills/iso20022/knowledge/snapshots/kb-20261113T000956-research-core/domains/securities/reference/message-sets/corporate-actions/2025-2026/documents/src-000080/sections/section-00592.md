---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.1 GeneralInformation <GnlInf>", "14.4.3.5.1.4 MandatoryVoluntaryEventType <MndtryVlntryEvtTp>"]
file_pages: [774]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.1.4 MandatoryVoluntaryEventType <MndtryVlntryEvtTp>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 774 to 774.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 774

```text
EventType <EvtTp> contains one of the following elements (see
"CorporateActionEventType112Choice" on page 989 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 989
Or}   Proprietary <Prtry> [1..1] ± 995
Constraints
• EventTypeRule
If Code is present, the code OTHR must only be used in case no other corporate action event code
is appropriate.
If Code is present, the code CHAN must only be used in case no other corporate action event code
is appropriate and only for an event which relates to a change.
If Code is present, the code REDM must only be used when the redemption is decided by the issuer
and not by the securities holders.
14.4.3.5.1.4  MandatoryVoluntaryEventType <MndtryVlntryEvtTp>
Presence: [1..1]
Definition: Specifies whether the event is mandatory, mandatory with options or voluntary.
MandatoryVoluntaryEventType <MndtryVlntryEvtTp> contains one of the following elements (see
"CorporateActionMandatoryVoluntary3Choice" on page 975 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 975
Or}   Proprietary <Prtry> [1..1] ± 975
14.4.3.5.1.5  LastNotificationIdentification <LastNtfctnId>
Presence: [0..1]
Definition: Provides information about the identification of the last notification.
LastNotificationIdentification <LastNtfctnId> contains the following elements (see
"NotificationIdentification5" on page 953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 954
   CreationDateTime <CreDtTm> [0..1] ± 954
14.4.3.5.2  UnderlyingSecurity <UndrlygScty>
Presence: [1..1]
Definition: Security concerned by the corporate action.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 774 February 2026
```

