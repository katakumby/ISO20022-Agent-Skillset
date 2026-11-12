---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.2 NotificationGeneralInformation <NtfctnGnlInf>", "3.4.2.1 NotificationIdentification <NtfctnId>"]
file_pages: [61, 62]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.2.1 NotificationIdentification <NtfctnId>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 61 to 62.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 61

```text
NotificationGeneralInformation <NtfctnGnlInf> contains the following
CorporateActionNotification9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NotificationIdentification <NtfctnId> [0..1] Text 61
   NotificationType <NtfctnTp> [1..1] CodeSet 61
   ProcessingStatus <PrcgSts> [1..1] ± 61
Constraints
• NotificationTypeGuideline
NotificationType REPL is used to replace a previously sent CorporateActionNotification message that
was reported with EventCompletenessStatus being incomplete or complete.
3.4.2.1  NotificationIdentification <NtfctnId>
Presence: [0..1]
Definition: Unique identification of the group of corporate action notification messages when the
notification is split in multiple (paginated) messages.
Datatype: "Max35Text" on page 1251
3.4.2.2  NotificationType <NtfctnTp>
Presence: [1..1]
Definition: Specifies the type of notification.
Datatype: "CorporateActionNotificationType1Code" on page 1196
CodeName Name Definition
NEWM New New notification.
REPL Replacement Notification replacing a previously sent
notification.
RMDR Reminder Notification sent as a reminder of an
event taking place.
3.4.2.3  ProcessingStatus <PrcgSts>
Presence: [1..1]
Definition: Specifies the status of the details of the corporate action event.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 61 February 2026
```

## File page 62

```text
ProcessingStatus <PrcgSts> contains one of the following elements (see
"CorporateActionProcessingStatus5Choice" on page 916 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1]  917
     EventCompletenessStatus <EvtCmpltnsSts> [1..1] CodeSet 917
     EventConfirmationStatus <EvtConfSts> [1..1] CodeSet 917
Or}   Proprietary <Prtry> [1..1] ± 917
3.4.3 PreviousNotificationIdentification <PrvsNtfctnId>
Presence: [0..1]
Definition: Identification of the previously sent notification document.
PreviousNotificationIdentification <PrvsNtfctnId> contains the following elements (see
"DocumentIdentification31" on page 860 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 861
   LinkageType <LkgTp> [0..1] ± C22 861
3.4.4 InstructionIdentification <InstrId>
Presence: [0..1]
Definition: Identification of a related instruction document.
InstructionIdentification <InstrId> contains the following elements (see "DocumentIdentification9" on
page 877 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 877
3.4.5 OtherDocumentIdentification <OthrDocId>
Presence: [0..*]
Definition: Identification of other documents as well as the document number.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 62 February 2026
```

