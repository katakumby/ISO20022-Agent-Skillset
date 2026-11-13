---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["17 camt.018.001.05 GetBusinessDayInformationV05", "17.4 Message Building Blocks", "17.4.2 BusinessDayInformationQueryDefinition <BizDayInfQryDef>", "17.4.2.2 Criteria <Crit>", "17.4.2.2.2 NewCriteria <NewCrit>", "17.4.2.2.2.3 ReturnCriteria <RtrCrit>", "17.4.2.2.2.3.1 SystemDateIndicator <SysDtInd>"]
file_pages: [533]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.018.001.05"]
---

# 17.4.2.2.2.3.1 SystemDateIndicator <SysDtInd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 533 to 533.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 533

```text
ReturnCriteria <RtrCrit> contains the following BusinessDayReturnCriteria2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemDateIndicator <SysDtInd> [0..1] Indicator 533
   SystemStatusIndicator <SysStsInd> [0..1] Indicator 533
   SystemCurrencyIndicator <SysCcyInd> [0..1] Indicator 533
   ClosurePeriodIndicator <ClsrPrdInd> [0..1] Indicator 533
   EventIndicator <EvtInd> [0..1] Indicator 534
   SessionPeriodIndicator <SsnPrdInd> [0..1] Indicator 534
   EventTypeIndicator <EvtTpInd> [0..1] Indicator 534
17.4.2.2.2.3.1  SystemDateIndicator <SysDtInd>
Presence: [0..1]
Definition: Indicates whether the system date is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
17.4.2.2.2.3.2  SystemStatusIndicator <SysStsInd>
Presence: [0..1]
Definition: Indicates whether the system status is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
17.4.2.2.2.3.3  SystemCurrencyIndicator <SysCcyInd>
Presence: [0..1]
Definition: Indicates whether the system currency is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
17.4.2.2.2.3.4  ClosurePeriodIndicator <ClsrPrdInd>
Presence: [0..1]
Definition: Indicates whether the closure information is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
Approved by the Payments SEG on 04 February 2025 camt.018.001.05 GetBusinessDayInformationV05
Cash Management - Maintenance 2024 - 2025 533 February 2025
```

