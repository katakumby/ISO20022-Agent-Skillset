---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.11 Date Time Period", "6.1.11.2 TimePeriodDetails1", "6.1.11.2.2 ToTime <ToTm>"]
file_pages: [828]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.11.2.2 ToTime <ToTm>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 828 to 828.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 828

```text
6.1.11.2.2  ToTime <ToTm>
Presence: [0..1]
Definition: Time at which the time span ends.
Datatype: "ISOTime" on page 918
6.1.11.3  DateTimePeriod1
Definition: Time span defined by a start date and time, and an end date and time.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 828
   ToDateTime <ToDtTm> [1..1] DateTime 828
6.1.11.3.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the period starts.
Datatype: "ISODateTime" on page 908
6.1.11.3.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the period ends.
Datatype: "ISODateTime" on page 908
6.1.12 Financial Institution Identification
6.1.12.1  ClearingSystemMemberIdentification2
Definition: Unique identification, as assigned by a clearing system, to unambiguously identify a member
of the clearing system.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingSystemIdentification <ClrSysId> [0..1] ± 828
   MemberIdentification <MmbId> [1..1] Text 829
6.1.12.1.1  ClearingSystemIdentification <ClrSysId>
Presence: [0..1]
Definition: Specification of a pre-agreed offering between clearing agents or the channel through which
the payment instruction is processed.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
828 March 2026
```

