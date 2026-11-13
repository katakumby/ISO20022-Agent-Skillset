---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 camt.003.001.08 GetAccountV08", "2.4 Message Building Blocks", "2.4.2 AccountQueryDefinition <AcctQryDef>", "2.4.2.2 AccountCriteria <AcctCrit>", "2.4.2.2.2 NewCriteria <NewCrit>", "2.4.2.2.2.3 ReturnCriteria <RtrCrit>", "2.4.2.2.2.3.5 MultilateralBalanceReturnCriteria <MulBalRtrCrit>", "2.4.2.2.2.3.5.3 ValueDateIndicator <ValDtInd>"]
file_pages: [44]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.003.001.08"]
---

# 2.4.2.2.2.3.5.3 ValueDateIndicator <ValDtInd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 44 to 44.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 44

```text
Definition: Indicates whether the balance status is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.2.3.5.3  ValueDateIndicator <ValDtInd>
Presence: [1..1]
Definition: Indicates whether the value date is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.2.3.5.4  ProcessingDateIndicator <PrcgDtInd>
Presence: [1..1]
Definition: Indicates whether the processing date is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.2.3.5.5  NumberOfPaymentsIndicator <NbOfPmtsInd>
Presence: [1..1]
Definition: Indicates whether the number of payment is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.2.3.6  BilateralLimitIndicator <BilLmtInd>
Presence: [0..1]
Definition: Indicates whether the bilateral limit is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.2.3.7  BilateralBalanceReturnCriteria <BilBalRtrCrit>
Presence: [0..1]
Definition: Defines the criteria used to report on a bilateral balance.
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 44 February 2025
```

