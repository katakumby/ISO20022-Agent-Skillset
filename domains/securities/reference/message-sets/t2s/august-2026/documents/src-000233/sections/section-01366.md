---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.18 Issuance <Issnc>", "32.4.3.1.1.3.18.10 IssuanceDistribution <IssncDstrbtn>", "32.4.3.1.1.3.18.10.1 Code <Cd>"]
file_pages: [1975]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.18.10.1 Code <Cd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1975 to 1975.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1975

```text
32.4.3.1.1.3.18.10.1  Code <Cd>
Presence: [1..1]
Definition: Securities transaction type expressed as an ISO 20022 code.
Datatype: "SecuritiesTransactionType11Code" on page 3295
CodeName Name Definition
NSYN NonSyndicated Relates to the issue of medium and short
term paper (CP, CD, MTN, notes.) under
a program and without syndication
arrangement.
SYND SyndicateUnderwriters Relates to the issue of financial
instruments through a syndicate of
underwriters and a lead manager.
32.4.3.1.1.3.18.10.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Securities transaction type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
32.4.3.1.1.3.18.11  GoverningLaw <GovngLaw>
Presence: [0..*]
Definition: Jurisdiction (country, county, state, province, city) of the issue.
GoverningLaw <GovngLaw> contains the following Jurisdiction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 1975
   Country <Ctry> [0..1] CodeSet C4 1975
32.4.3.1.1.3.18.11.1  Identification <Id>
Presence: [0..1]
Definition: Specifies the jurisdiction (county, state, province, city).
Datatype: "Max70Text" on page 3329
32.4.3.1.1.3.18.11.2  Country <Ctry>
Presence: [0..1]
Definition: Specifies the country.
Impacted by: C4 "Country"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1975 August 2026
```

