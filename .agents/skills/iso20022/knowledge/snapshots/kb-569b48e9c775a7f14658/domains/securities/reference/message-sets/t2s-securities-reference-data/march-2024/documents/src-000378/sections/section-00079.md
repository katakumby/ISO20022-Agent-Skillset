---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["10 reda.030.001.01 SecurityDeletionStatusAdviceV01", "10.4 Message Building Blocks", "10.4.4 SupplementaryData <SplmtryData>"]
file_pages: [128]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.030.001.01"]
---

# 10.4.4 SupplementaryData <SplmtryData>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 128 to 128.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 128

```text
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus72Choice" on page 501 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1]  502
     Reason <Rsn> [0..*] ± C1 502
Or   PendingProcessing <PdgPrcg> [1..1] ± 502
Or   Rejected <Rjctd> [1..1] ± 503
Or   Completed <Cmpltd> [1..1]  503
     Reason <Rsn> [0..*] ± C1 503
Or}   Proprietary <Prtry> [1..1] ± 504
10.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C7 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 486 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 486
   Envelope <Envlp> [1..1] (External Schema) 486
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.030.001.01 SecurityDeletionStatusAdviceV01
Target2-Securities - Securities Reference Data 128 March 2024
```

