---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.15 De Minimus", "66.1.15.2 DeMinimusApplicable1", "66.1.15.2.1 NewIssuePermission <NewIssePrmssn>"]
file_pages: [4476]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.15.2.1 NewIssuePermission <NewIssePrmssn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4476 to 4476.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4476

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NewIssuePermission <NewIssePrmssn> [1..1] Indicator 4476
   Percentage <Pctg> [0..1] Rate 4476
66.1.15.2.1  NewIssuePermission <NewIssePrmssn>
Presence: [1..1]
Definition: Indicates whether the investor permits its beneficial owners that are restricted persons, if
any, to participate in profits and losses allocated to the investor that are attribute to new issue
securities.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.15.2.2  Percentage <Pctg>
Presence: [0..1]
Definition: Percentage of the new issue profits and losses that it receives to beneficial owners that are
restricted persons.
Datatype: "PercentageRate" on page 5401
66.1.15.3  DeMinimusNotApplicable1
Definition: Conditions applicable when the investor is not covered by the "de minimis" exemption.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RestrictedPersonReason <RstrctdPrsnRsn> [1..1] Text 4476
66.1.15.3.1  RestrictedPersonReason <RstrctdPrsnRsn>
Presence: [1..1]
Definition: Reason for the restricted person.
Datatype: "Max350Text" on page 5403
66.1.16 Direct Debit
66.1.16.1  DirectDebitMandate7
Definition: Direct debit mandate parties and accounts.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4476 May 2026
```

