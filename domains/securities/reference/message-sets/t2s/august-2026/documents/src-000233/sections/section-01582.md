---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["49 reda.029.001.01 SecurityMaintenanceStatusAdviceV01", "49.4 Message Building Blocks", "49.4.4 SupplementaryData <SplmtryData>"]
file_pages: [2207]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.029.001.01"]
---

# 49.4.4 SupplementaryData <SplmtryData>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2207 to 2207.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2207

```text
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus72Choice" on page 3163 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1]  3164
     Reason <Rsn> [0..*] ± C6 3164
Or   PendingProcessing <PdgPrcg> [1..1] ± 3164
Or   Rejected <Rjctd> [1..1] ± 3165
Or   Completed <Cmpltd> [1..1]  3165
     Reason <Rsn> [0..*] ± C6 3165
Or}   Proprietary <Prtry> [1..1] ± 3166
49.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C7 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 3011 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 3011
   Envelope <Envlp> [1..1] (External Schema) 3012
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.029.001.01
SecurityMaintenanceStatusAdviceV01
Target2-Securities 2207 August 2026
```

