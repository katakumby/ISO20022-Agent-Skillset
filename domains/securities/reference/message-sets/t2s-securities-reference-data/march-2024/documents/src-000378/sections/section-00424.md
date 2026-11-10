---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.2 Message Datatypes", "13.2.2 CodeSet", "13.2.2.27 MaturityRedemptionType1Code"]
file_pages: [519]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.2.2.27 MaturityRedemptionType1Code

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 519 to 519.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 519

```text
13.2.2.27  MaturityRedemptionType1Code
Definition: Indicates the type of redemption at maturity.
Type: CodeSet
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
13.2.2.28  NoReasonCode
Definition: Specifies that there is no reason available.
Type: CodeSet
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
13.2.2.29  Operation1Code
Definition: Indicates the relationship between two variables.
Type: CodeSet
CodeName Name Definition
TILL Till Indicates a range delimited by two
variables.
ORRR Or Indicates either of two variables is valid,
but not both.
ANDD And Indicates that only when both variables
are given, the operation is valid.
13.2.2.30  Operator1Code
Definition: Code containing the operator used to indicate the relationship between a variable and a fixed
value.
Type: CodeSet
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 519 March 2024
```

