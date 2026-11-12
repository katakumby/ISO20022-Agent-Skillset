---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.4 CommonFinancialInstrumentAttributes10", "13.1.6.4.22 SpreadAndBenchmarkCurve <SprdAndBchmkCrv>", "13.1.6.4.22.6 BenchmarkCurvePoint <BchmkCrvPt>"]
file_pages: [432]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.4.22.6 BenchmarkCurvePoint <BchmkCrvPt>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 432 to 432.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 432

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.6.4.22.6  BenchmarkCurvePoint <BchmkCrvPt>
Presence: [0..1]
Definition: Identifies a point on a benchmark curve. The point can be stated via a combination of
maturity month/year and coupon.
Datatype: "Max256Text" on page 534
13.1.6.4.23  PutType <PutTp>
Presence: [0..1]
Definition: Represents the type of put.
PutType <PutTp> contains one of the following PutType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 432
Or}   Proprietary <Prtry> [1..1] ± 432
13.1.6.4.23.1  Code <Cd>
Presence: [1..1]
Definition: Put type expressed as an ISO 20022 code.
Datatype: "PutType1Code" on page 522
CodeName Name Definition
MAND Mandatory Type of execution of the put feature is
mandatory.
OPTI Optional Type of execution of the put feature is
optional.
TWOS Both Type of execution of the put feature
could be optional or mandatory.
13.1.6.4.23.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Put type expressed as a proprietary code.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 432 March 2024
```

