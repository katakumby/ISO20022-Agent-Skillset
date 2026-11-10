---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.7 InvestmentAccountOwnershipInformation16", "66.1.24.7.20 MailType <MailTp>"]
file_pages: [4612]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.7.20 MailType <MailTp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4612 to 4612.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4612

```text
Constraints
• ValidationByTable
Must be a valid terrestrial language.
66.1.24.7.20  MailType <MailTp>
Presence: [0..1]
Definition: Method used for postal mailing.
MailType <MailTp> contains one of the following elements (see "MailType1Choice" on page 5020 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5020
Or}   Proprietary <Prtry> [1..1] ± 5020
66.1.24.7.21  CountryAndResidentialStatus <CtryAndResdtlSts>
Presence: [0..1]
Definition: Country and residential status of the organisation or individual person.
CountryAndResidentialStatus <CtryAndResdtlSts> contains the following elements (see
"CountryAndResidentialStatusType2" on page 5004 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [1..1] CodeSet C12 5004
   ResidentialStatus <ResdtlSts> [1..1] CodeSet 5004
66.1.24.7.22  MonetaryWealth <MntryWlth>
Presence: [0..1]
Definition: Annual wealth of the individual person or share capital value of the legal entity and date on
which the annual wealth of the individual person was registered or declared or the date the stock value
of the organisation was registered.
MonetaryWealth <MntryWlth> contains the following elements (see "DateAndAmount1" on page 4343
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [1..1] Date 4343
   Amount <Amt> [1..1] Amount C1, C13 4344
66.1.24.7.23  EquityValue <EqtyVal>
Presence: [0..1]
Definition: Amount of total assets minus liabilities of the individual person or the amount of the
difference between assets and liabilities plus rights over obligations (net equity) of the organisation and
the date on which the equity value was registered.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4612 May 2026
```

