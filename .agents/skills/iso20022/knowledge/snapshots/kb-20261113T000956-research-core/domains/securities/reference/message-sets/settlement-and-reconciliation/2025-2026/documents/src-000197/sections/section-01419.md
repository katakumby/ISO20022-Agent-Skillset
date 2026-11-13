---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.16 PendingStatus20Choice", "35.1.29.16.1 Forwarded <Fwdd>"]
file_pages: [1900]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.16.1 Forwarded <Fwdd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1900 to 1900.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1900

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Forwarded <Fwdd> [1..1] ± 1900
Or}   UnderInvestigation <UdrInvstgtn> [1..1] ± 1900
35.1.29.16.1  Forwarded <Fwdd>
Presence: [1..1]
Definition: Allegement is forwarded.
Forwarded <Fwdd> contains the following elements (see "NoSpecifiedReason1" on page 1900 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1900
35.1.29.16.2  UnderInvestigation <UdrInvstgtn>
Presence: [1..1]
Definition: Allegement is under investigation.
UnderInvestigation <UdrInvstgtn> contains the following elements (see "NoSpecifiedReason1" on
page 1900 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1900
35.1.29.17  NoSpecifiedReason1
Definition: No specified reason available for the status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1900
35.1.29.17.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.18  PendingStatus67Choice
Definition: Specifies whether the status is provided with a reason or not.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1900 March 2026
```

