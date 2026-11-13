---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.8 Commission", "7.1.8.1 Commission25", "7.1.8.1.6 TotalVATAmount <TtlVATAmt>"]
file_pages: [255, 256]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.8.1.6 TotalVATAmount <TtlVATAmt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 255 to 256.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 255

```text
TotalCommission <TtlComssn> contains the following elements (see "AmountAndDirection29" on
page 228 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C10 228
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 229
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C10 229
   ForeignExchangeDetails <FXDtls> [0..1] ± 229
7.1.8.1.6  TotalVATAmount <TtlVATAmt>
Presence: [0..1]
Definition: Amount that results of the calculation of VAT on net fees, according to the transaction current
tariffs.
Impacted by: C1 "ActiveCurrency", C9 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 611
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
7.1.8.1.7  VATRate <VATRate>
Presence: [0..1]
Definition: Specifies the VAT rate.
Datatype: "BaseOneRate" on page 666
7.1.8.2  CommissionType6Choice
Definition: Choice between a code or a data source scheme to determine the commission type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 255
Or}   Proprietary <Prtry> [1..1] ± 257
7.1.8.2.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 255 February 2025
```

## File page 256

```text
Definition: Commission type is identified using a code.
Datatype: "CommissionType9Code" on page 621
CodeName Name Definition
CLDI ClientDirected Commission is as per client agreement.
STEP StepOut Commission for a step-out trade,
charged by the step-out broker.
SOFT SoftDollar Commission designated by the broker
for third party services. The soft dollar
arrangement refers to an arrangement
wherean investment manager directs
transactions to a brokerand, in
exchange, the broker provides
brokerage and research services to the
investment manager. Soft dollar
arrangements include proprietary and
third party research arrangements, but
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
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 256 February 2025
```

