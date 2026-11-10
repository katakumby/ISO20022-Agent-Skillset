---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.3.2.22 SpreadAndBenchmarkCurve <SprdAndBchmkCrv>", "28.4.2.1.3.2.22.6 BenchmarkCurvePoint <BchmkCrvPt>"]
file_pages: [1518]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.2.22.6 BenchmarkCurvePoint <BchmkCrvPt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1518 to 1518.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1518

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
28.4.2.1.3.2.22.6  BenchmarkCurvePoint <BchmkCrvPt>
Presence: [0..1]
Definition: Identifies a point on a benchmark curve. The point can be stated via a combination of
maturity month/year and coupon.
Datatype: "Max256Text" on page 3327
28.4.2.1.3.2.23  PutType <PutTp>
Presence: [0..1]
Definition: Represents the type of put.
PutType <PutTp> contains one of the following PutType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1518
Or}   Proprietary <Prtry> [1..1] ± 1518
28.4.2.1.3.2.23.1  Code <Cd>
Presence: [1..1]
Definition: Put type expressed as an ISO 20022 code.
Datatype: "PutType1Code" on page 3282
CodeName Name Definition
MAND Mandatory Type of execution of the put feature is
mandatory.
OPTI Optional Type of execution of the put feature is
optional.
TWOS Both Type of execution of the put feature
could be optional or mandatory.
28.4.2.1.3.2.23.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Put type expressed as a proprietary code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1518 August 2026
```

