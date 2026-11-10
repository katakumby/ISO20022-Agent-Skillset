---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.47 Tax", "66.1.47.2 InformativeTax2", "66.1.47.2.5 IndividualTax <IndvTax>", "66.1.47.2.5.1 Type <Tp>", "66.1.47.2.5.1.2 Proprietary <Prtry>"]
file_pages: [5228]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.47.2.5.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5228 to 5228.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5228

```text
CodeName Name Definition
preventing the pre-death transfer of
wealth.
COAX ConsumptionTax Tax that is levied on goods and services
purchased by customers, and is added
to the retail price.
EUTR EUTaxRetention Tax withheld at source in the framework
of the European Directive on taxation of
savings in the form of interest payments.
AKT1 Aktiengewinn1 Share-related profit. This is a tax specific
to the German market. The share-
related-profit gives the fund the
opportunity to pass on to the institutional
investor redeeming fund units certain
tax-free income from equity. The
calculation method is based on the old
Investment Tax Act
(Investmentsteuergesetz).
AKT2 Aktiengewinn2 Share-related profit. This is a tax specific
to the German market. The share-
related-profit gives the fund the
opportunity to pass on to the institutional
investor redeeming fund units certain
tax-free income from equity. The
calculation method is based on the new
Investment Tax Act
(Investmentsteuergesetz).
ZWIS Zwischengewinn Zwischengewinn.
66.1.47.2.5.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of tax expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.47.2.5.2  InformativeAmount <InftvAmt>
Presence: [0..1]
Definition: Amount of money resulting from the calculation of the tax. This amount is provided for
information only.
Impacted by: C1 "ActiveCurrency", C13 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5228 May 2026
```

