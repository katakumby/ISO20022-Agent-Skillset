---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.40 RedemptionType <RedTp>"]
file_pages: [1994]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.40 RedemptionType <RedTp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1994 to 1994.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1994

```text
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification1" on
page 2966 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   SchemeName <SchmeNm> [0..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
32.4.3.1.1.3.40  RedemptionType <RedTp>
Presence: [0..1]
Definition: Indicates the type of redemption at maturity.
RedemptionType <RedTp> contains one of the following MaturityRedemptionType3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1994
Or}   Proprietary <Prtry> [1..1] ± 1994
32.4.3.1.1.3.40.1  Code <Cd>
Presence: [1..1]
Definition: Maturity redemption type expressed as an ISO 20022 code.
Datatype: "MaturityRedemptionType1Code" on page 3264
CodeName Name Definition
FRED FinalRedemption Indicates that the type of redemption at
maturity is final.
PRNR PartialRedemptionWithoutReduction Indicates that the type of redemption at
maturity is partial without reduction.
PRWR PartialRedemptionWithReduction Indicates that the type of redemption at
maturity is partial with reduction.
RNDM DrawingAtRandom Indicates that the type of redemption at
maturity is drawing at random.
PRRA DrawingProRata Indicates that the type of redemption at
maturity is drawing pro-rata.
CALL Call Indicates that the type of redemption at
maturity is call.
PUUT Put Indicates that the type of redemption at
maturity is put.
32.4.3.1.1.3.40.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Maturity redemption type expressed as a proprietary code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1994 August 2026
```

