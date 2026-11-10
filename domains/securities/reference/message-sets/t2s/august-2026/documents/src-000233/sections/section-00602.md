---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "27.4.2.3.34 TEFRARule <TEFRARule>", "27.4.2.3.34.2 Proprietary <Prtry>"]
file_pages: [787]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.3.34.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 787 to 787.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 787

```text
CodeName Name Definition
RULC C Indicates that the security is issued
under the TEFRA rule C.
RULD D Indicates that the security is issued
under the TEFRA rule D.
27.4.2.3.34.2  Proprietary <Prtry>
Presence: [1..1]
Definition: TEFRA rules expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
27.4.2.3.35  SerieNumber <SrNb>
Presence: [0..1]
Definition: Identifies the series number.
Datatype: "Max16Text" on page 3326
27.4.2.3.36  Class <Clss>
Presence: [0..1]
Definition: Identifier that links multiple security classes.
Datatype: "Max16Text" on page 3326
27.4.2.3.37  WithholdingTaxRegime <WhldgTaxRgm>
Presence: [0..*]
Definition: Amount or percentage of a cash distribution that will be withheld by a tax authority.
WithholdingTaxRegime <WhldgTaxRgm> contains the following SecurityWithHoldingTax1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   WithholdingTaxValue <WhldgTaxVal> [1..1] ± 787
   Country <Ctry> [1..1] CodeSet C4 788
27.4.2.3.37.1  WithholdingTaxValue <WhldgTaxVal>
Presence: [1..1]
Definition: Value of the withholding tax as rate, amount or not specified.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 787 August 2026
```

