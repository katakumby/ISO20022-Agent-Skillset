---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.111 InRepairStatusReason1Code"]
file_pages: [5311, 5312]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.111 InRepairStatusReason1Code

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5311 to 5312.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5311

```text
66.2.2.111  InRepairStatusReason1Code
Definition: Specifies the reason for a In Repair status.
Type: CodeSet
CodeName Name Definition
COMA CommercialAgreement Order has been accepted and
centralised before the cut off, but with
different sales agreement than the one
provided in the order.
66.2.2.112  Insurance1Code
Definition: Specifies the type of insurance.
Type: CodeSet
CodeName Name Definition
LIFE LifeInsurance Life insurance.
PDIS PermanentDisabilityInsurance Permanent disability insurance.
66.2.2.113  IntendedOrActual2Code
Definition: Specifies if a charge or cost is intended (ex ante) or actual (post ante).
Type: CodeSet
CodeName Name Definition
ANTE ExAnte Ex ante (intended).
POST ExPost Ex post (actual).
66.2.2.114  InvestmentAccountCategory1Code
Definition: Specifies the investment account category.
Type: CodeSet
CodeName Name Definition
MAND MandateAccount Account is fully managed by the financial
institution, that is, an investor gives a
'mandate' to the financial institution to
execute a mutually agreed investment
strategy on its behalf.
RETA RetailAccount Account is a standard account managed
by the investor. The investor issues
instructions for the account to the
financial institution.
66.2.2.115  InvestmentFundFee2Code
Definition: Type of service for which a charge is asked or paid.
Type: CodeSet
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5311 May 2026
```

## File page 5312

```text
CodeName Name Definition
BEND BackEndLoad Fee paid by the investor to the fund or
fund management company when
redeeming.
FEND FrontEndLoad Fee paid by the investor to the fund or
fund management company when
subscribing.
TRAN TransferFee In investment funds, a fee charged for
the transfer of ownership of an
investment fund.
POST PostageCharge Charge paid for the postage.
REGF RegulatoryFee Fee charged by a regulatory authority,
for example, securities and exchange
fees.
SHIP ShippingCharge Charge for shipping, including the
insurance of securities.
SPCN SpecialConcessions Fees, drawdown, or other reduction from
or in addition to the deal price.
66.2.2.116  InvestmentFundFee3Code
Definition: Specifies the type of service for which a fee e is asked or paid.
Type: CodeSet
CodeName Name Definition
BEND BackEndLoad Fee paid by the investor to the fund or
fund management company when
redeeming.
BRKF BrokerageFee Fee paid to a broker for services
provided.
CDSC ContingentDeferredSalesCharge Deferred sales charge.
CBCH CorrespondentBankCharge In investment funds, the charge of the
correspondent bank for transferring
money.
DLEV DilutionLevy In investment funds, a charge payable
by the investor covering bid-offer
spreads and dealing charges for the
underlying investments. The dilution levy
is paid to the fund for the benefit of other
unit holders.
FEND FrontEndLoad Fee paid by the investor to the fund or
fund management company when
subscribing.
INIT InitialCharge Charge paid at the time of the first
subscription.
PREM Premium In investment funds, pre-arranged
addition to the trade amount based on
the published net asset value.
CHAR ServiceProvisionFee Fee paid by the investor to a distributor/
intermediary or other service provider for
the provision of financial services.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5312 May 2026
```

