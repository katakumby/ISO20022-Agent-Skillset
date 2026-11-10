---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.13 ForeignExchangeDetails <FXDtls>"]
file_pages: [2587]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.13 ForeignExchangeDetails <FXDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2587 to 2587.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2587

```text
BeneficiaryDetails <BnfcryDtls> contains the following elements (see "IndividualPerson31" on
page 5058 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 5058
   BirthDate <BirthDt> [0..1] Date 5059
   CountryAndResidentialStatus <CtryAndResdtlSts> [0..1] ± 5059
   BeneficiaryCertificationCompletion
<BnfcryCertfctnCmpltn>
[0..1] CodeSet 5059
   OtherIdentification <OthrId> [0..*]  5059
     Identification <Id> [1..1] Text 5060
     IdentificationType <IdTp> [1..1]  5060
{Or       Code <Cd> [1..1] CodeSet 5060
Or}       Proprietary <Prtry> [1..1] ± 5061
     Issuer <Issr> [0..1] Text 5061
Constraints
• PersonElementRule
One of the elements (Name, BirthDate, CountryAndResidentialStatus,
BeneficiaryCertificationCompletion, OtherIdentification) must be present.
47.4.4.8.13  ForeignExchangeDetails <FXDtls>
Presence: [0..1]
Definition: Information needed to process a currency exchange or conversion.
How the exchange rate is expressed determines which currency is the Unit Currency and Quoted
Currency. If the amounts concerned are EUR 1000 and USD 1300, the exchange rate may be
expressed as per either of the following examples:
EXAMPLE 1
UnitCurrency EUR
QuotedCurrency USD
ExchangeRate 1.300
EXAMPLE 2
UnitCurrency USD
QuotedCurrency EUR
ExchangeRate 0.769.
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2587 May 2026
```

