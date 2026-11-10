---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.13 CurrencyDesignation1"]
file_pages: [4831]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.13 CurrencyDesignation1

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4831 to 4831.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4831

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.28.13  CurrencyDesignation1
Definition: Information about the designation of a currency.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CurrencyDesignation <CcyDsgnt> [0..1] CodeSet 4831
   Location <Lctn> [0..1] CodeSet C12 4831
   AdditionalInformation <AddtlInf> [0..1] Text 4831
66.1.28.13.1  CurrencyDesignation <CcyDsgnt>
Presence: [0..1]
Definition: Specifies whether the currency is settled offshore or onshore.
Datatype: "CurrencyDesignation1Code" on page 5293
CodeName Name Definition
ONSH Onshore Onshore.
OFFS Offshore Offshore.
66.1.28.13.2  Location <Lctn>
Presence: [0..1]
Definition: Offshore location of the currency.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.28.13.3  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the off-shore currency.
Datatype: "Max350Text" on page 5403
66.1.28.14  FATCAForm1Choice
Definition: Choice of formats for the type of Foreign Account Tax Compliance Act (FATCA) form.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4831 May 2026
```

