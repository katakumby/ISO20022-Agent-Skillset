---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.35 FutureOrOptionDetails3", "7.1.19.35.6 AnnouncementDate <AnncmntDt>"]
file_pages: [327]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.35.6 AnnouncementDate <AnncmntDt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 327 to 327.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 327

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
7.1.19.35.6  AnnouncementDate <AnncmntDt>
Presence: [0..1]
Definition: Date/time, as announced by the issuer, at which the securities will be issued.
Datatype: "ISODateTime" on page 662
7.1.19.35.7  Appearance <Apprnc>
Presence: [0..1]
Definition: Specifies the deliverability of a security.
Datatype: "Appearance1Code" on page 614
CodeName Name Definition
DELI Deliverable Physical certificates exist.
NDEL NotDeliverable Not yet deliverable contract.
LIMI Limited Limited or partial deliverability.
BENT BookEntry Security exists only as an electronic
record, ie, there are no physical
certificates representing the security.
DFBE DeferredBookEntry Deferred printing, book entry.
DLBE DeliverableBookEntry Deliverable, book entry.
TMPG TemporaryGlobal Deferred printing, global certificate.
GLOB Global Not deliverable, global certificate.
7.1.19.35.8  StrippableIndicator <StrpblInd>
Presence: [0..1]
Definition: Indicates whether the interest is separable from the principal.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.35.9  PositionLimit <PosLmt>
Presence: [0..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 327 February 2025
```

