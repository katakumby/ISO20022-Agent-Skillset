---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.117 InvestmentFundMiFIDFee2Code"]
file_pages: [5313, 5314, 5315, 5316, 5317]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.117 InvestmentFundMiFIDFee2Code

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5313 to 5317.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5313

```text
CodeName Name Definition
SWIT Switch In investment funds, charge related to a
switch transaction.
UCIC UCITSCommission Charges paid by the investor to the fund
company for subscription and
redemption orders.
COMM Commission Amount paid out by the fund to a third
party.
SHIP ShippingCharge Charge for shipping, including the
insurance of securities.
POST PostageCharge Charge paid for the postage.
CDPL CommissionDePlacement Amount of cash due to an intermediary
for selling a product, or services, to a
third party.
ADDF AdditionalFee Additional fee not covered by another
fee type.
REGF RegulatoryFee Fee charged by a regulatory authority,
for example, securities and exchange
fees.
PENA Penalty Fee charged to the investor for early
redemption of the fund.
NTWK NetworkFee Network fee assigned to a transaction on
a DLT network.
66.2.2.117  InvestmentFundMiFIDFee2Code
Definition: Specifies a type of cost or charge.
Type: CodeSet
CodeName Name Definition
BORF BorrowingCostFund Financing costs related to borrowing for
the purposes of gearing expressed as a
percentage of the NAV. When used in
reference to MiFID, this is in the scope of
the European MiFID Template (EMT)
reference 07105 and 08045.
DIS2 DistributionFee Distribution fee. This fee is included in
the total on going costs and is not
included in the management fee. It is
only applicable if the product has this
feature. The cost reported should reflect
the current running distribution fee.
When used in reference to MiFID, this is
in the scope of the European MiFID
Template (EMT) reference 07120 and
08060 and this a percentage of the NAV
of the financial instrument expressed in
annualised terms (rate of cost deduction
to be applied).
FES3 GrossOneOffEntryCostStructured Gross one-off entry cost for a structured
product. When used in reference to
MiFID, this is in the scope of the
European MiFID Template (EMT)
reference 08010 and may be specified
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5313 May 2026
```

## File page 5314

```text
CodeName Name Definition
as an actual amount or a percentage of
the reference value, EMT reference
08110 or 08120, and should only
incorporate manufacturer costs (that is,
the cost of the financial instrument) and
distributor costs upfront when known by
the manufacturer. It should, however, not
include distribution fees added on top of
the product price by distributors that is
out of control of the manufacturer.
FEND GrossOneOffMaximumEntryCostNonAcquired Gross one-off maximum entry cost not
acquired to the fund. When used in
reference to MiFID, this is in the scope of
the European MiFID Template (EMT)
reference 07020 and is a percentage of
the amount to be invested. This fee is
paid by the investor to the fund or fund
management company. This is indicative
and should be adapted by the distributor
according to the agreement with the
asset manager.
FES2 GrossOneOffMaximumEntryCostStructured Gross maximum one-off entry cost for a
structured product. When used in
reference to MiFID, this is in the scope of
the European MiFID Template (EMT)
reference 07020 or 08120, and is the
'ask price' or 'fair value'. It may be
specified as an actual amount or a
percentage of the reference value, EMT
reference 07150, and should only
incorporate manufacturer costs (that is,
the cost of the financial instrument) and
distributor costs upfront when known by
the manufacturer. It should, however, not
include distribution fees added on top of
the product price by distributors that are
out of control of the manufacturer.
GOC1 GrossOngoingCosts Gross on-going costs. When used in
reference to MiFID, this is in the scope of
the European MiFID Template (EMT)
reference 07100 and 08030 and is a
percentage of the NAV of the financial
product, expressed in annualised terms
(rate of cost deduction to be applied).
This includes management fees and
distribution fees and excludes all
transaction costs, incidental costs and
performance fees. Costs reported should
reflect current running ongoing costs.
The gross on-going costs is expressed
as a percentage of the NAV of the
financial instrument per annum.
GOCS GrossOngoingCostsStructured Gross on-going costs for a structured
product. When used in reference to
MiFID, this is in the scope of the
European MiFID Template (EMT)
reference 07100 and 08030 and is
expressed as a percentage of the NAV
or currency and amount for an absolute
quotation of the financial product in
annualised terms related to the
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5314 May 2026
```

## File page 5315

```text
CodeName Name Definition
reference value, EMT reference 07150
or 07155 or 08110.
INCF IncidentalCosts Fee that covers incidental costs. When
used in reference to MiFID, this is in the
scope of the European MiFID Template
(EMT) reference 07140 and 08080 and
is expressed as a percentage of the
NAV. Includes performance fees and
other costs.
INCS IncidentalCostsStructured Fee that covers incidental costs for a
structured product. When used in
reference to MiFID, this is in the scope of
the European MiFID Template (EMT)
reference 07140 and 08080 and is
expressed as a percentage of the NAV
or a currency and amount for an
absolute quotation of the financial
product in annualised terms related to
the reference value, EMT reference
07150 or 07155 and 08110.
MNF1 ManagementFee Management fee paid to an investment
manager for services. When used in
reference to MiFID, this is in the scope of
the European MiFID Template (EMT)
reference 07110 and 08050 and is a
percentage of the NAV of the financial
product expressed in annualised terms
(rate of cost deduction to be applied).
These fees are included in total ongoing
costs and are fees used by distributors
to calculate retrocession fees. The costs
reported should reflect current running
management costs.
MANS ManagementFeeStructured Management fee for a structured
product. When used in reference to
MiFID, this is in the scope of the
European MiFID Template (EMT)
reference 07110 and 08050 and is
expressed as a percentage of the NAV
or a currency and amount for an
absolute quotation of the financial
product in annualised terms related to
the reference value, EMT reference
07150 or 07155 or 08110.
NET2 NetOneOffEntryCostExPostStructured Net one-off entry cost for a structured
product. When used in reference to
MiFID, this is in the scope of the
European MiFID Template (EMT)
reference 08015 and is minus the
upfront distribution fee. The cost
reported is a net disclosure and
therefore the upfront distributor fee is
equal to the difference between the
gross one-off entry cost (EMT reference
08010) and the net one-off entry (EMT
reference 08015).
NESF NetOneOffEntryCostNonAcquiredStructuredFun
d
Net one-off entry cost for a structured
fund. When used in reference to MiFID,
this is in the scope of the European
MiFID Template (EMT) reference 07025.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5315 May 2026
```

