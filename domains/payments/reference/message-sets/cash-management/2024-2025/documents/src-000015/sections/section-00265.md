---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["8 camt.009.001.08 GetLimitV08", "8.4 Message Building Blocks", "8.4.2 LimitQueryDefinition <LmtQryDef>", "8.4.2.2 LimitCriteria <LmtCrit>", "8.4.2.2.2 NewCriteria <NewCrit>", "8.4.2.2.2.3 ReturnCriteria <RtrCrit>", "8.4.2.2.2.3.1 StartDateTimeIndicator <StartDtTmInd>"]
file_pages: [389, 390]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.009.001.08"]
---

# 8.4.2.2.2.3.1 StartDateTimeIndicator <StartDtTmInd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 389 to 390.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 389

```text
ReturnCriteria <RtrCrit> contains the following LimitReturnCriteria2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StartDateTimeIndicator <StartDtTmInd> [0..1] Indicator 389
   StatusIndicator <StsInd> [0..1] Indicator 389
   UsedAmountIndicator <UsdAmtInd> [0..1] Indicator 389
   UsedPercentageIndicator <UsdPctgInd> [0..1] Indicator 389
8.4.2.2.2.3.1  StartDateTimeIndicator <StartDtTmInd>
Presence: [0..1]
Definition: Indicates whether the limit start date time is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
8.4.2.2.2.3.2  StatusIndicator <StsInd>
Presence: [0..1]
Definition: Indicates whether the limit status is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
8.4.2.2.2.3.3  UsedAmountIndicator <UsdAmtInd>
Presence: [0..1]
Definition: Indicates whether the limit used amount is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
8.4.2.2.2.3.4  UsedPercentageIndicator <UsdPctgInd>
Presence: [0..1]
Definition: Indicates whether the limit used percentage is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
8.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Approved by the Payments SEG on 04 February 2025 camt.009.001.08 GetLimitV08
Cash Management - Maintenance 2024 - 2025 389 February 2025
```

## File page 390

```text
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C9 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 815 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 816
   Envelope <Envlp> [1..1] (External Schema) 816
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Payments SEG on 04 February 2025 camt.009.001.08 GetLimitV08
Cash Management - Maintenance 2024 - 2025 390 February 2025
```

