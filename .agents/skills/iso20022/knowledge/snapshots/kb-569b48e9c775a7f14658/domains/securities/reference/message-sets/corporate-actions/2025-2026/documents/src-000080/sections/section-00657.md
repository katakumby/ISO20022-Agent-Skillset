---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.5 Date Time", "16.1.5.5 DateFormat59Choice", "16.1.5.5.2 DateCode <DtCd>", "16.1.5.5.2.2 Proprietary <Prtry>"]
file_pages: [848]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.5.5.2.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 848 to 848.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 848

```text
Datatype: "DateType9Code" on page 1206
CodeName Name Definition
PWAL BlockingTillEndOfElectionPeriod Blocking occurs until and inclusive of the
end of the election period of the option.
MKDT BlockingTillMarketDeadline Blocking occurs until and inclusive of the
market deadline of the option.
MEET BlockingTillMeetingDate Blocking occurs until and inclusive of the
meeting date.
PAYD BlockingTillPaymentDate Unblocking will occur on payment date of
the option.
RDTE BlockingTillRecordDate Blocking occurs until and inclusive of the
record date of the event.
RDDT BlockingTillResponseDeadline Blocking occurs until and inclusive of the
account servicer deadline for the option.
NARR NarrativeUnblockingDate Refer to additional information element
for the date until when the securities are
blocked.
UKWN Unknown Date is unknown by the sender or has
not been established.
16.1.5.5.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of date.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.5.6  DateAndDateTime2Choice
Definition: Choice between a date or a date and time format.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 848
Or}   DateTime <DtTm> [1..1] DateTime 849
16.1.5.6.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Datatype: "ISODate" on page 1243
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 848 February 2026
```

