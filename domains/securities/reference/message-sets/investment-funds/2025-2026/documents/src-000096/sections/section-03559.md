---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.27 Market", "66.1.27.2 PlaceOfTradeIdentification4Choice", "66.1.27.2.1 Country <Ctry>"]
file_pages: [4809]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.27.2.1 Country <Ctry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4809 to 4809.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4809

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Country <Ctry> [1..1] CodeSet C12 4809
Or   Exchange <Xchg> [1..1] IdentifierSet 4809
Or   Party <Pty> [1..1] IdentifierSet C4 4809
Or}   OverTheCounter <OverTheCntr> [1..1] Text 4809
66.1.27.2.1  Country <Ctry>
Presence: [1..1]
Definition: Country in which the transaction is executed.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.27.2.2  Exchange <Xchg>
Presence: [1..1]
Definition: Exchange at which the transaction is executed.
Datatype: "MICIdentifier" on page 5396
66.1.27.2.3  Party <Pty>
Presence: [1..1]
Definition: Party's location at which the transaction is executed.
Impacted by: C4 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 5389
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
66.1.27.2.4  OverTheCounter <OverTheCntr>
Presence: [1..1]
Definition: Place at which the Over-the-Counter (OTC) transaction is executed.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4809 May 2026
```

