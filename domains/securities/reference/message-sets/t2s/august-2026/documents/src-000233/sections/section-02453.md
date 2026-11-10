---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.91 MaturityRedemptionType1Code"]
file_pages: [3264]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.91 MaturityRedemptionType1Code

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3264 to 3264.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3264

```text
82.2.2.91  MaturityRedemptionType1Code
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
82.2.2.92  ModificationProcessingStatus1Code
Definition: Specifies the status of a cancellation request.
Type: CodeSet
CodeName Name Definition
PACK Accepted Modification request has been
acknowledged for further processing by
the account servicer.
REJT Rejected Modification has been rejected for further
processing.
MODC Completed Modification has been completed.
DEND Denied Modification will not be executed.
MODP Pending Modification is pending. It is not known
at this time whether modified can be
executed.
REPR InRepair Modification request is in repair.
82.2.2.93  MovementResponseType1Code
Definition: Specifies the type of movement response to be returned.
Type: CodeSet
CodeName Name Definition
FULL Full Response will include full details on the
movements reported.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3264 August 2026
```

