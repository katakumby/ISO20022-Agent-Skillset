---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["13 camt.014.001.05 ReturnMemberV05", "13.4 Message Building Blocks", "13.4.2 ReportOrError <RptOrErr>", "13.4.2.1 Report <Rpt>", "13.4.2.1.2 MemberOrError <MmbOrErr>", "13.4.2.1.2.1 Member <Mmb>", "13.4.2.1.2.1.4 Type <Tp>", "13.4.2.1.2.1.4.1 Code <Cd>"]
file_pages: [490]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.014.001.05"]
---

# 13.4.2.1.2.1.4.1 Code <Cd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 490 to 490.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 490

```text
Type <Tp> contains one of the following SystemMemberType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 490
Or}   Proprietary <Prtry> [1..1] Text 490
13.4.2.1.2.1.4.1  Code <Cd>
Presence: [1..1]
Definition: System member type, in a coded form.
Datatype: "ExternalSystemMemberType1Code" on page 857
13.4.2.1.2.1.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: System member type, in a proprietary form.
Datatype: "Max35Text" on page 889
13.4.2.1.2.1.5  Status <Sts>
Presence: [0..1]
Definition: Status of a member in a system, for example enabled or deleted.
Status <Sts> contains one of the following SystemMemberStatus1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 490
Or}   Proprietary <Prtry> [1..1] Text 490
13.4.2.1.2.1.5.1  Code <Cd>
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
13.4.2.1.2.1.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: System member status, in a proprietary form.
Datatype: "Max35Text" on page 889
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 490 February 2025
```

