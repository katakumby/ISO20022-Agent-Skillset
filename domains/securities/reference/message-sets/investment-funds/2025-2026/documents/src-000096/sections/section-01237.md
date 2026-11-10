---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.7 AmountOrUnitsOrPercentage <AmtOrUnitsOrPctg>"]
file_pages: [1740]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.7 AmountOrUnitsOrPercentage <AmtOrUnitsOrPctg>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1740 to 1740.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1740

```text
BeneficiaryDetails <BnfcryDtls> contains the following elements (see "IndividualPerson32" on
page 5075 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 5076
   BirthDate <BirthDt> [0..1] Date 5076
   CountryAndResidentialStatus <CtryAndResdtlSts> [0..1] ± 5076
   OtherIdentification <OthrId> [0..*]  5076
     Identification <Id> [1..1] Text 5077
     IdentificationType <IdTp> [1..1]  5077
{Or       Code <Cd> [1..1] CodeSet 5077
Or}       Proprietary <Prtry> [1..1] ± 5078
     Issuer <Issr> [0..1] Text 5078
Constraints
• PersonElementRule
One of the elements (Name, BirthDate, CountryAndResidentialStatus, OtherIdentification) must be
present.
41.4.4.8.7  AmountOrUnitsOrPercentage <AmtOrUnitsOrPctg>
Presence: [1..1]
Definition: Amount of money or the number of units or percentage to be redeemed for the redemption
order.
AmountOrUnitsOrPercentage <AmtOrUnitsOrPctg> contains one of the following
FinancialInstrumentQuantity48Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   UnitsNumber <UnitsNb> [1..1] Quantity 1740
Or   GrossAmount <GrssAmt> [1..1] Amount C4, C9 1741
Or   NetAmount <NetAmt> [1..1] Amount C4, C9 1741
Or   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1741
Or}   HoldingsRedemptionRate <HldgsRedRate> [1..1] Rate 1742
41.4.4.8.7.1  UnitsNumber <UnitsNb>
Presence: [1..1]
Definition: Number of investment fund units redeemed.
Datatype: "DecimalNumber" on page 5400
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1740 May 2026
```

