---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.8 Charge", "66.1.8.2 CostsAndCharges2", "66.1.8.2.2 IndividualCostOrCharge <IndvCostOrChrg>", "66.1.8.2.2.1 CostType <CostTp>"]
file_pages: [4443, 4444, 4445, 4446, 4447]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.8.2.2.1 CostType <CostTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4443 to 4447.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4443

```text
• ExAnteOrExPost2Guideline
If ExAnteOrExPost contains POST then CostType must be an ex post cost or charge.
• SignAmount1Rule
If Amount is not present, then Sign is not allowed.
On Condition
    /Amount is absent
Following Must be True
    /Sign Must be absent
• SignAmount2Rule
Sign must only be used to express a negative value for Amount.
66.1.8.2.2.1  CostType <CostTp>
Presence: [1..1]
Definition: Type of cost or charge.
CostType <CostTp> contains one of the following ChargeType8Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4443
Or}   Proprietary <Prtry> [1..1] ± 4448
66.1.8.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Cost or charge expressed as a code.
Datatype: "InvestmentFundMiFIDFee2Code" on page 5313
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
Investment Funds - Maintenance 2025 - 2026 4443 May 2026
```

## File page 4444

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
Investment Funds - Maintenance 2025 - 2026 4444 May 2026
```

## File page 4445

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
Investment Funds - Maintenance 2025 - 2026 4445 May 2026
```

## File page 4446

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
Investment Funds - Maintenance 2025 - 2026 4446 May 2026
```

## File page 4447

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
Investment Funds - Maintenance 2025 - 2026 4447 May 2026
```

