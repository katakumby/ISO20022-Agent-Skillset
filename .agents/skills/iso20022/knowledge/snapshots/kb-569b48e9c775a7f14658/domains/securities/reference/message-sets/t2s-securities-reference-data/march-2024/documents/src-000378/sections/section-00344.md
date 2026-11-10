---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.4 CommonFinancialInstrumentAttributes10", "13.1.6.4.34 TEFRARule <TEFRARule>", "13.1.6.4.34.2 Proprietary <Prtry>"]
file_pages: [437]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.4.34.2 Proprietary <Prtry>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 437 to 437.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 437

```text
CodeName Name Definition
RULC C Indicates that the security is issued
under the TEFRA rule C.
RULD D Indicates that the security is issued
under the TEFRA rule D.
13.1.6.4.34.2  Proprietary <Prtry>
Presence: [1..1]
Definition: TEFRA rules expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.6.4.35  SerieNumber <SrNb>
Presence: [0..1]
Definition: Identifies the series number.
Datatype: "Max16Text" on page 533
13.1.6.4.36  Class <Clss>
Presence: [0..1]
Definition: Identifier that links multiple security classes.
Datatype: "Max16Text" on page 533
13.1.6.4.37  WithholdingTaxRegime <WhldgTaxRgm>
Presence: [0..*]
Definition: Amount or percentage of a cash distribution that will be withheld by a tax authority.
WithholdingTaxRegime <WhldgTaxRgm> contains the following SecurityWithHoldingTax1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   WithholdingTaxValue <WhldgTaxVal> [1..1] ± 437
   Country <Ctry> [1..1] CodeSet C4 438
13.1.6.4.37.1  WithholdingTaxValue <WhldgTaxVal>
Presence: [1..1]
Definition: Value of the withholding tax as rate, amount or not specified.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 437 March 2024
```

