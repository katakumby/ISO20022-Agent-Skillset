---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "43.4.5.9.7 Units <Units>"]
file_pages: [1947]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.9.7 Units <Units>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1947 to 1947.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1947

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
43.4.5.9.7  Units <Units>
Presence: [1..1]
Definition: Quantity of units or digital tokens.
Units <Units> contains one of the following Unit1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   UnitsNumber <UnitsNb> [1..1] Quantity 1947
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1947
43.4.5.9.7.1  UnitsNumber <UnitsNb>
Presence: [1..1]
Definition: Quantity of units.
Datatype: "DecimalNumber" on page 5400
43.4.5.9.7.2  DigitalTokenUnit <DgtlTknUnit>
Presence: [1..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 5400
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1947 May 2026
```

