---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.23 CountryCode"]
file_pages: [622]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.23 CountryCode

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 622 to 622.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 622

```text
CodeName Name Definition
do not include client-directed brokerage
arrangements. The U.S. Securities
Exchange Act of 1934, Section 238(e),
created a "safe harbor" to protect
investment managers from claims that
they had breached their fiduciary duties
by using their client commissions to pay
a higher commission than they might
have paid for execution services to
acquire investment research. The SEC
defines soft dollars as: The Commission
has defined soft dollar practices as
arrangements under which products or
services, other than execution of
securities transactions, are obtained
through an adviser or a broker-dealer in
exchange for the direction by the adviser
of client brokerage transactions to the
broker-dealer. An individual or firm must
exercise "investment discretion" over an
account, as defined in Section 3(a)(35)
of the Exchange Act, in order to use
client commissions to obtain research
under Section 28(e) of the Exchange Act
("Section 28(e)").
PERN PercentageOfPrincipal Commission is a percentage of principal.
FLAT FlatFee Commission is a flat fee.
PERU PerUnit Commission is per unit of financial
instrument.
PWCD PercentageCommissionWaivedAsCashDiscount Commission is a percentage commission
waived as cash discount.
PWEU PercentageCommissionWaivedAsAdditionalUnit
s
Commission is a percentage commission
waived as additional units.
BRKR BrokerageRate Brokerage commission.
DFDP DifferentialOrDeferredPayment Differential or deferred payment
commission rate.  .
PBOC PointsPerBondOrContract Commission is based on points per bond
or contract.
7.2.2.23  CountryCode
Definition: Code to identify a country, a dependency, or another area of particular geopolitical interest,
on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).
Type: CodeSet
Format
pattern [A-Z]{2,2}
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 622 February 2025
```

