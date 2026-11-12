---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.47 AlternatePartyIdentification7", "66.1.30.47.3 AlternateIdentification <AltrnId>"]
file_pages: [5045]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.47.3 AlternateIdentification <AltrnId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5045 to 5045.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5045

```text
Definition: Country in which a person resides (the place of a person's home). In the case of a company,
it is the country from which the affairs of that company are directed.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.30.47.3  AlternateIdentification <AltrnId>
Presence: [1..1]
Definition: Alternate identification for a party.
Datatype: "Max35Text" on page 5403
66.1.31 Payment
66.1.31.1  SourceOfCash1Choice
Definition: Choice of formats for the source of the cash.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5045
Or}   Proprietary <Prtry> [1..1] ± 5046
66.1.31.1.1  Code <Cd>
Presence: [1..1]
Definition: Source of cash expressed as a code.
Datatype: "SourceOfCash1Code" on page 5364
CodeName Name Definition
ALMY Alimony Income as a result of alimony.
CASH CashProceeds Income is cash proceeds from
customers.
COMP Compensation Income is from compensation received.
EMIN EmployeeIncome Employee income.
GIFT Gift Income was a cash gift.
INHE Inheritance Cash from an inheritance.
INLQ InsurancePremiumLiquidation Income from the liquidation of an
insurance premium.
REST RealEstateSale Income from the sale of real estate.
REDM Redemption Redemption of an investment fund.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5045 May 2026
```

