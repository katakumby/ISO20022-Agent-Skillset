---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.10 LetterIntent1", "66.1.28.10.1 LetterIntentReference <LttrInttRef>"]
file_pages: [4825]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.10.1 LetterIntentReference <LttrInttRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4825 to 4825.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4825

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LetterIntentReference <LttrInttRef> [1..1] Text 4825
   Amount <Amt> [0..1] Amount C1 4825
   StartDate <StartDt> [0..1] Date 4825
   EndDate <EndDt> [0..1] Date 4825
66.1.28.10.1  LetterIntentReference <LttrInttRef>
Presence: [1..1]
Definition: Reference of a letter of intent program, in which sales commissions are reduced based on
the aggregate of a customer's actual purchase and anticipated purchases, over a specific period of
time, and as agreed by the customer.
Datatype: "Max35Text" on page 5403
66.1.28.10.2  Amount <Amt>
Presence: [0..1]
Definition: Amount stated on the letter of intent.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.28.10.3  StartDate <StartDt>
Presence: [0..1]
Definition: Start date stated on the letter of intent.
Datatype: "ISODate" on page 5388
66.1.28.10.4  EndDate <EndDt>
Presence: [0..1]
Definition: End date stated on the letter of intent.
Datatype: "ISODate" on page 5388
66.1.28.11  Notification2
Definition: Information about the type of notification required.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4825 May 2026
```

