---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 camt.003.001.08 GetAccountV08", "2.4 Message Building Blocks", "2.4.2 AccountQueryDefinition <AcctQryDef>", "2.4.2.2 AccountCriteria <AcctCrit>", "2.4.2.2.2 NewCriteria <NewCrit>", "2.4.2.2.2.3 ReturnCriteria <RtrCrit>", "2.4.2.2.2.3.7 BilateralBalanceReturnCriteria <BilBalRtrCrit>", "2.4.2.2.2.3.7.1 TypeIndicator <TpInd>"]
file_pages: [45]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.003.001.08"]
---

# 2.4.2.2.2.3.7.1 TypeIndicator <TpInd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 45 to 45.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 45

```text
BilateralBalanceReturnCriteria <BilBalRtrCrit> contains the following CashBalanceReturnCriteria2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TypeIndicator <TpInd> [1..1] Indicator 45
   StatusIndicator <StsInd> [1..1] Indicator 45
   ValueDateIndicator <ValDtInd> [1..1] Indicator 45
   ProcessingDateIndicator <PrcgDtInd> [1..1] Indicator 45
   NumberOfPaymentsIndicator <NbOfPmtsInd> [1..1] Indicator 46
2.4.2.2.2.3.7.1  TypeIndicator <TpInd>
Presence: [1..1]
Definition: Indicates whether the balance type is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.2.3.7.2  StatusIndicator <StsInd>
Presence: [1..1]
Definition: Indicates whether the balance status is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.2.3.7.3  ValueDateIndicator <ValDtInd>
Presence: [1..1]
Definition: Indicates whether the value date is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.2.3.7.4  ProcessingDateIndicator <PrcgDtInd>
Presence: [1..1]
Definition: Indicates whether the processing date is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 45 February 2025
```

