---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.2 InvestmentAccountType1Choice"]
file_pages: [4556]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.2 InvestmentAccountType1Choice

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4556 to 4556.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4556

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.24.2  InvestmentAccountType1Choice
Definition: Choice of formats for the specification of the investment account type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4556
Or}   Proprietary <Prtry> [1..1] ± 4556
66.1.24.2.1  Code <Cd>
Presence: [1..1]
Definition: Investment account type expressed as a code.
Datatype: "FundCashAccount2Code" on page 5304
CodeName Name Definition
CASH CashAccount Cash account.
CPFO PensionFundOrdinary Central Provident Fund (CPF) ordinary
account.
CPFS PensionFundSpecial Central Provident Fund (CPF) special
account.
SRSA RetirementScheme Supplementary Retirement Scheme
(SRS) account.
66.1.24.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Investment account type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4556 May 2026
```

