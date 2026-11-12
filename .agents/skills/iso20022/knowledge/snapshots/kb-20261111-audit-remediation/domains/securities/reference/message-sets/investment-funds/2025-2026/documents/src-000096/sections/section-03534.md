---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.28 MainFundOrderDeskLocation1", "66.1.26.28.2 TimeZoneOffSet <TmZoneOffSet>"]
file_pages: [4784]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.28.2 TimeZoneOffSet <TmZoneOffSet>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4784 to 4784.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4784

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.26.28.2  TimeZoneOffSet <TmZoneOffSet>
Presence: [1..1]
Definition: Offset of the reporting time before or after 00: 00 hour UTC.
TimeZoneOffSet <TmZoneOffSet> contains the following UTCOffset1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [1..1] Indicator 4784
   NumberOfHours <NbOfHrs> [1..1] Time 4784
66.1.26.28.2.1  Sign <Sgn>
Presence: [1..1]
Definition: Indicates whether the offset is before or after 00: 00 hour UTC.
Datatype: One of the following values must be used (see "PlusOrMinusIndicator" on page 5399):
• Meaning When True: Plus
• Meaning When False: Minus
66.1.26.28.2.2  NumberOfHours <NbOfHrs>
Presence: [1..1]
Definition: Offset of the reporting time, in hours, before or after 00: 00 hour UTC.
Datatype: "ISOTime" on page 5405
66.1.26.29  ProcessingCharacteristics12
Definition: Processing characteristics linked to a redemption from an investment fund or alternative/
hedge fund.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4784 May 2026
```