## File page 5316

```text
CodeName Name Definition
This is expressed as a percentage of the
amount to be invested.
NETO NetOneOffEntryCostStructuredNonAcquired Net one-off entry cost for a structured
product. When used in reference to
MiFID, this is in the scope of the
European MiFID Template (EMT)
reference 07025 and is minus the
upfront distribution fee. The cost
reported is a net disclosure and
therefore the upfront distributor fee is
equal to the difference between the one-
off entry cost (EMT reference 07020)
and the net one-off entry (EMT reference
07025).
NRAM NotionalReferenceAmount Notional reference amount. When used
in reference to MiFID, this is in the scope
of the European MiFID Template (EMT)
reference 07155 and 08120. This is the
amount expressed as a number of
currency units to which a unit disclosed
ex-post cost is based and to which a
percentage disclosed cost should be
multiplied in order to retrieve the unit
cost.
OOEA OneOffEntryCostAcquired Percentage of the NAV. When used in
reference to MiFID, this is in the scope of
the European MiFID Template (EMT)
reference 08025.
OOSF OneOffExitCostPriorStructuredProductFund One-off exit cost prior to the
recommended holding period (RHP).
When used in reference to MiFID, this is
in the scope of the European MiFID
Template (EMT) reference 07090 and
may be specified as a percentage of the
amount to be divested.
OOSS OneOffExitCostPriorStructuredSecurities One-off exit cost prior to the
recommended holding period (RHP).
When used in reference to MiFID, this is
in the scope of the European MiFID
Template (EMT) reference 07090 and is
specified as an actual amount or a
percentage of the reference value, EMT
reference 07150 or 07155.
BENS OneOffExitCostStructured One off exit cost for a structured product.
When used in reference to MiFID, this is
in the scope of the European MiFID
Template (EMT) reference 08020 and
when expressed as a percentage, this is
a percentage of the reference value,
EMT reference 08110 or 08120.
ENAC OneOffMaximumEntryCostAcquired Maximum cost of the one-off entry fee.
When used in reference to MiFID, this is
in the scope of the European MiFID
Template (EMT) reference 07040 and is
the subscription fees acquired to the
fund. It is not included in the one off
entry cost 07020. This maximum one-off
entry cost acquired to the fund is
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5316 May 2026
```

## File page 5317

```text
CodeName Name Definition
specified as a percentage of the amount
to be invested.
ENFX OneOffMaximumEntryCostFixedAmountItaly Maximum one-off entry cost fixed
amount. When used in reference to
MiFID, this is in the scope of the
European MiFID Template (EMT)
reference 07030 and is a flat fee defined
by the fund or fund management
company. This is indicative and should
be adapted by the distributor according
to the relationship been the fund and the
distribution. This cost is not taken into
account in the gross one-off maximum
entry cost (FEND), EMT reference
07020.
EXAC OneOffMaximumExitCostAcquired Maximum cost of the one-off exit fee
acquired to the fund. When used in
reference to MiFID, this is in the scope of
the European MiFID Template (EMT)
reference 07070. It is not included in the
one off maximum exit cost EMT
reference 07050. This is paid by the
investor to the fund or fund management
company. This is a percentage of the
NAV.
ENBX OneOffMaximumExitCostFixedAmountItaly Maximum one-off exit cost, a maximum
fixed amount per redemption. When
used in reference to MiFID, this is in the
scope of the European MiFID Template
(EMT) reference 07060 and is flat fee
defined by the fund or fund management
company. It is indicative and should be
adapted distributor according to the
relationship been the fund and the
distribution. This cost is not taken in
account in the one-off maximum exit cost
EMT reference 07050.
BEND OneOffMaximumExitCostNonAcquired Maximum cost of the one-off exit fee not
acquired to the fund that could happen at
a certain time during the life of the
product. This is a percentage of the
NAV. When used in reference to MiFID,
this is in the scope of the European
MiFID Template (EMT) reference 07050.
PENO OneOffTypicalExitCost One-off typical exit current exit cost
linked to the recommended holding
period (RHP) or time to maturity. When
used in reference to MiFID, this is in the
scope of the European MiFID Template
(EMT) reference 07080 and are the
'normal' fees if the client holds the
product until maturity or during the RHP.
Example: a product with a 5 year
maturity has exit costs of:
- 4% after 1 and 2 years
- 3% after 3 years
- 1% after 4 years
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5317 May 2026
```

