---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.6 MarketPracticeVersion1", "66.1.28.6.2 Date <Dt>"]
file_pages: [4819]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.6.2 Date <Dt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4819 to 4819.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4819

```text
66.1.28.6.2  Date <Dt>
Presence: [0..1]
Definition: Year and month, for example, 2013-06.
Datatype: "ISOYearMonth" on page 5406
66.1.28.6.3  Number <Nb>
Presence: [0..1]
Definition: Version of the market practice.
Datatype: "Max35Text" on page 5403
66.1.28.7  NewIssueAllocation2
Definition: Information about the investment account ownership with respect to new issue allocation for
a hedge fund.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Restricted <Rstrctd> [1..1] Indicator 4819
   ExemptPersonReason <XmptPrsnRsn> [0..1] Text 4819
   DeMinimus <DeMnms> [0..1] ± 4819
66.1.28.7.1  Restricted <Rstrctd>
Presence: [1..1]
Definition: Indicates whether the investor is eligible to participate in the profits and losses from a new
issue.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.28.7.2  ExemptPersonReason <XmptPrsnRsn>
Presence: [0..1]
Definition: Reason for exemption.
Datatype: "Max350Text" on page 5403
66.1.28.7.3  DeMinimus <DeMnms>
Presence: [0..1]
Definition: Conditions applicable when the investor is covered by the "de minimis" exemption.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4819 May 2026
```

