---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.2.2.20 Issuance <Issnc>", "28.4.2.2.2.20.11 IssuanceDistribution <IssncDstrbtn>", "28.4.2.2.2.20.11.1 Code <Cd>"]
file_pages: [1696]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.2.20.11.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1696 to 1696.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1696

```text
28.4.2.2.2.20.11.1  Code <Cd>
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
28.4.2.2.2.20.11.2  Proprietary <Prtry>
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
28.4.2.2.2.20.12  GoverningLaw <GovngLaw>
Presence: [0..*]
Definition: Jurisdiction (country, county, state, province, city) of the issue.
GoverningLaw <GovngLaw> contains the following Jurisdiction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 1696
   Country <Ctry> [0..1] CodeSet C4 1696
28.4.2.2.2.20.12.1  Identification <Id>
Presence: [0..1]
Definition: Specifies the jurisdiction (county, state, province, city).
Datatype: "Max70Text" on page 3329
28.4.2.2.2.20.12.2  Country <Ctry>
Presence: [0..1]
Definition: Specifies the country.
Impacted by: C4 "Country"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1696 August 2026
```

