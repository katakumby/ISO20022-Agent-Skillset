---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.8 Units <Units>"]
file_pages: [2828]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.8 Units <Units>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2828 to 2828.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2828

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
49.4.5.9.8  Units <Units>
Presence: [1..1]
Definition: Quantity of units or digital tokens.
Units <Units> contains one of the following Unit1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   UnitsNumber <UnitsNb> [1..1] Quantity 2828
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 2828
49.4.5.9.8.1  UnitsNumber <UnitsNb>
Presence: [1..1]
Definition: Quantity of units.
Datatype: "DecimalNumber" on page 5400
49.4.5.9.8.2  DigitalTokenUnit <DgtlTknUnit>
Presence: [1..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 5400
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2828 May 2026
```

