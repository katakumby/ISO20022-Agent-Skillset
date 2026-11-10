---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.2 OriginalGroupInformationAndStatus <OrgnlGrpInfAndSts>", "3.4.2.7 StatusReasonInformation <StsRsnInf>", "3.4.2.7.1 Originator <Orgtr>"]
file_pages: [149]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.2.7.1 Originator <Orgtr>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 149 to 149.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 149

```text
On Condition
    /Reason/Code is within DataType <<Code>> ValidationRuleNarrative1Code
 And    /Reason is present
 And    /Reason/Code is present
Following Must be True
    /AdditionalInformation[1] Must be present
3.4.2.7.1  Originator <Orgtr>
Presence: [0..1]
Definition: Party that issues the status.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 149 March 2026
```

