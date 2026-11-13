---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.1.2.34 TEFRARule <TEFRARule>", "28.4.2.1.1.2.34.2 Proprietary <Prtry>"]
file_pages: [1147]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.2.34.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1147 to 1147.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1147

```text
CodeName Name Definition
RULC C Indicates that the security is issued
under the TEFRA rule C.
RULD D Indicates that the security is issued
under the TEFRA rule D.
28.4.2.1.1.2.34.2  Proprietary <Prtry>
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
28.4.2.1.1.2.35  SerieNumber <SrNb>
Presence: [0..1]
Definition: Identifies the series number.
Datatype: "Max16Text" on page 3326
28.4.2.1.1.2.36  Class <Clss>
Presence: [0..1]
Definition: Identifier that links multiple security classes.
Datatype: "Max16Text" on page 3326
28.4.2.1.1.2.37  WithholdingTaxRegime <WhldgTaxRgm>
Presence: [0..*]
Definition: Amount or percentage of a cash distribution that will be withheld by a tax authority.
WithholdingTaxRegime <WhldgTaxRgm> contains the following SecurityWithHoldingTax1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   WithholdingTaxValue <WhldgTaxVal> [1..1] ± 1147
   Country <Ctry> [1..1] CodeSet C4 1148
28.4.2.1.1.2.37.1  WithholdingTaxValue <WhldgTaxVal>
Presence: [1..1]
Definition: Value of the withholding tax as rate, amount or not specified.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1147 August 2026
```

