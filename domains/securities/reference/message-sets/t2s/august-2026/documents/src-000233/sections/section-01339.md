---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.4 Derivative <Deriv>", "32.4.3.1.1.2.4.2 Option <Optn>", "32.4.3.1.1.2.4.2.11 VersionNumber <VrsnNb>"]
file_pages: [1938]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.4.2.11 VersionNumber <VrsnNb>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1938 to 1938.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1938

```text
Definition: Assignment method expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
32.4.3.1.1.2.4.2.11  VersionNumber <VrsnNb>
Presence: [0..1]
Definition: Number allocated by options exchanges to record that an option has undergone a change in
its contract specifications (particularly adjustment of the strike price).
Datatype: "Number" on page 3324
32.4.3.1.1.2.4.2.12  ExpiryLocation <XpryLctn>
Presence: [0..1]
Definition: Financial center where option expires.
Datatype: "Max4AlphaNumericText" on page 3328
32.4.3.1.1.2.4.2.13  Standardisation <Stdstn>
Presence: [0..1]
Definition: Specifies whether the terms of the security (underlying instruments, expiration date, contract
size) are defined according to the exchange specifications or whether they can be user defined.
Standardisation <Stdstn> contains one of the following Standardisation3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..*] CodeSet 1938
Or}   Proprietary <Prtry> [1..1] ± 1939
32.4.3.1.1.2.4.2.13.1  Code <Cd>
Presence: [1..*]
Definition: Standardisation expressed as an ISO 20022 code.
Datatype: "Standardisation1Code" on page 3304
CodeName Name Definition
FLEX Flexible Derivatives defined according to
exchange specifications, but certain
characteristics can be user defined.
NSTA NonStandardised Custom-made instrument between two
parties. Underlying
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1938 August 2026
```

