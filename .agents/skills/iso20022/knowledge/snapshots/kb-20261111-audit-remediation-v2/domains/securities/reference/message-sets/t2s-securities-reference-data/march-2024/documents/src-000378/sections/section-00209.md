---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.2 CommonFinancialInstrumentAttributes12", "13.1.6.2.42 RedemptionType <RedTp>"]
file_pages: [287]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.2.42 RedemptionType <RedTp>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 287 to 287.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 287

```text
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification1" on
page 478 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 478
   SchemeName <SchmeNm> [0..1] Text 478
   Issuer <Issr> [0..1] Text 478
13.1.6.2.42  RedemptionType <RedTp>
Presence: [0..1]
Definition: Indicates the type of redemption at maturity.
RedemptionType <RedTp> contains one of the following MaturityRedemptionType3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 287
Or}   Proprietary <Prtry> [1..1] ± 287
13.1.6.2.42.1  Code <Cd>
Presence: [1..1]
Definition: Maturity redemption type expressed as an ISO 20022 code.
Datatype: "MaturityRedemptionType1Code" on page 519
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
13.1.6.2.42.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Maturity redemption type expressed as a proprietary code.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 287 March 2024
```

