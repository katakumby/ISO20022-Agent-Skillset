---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.14 Date Time Period", "66.1.14.6 DateTimePeriod1", "66.1.14.6.2 ToDateTime <ToDtTm>"]
file_pages: [4475]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.14.6.2 ToDateTime <ToDtTm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4475 to 4475.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4475

```text
Datatype: "ISODateTime" on page 5388
66.1.14.6.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the period ends.
Datatype: "ISODateTime" on page 5388
66.1.15 De Minimus
66.1.15.1  DeMinimus1Choice
Definition: De minimus applicability conditions.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DeMinimusApplicable <DeMnmsAplbl> [1..1] ± 4475
Or}   DeMinimusNotApplicable <DeMnmsNotAplbl> [1..1] ± 4475
66.1.15.1.1  DeMinimusApplicable <DeMnmsAplbl>
Presence: [1..1]
Definition: Conditions applicable when the investor is covered by the "de minimis" exemption.
DeMinimusApplicable <DeMnmsAplbl> contains the following elements (see
"DeMinimusApplicable1" on page 4475 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NewIssuePermission <NewIssePrmssn> [1..1] Indicator 4476
   Percentage <Pctg> [0..1] Rate 4476
66.1.15.1.2  DeMinimusNotApplicable <DeMnmsNotAplbl>
Presence: [1..1]
Definition: Conditions applicable when the investor is not covered by the "de minimis" exemption.
DeMinimusNotApplicable <DeMnmsNotAplbl> contains the following elements (see
"DeMinimusNotApplicable1" on page 4476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RestrictedPersonReason <RstrctdPrsnRsn> [1..1] Text 4476
66.1.15.2  DeMinimusApplicable1
Definition: Conditions applicable when the investor is covered by the "de minimis" exemption.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4475 May 2026
```

