---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.53 CountryCode"]
file_pages: [5290]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.53 CountryCode

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5290 to 5290.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5290

```text
CodeName Name Definition
a tender offer is to take control of the
target company.
BONU BonusIssue Event is a bonus issue or scrip issue or
capitalisation issue. Security holders are
awarded additional assets free of
payment from the issuer in proportion to
their holding. A bonus issue is typically
represented by shares, rights or
warrants. Nominal value doesn't change.
Holder may be offered choice of form.
RHDI RightsDistribution Event is the distribution of rights to
shareholders, in proportion to their equity
holding.
EXRI CallOnRights Event is a call or exercise on nil-paid
securities or rights resulting from a rights
distribution (RHDI). This is to be used for
the second event in those cases where
the rights issue is dealt with in two
events, the first event being the rights
distribution (RHDI).
CHAN Change Event is a generic change. For example,
a change in the terms of an issue, a
change in the identification of a security,
change of a board lot, a change from
global to definitive.
REDO Redenomination Event by which the unit (currency and/or
nominal) of a financial instrument is
restated, eg, the debt in a national
currency is restated in euro.
EXOP ExchangeOption Event is an option for the shareholders
to exchange their securities for other
securities and/or cash. Exchange
options are mentioned in the terms and
conditions of a security and are valid
during the whole lifetime of a security.
EXOF ExchangeOffer Event is an exchange offer or capital
reorganisation.
It is an offer to shareholders to exchange
their holdings for other securities and/or
cash. Exchange offers are usually
voluntary involving the exchange of
outstanding security for a different
security or securities and/or cash.
DECR DecreaseInValue Event is a reduction of the share capital
and face value of a single share. The
number of the circulating shares remains
unchanged. It may include a capital pay-
out to shareholder.
66.2.2.53  CountryCode
Definition: Code to identify a country, a dependency, or another area of particular geopolitical interest,
on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).
Type: CodeSet
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5290 May 2026
```

