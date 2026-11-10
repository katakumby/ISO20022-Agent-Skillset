---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.4 Derivative <Deriv>", "27.4.2.2.4.2 Option <Optn>", "27.4.2.2.4.2.6 OptionStyle <OptnStyle>"]
file_pages: [734]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.4.2.6 OptionStyle <OptnStyle>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 734 to 734.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 734

```text
27.4.2.2.4.2.6  OptionStyle <OptnStyle>
Presence: [0..1]
Definition: Specifies how an option can be exercised (American, European, Bermudan).
OptionStyle <OptnStyle> contains one of the following OptionStyle1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 734
Or}   Proprietary <Prtry> [1..1] ± 734
27.4.2.2.4.2.6.1  Code <Cd>
Presence: [1..1]
Definition: Option style is defined using a code.
Datatype: "OptionStyle1Code" on page 3266
CodeName Name Definition
AMER American Option can be exercised before or on
expiry date.
EURO European Option that can be exercised on expiry
date only.
BERM Bermudan Option that can be exercised on multiple
discrete dates prior to, or on expiry date.
ASIA Asian Option where the payoff is not
determined by the underlying price at
maturity but by the average underlying
price over some pre-set period of time.
CANA Canary Option whose exercise style lies
somewhere between European options
and Bermudan options. The holder can
exercise the option at quarterly dates,
but not before a set time period (typically
one year) has elapsed.
27.4.2.2.4.2.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Option style is defined using a data source scheme.
Proprietary <Prtry> contains the following elements (see "GenericIdentification13" on page 2968 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2969
   SchemeName <SchmeNm> [0..1] Text 2969
   Issuer <Issr> [1..1] Text 2969
27.4.2.2.4.2.7  OptionType <OptnTp>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 734 August 2026
```

