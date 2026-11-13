---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["12 camt.013.001.04 GetMemberV04", "12.4 Message Building Blocks", "12.4.2 MemberQueryDefinition <MmbQryDef>", "12.4.2.2 MemberCriteria <MmbCrit>", "12.4.2.2.2 NewCriteria <NewCrit>", "12.4.2.2.2.2 SearchCriteria <SchCrit>", "12.4.2.2.2.2.2 Type <Tp>", "12.4.2.2.2.2.2.2 Proprietary <Prtry>"]
file_pages: [473]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.013.001.04"]
---

# 12.4.2.2.2.2.2.2 Proprietary <Prtry>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 473 to 473.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 473

```text
Definition: System member type, in a coded form.
Datatype: "ExternalSystemMemberType1Code" on page 857
12.4.2.2.2.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: System member type, in a proprietary form.
Datatype: "Max35Text" on page 889
12.4.2.2.2.2.3  Status <Sts>
Presence: [0..*]
Definition: Status of a member in a system, such as enabled or deleted.
Status <Sts> contains one of the following SystemMemberStatus1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 473
Or}   Proprietary <Prtry> [1..1] Text 473
12.4.2.2.2.2.3.1  Code <Cd>
Presence: [1..1]
Definition: System member status, in a coded form.
Datatype: "MemberStatus1Code" on page 861
CodeName Name Definition
ENBL Enabled Member is live on the system.
DSBL Disabled Member is temporarily not live on the
system.
DLTD Deleted Member is no longer live on the system.
JOIN Joining Member is joining and will soon be
enabled on the system.
12.4.2.2.2.2.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: System member status, in a proprietary form.
Datatype: "Max35Text" on page 889
12.4.2.2.2.3  ReturnCriteria <RtrCrit>
Presence: [0..1]
Definition: Defines the expected report.
Approved by the Payments SEG on 04 February 2025 camt.013.001.04 GetMemberV04
Cash Management - Maintenance 2024 - 2025 473 February 2025
```

