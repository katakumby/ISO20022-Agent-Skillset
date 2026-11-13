---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.3 InvestmentAccount74", "66.1.24.3.5 Name <Nm>"]
file_pages: [4562]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.3.5 Name <Nm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4562 to 4562.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4562

```text
Definition: Date the status is assigned.
StatusDate <StsDt> contains one of the following elements (see "DateAndDateTime1Choice" on
page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4467
Or}   DateTime <DtTm> [1..1] DateTime 4467
66.1.24.3.5  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
66.1.24.3.6  Designation <Dsgnt>
Presence: [0..1]
Definition: Supplementary registration information applying to a specific block of units for dealing and
reporting purposes. The supplementary registration information may be used when all the units are
registered, for example, to a funds supermarket, but holdings for each investor have to be reconciled
individually.
Datatype: "Max35Text" on page 5403
66.1.24.3.7  Type <Tp>
Presence: [0..1]
Definition: Type of account.
Type <Tp> contains one of the following elements (see "AccountType2Choice" on page 4327 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4327
Or}   Proprietary <Prtry> [1..1] ± 4327
66.1.24.3.8  OwnershipType <OwnrshTp>
Presence: [0..1]
Definition: Ownership status of the account, for example, joint owners.
OwnershipType <OwnrshTp> contains one of the following elements (see "OwnershipType2Choice"
on page 4640 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4640
Or}   Proprietary <Prtry> [1..1] ± 4642
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4562 May 2026
```

