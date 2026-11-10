---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.3 CommonFinancialInstrumentAttributes11", "13.1.6.3.18 Issuance <Issnc>", "13.1.6.3.18.10 IssuanceDistribution <IssncDstrbtn>", "13.1.6.3.18.10.1 Code <Cd>"]
file_pages: [344]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.3.18.10.1 Code <Cd>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 344 to 344.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 344

```text
13.1.6.3.18.10.1  Code <Cd>
Presence: [1..1]
Definition: Securities transaction type expressed as an ISO 20022 code.
Datatype: "SecuritiesTransactionType11Code" on page 523
CodeName Name Definition
NSYN NonSyndicated Relates to the issue of medium and short
term paper (CP, CD, MTN, notes.) under
a program and without syndication
arrangement.
SYND SyndicateUnderwriters Relates to the issue of financial
instruments through a syndicate of
underwriters and a lead manager.
13.1.6.3.18.10.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Securities transaction type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.6.3.18.11  GoverningLaw <GovngLaw>
Presence: [0..*]
Definition: Jurisdiction (country, county, state, province, city) of the issue.
GoverningLaw <GovngLaw> contains the following Jurisdiction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 344
   Country <Ctry> [0..1] CodeSet C4 344
13.1.6.3.18.11.1  Identification <Id>
Presence: [0..1]
Definition: Specifies the jurisdiction (county, state, province, city).
Datatype: "Max70Text" on page 535
13.1.6.3.18.11.2  Country <Ctry>
Presence: [0..1]
Definition: Specifies the country.
Impacted by: C4 "Country"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 344 March 2024
```

