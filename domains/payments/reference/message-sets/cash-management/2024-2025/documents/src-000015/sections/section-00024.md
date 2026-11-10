---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 camt.003.001.08 GetAccountV08", "2.4 Message Building Blocks", "2.4.2 AccountQueryDefinition <AcctQryDef>", "2.4.2.2 AccountCriteria <AcctCrit>", "2.4.2.2.2 NewCriteria <NewCrit>", "2.4.2.2.2.3 ReturnCriteria <RtrCrit>", "2.4.2.2.2.3.3 TypeIndicator <TpInd>"]
file_pages: [43]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.003.001.08"]
---

# 2.4.2.2.2.3.3 TypeIndicator <TpInd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 43 to 43.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 43

```text
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.2.3.3  TypeIndicator <TpInd>
Presence: [0..1]
Definition: Indicates whether the account type is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.2.3.4  MultilateralLimitIndicator <MulLmtInd>
Presence: [0..1]
Definition: Indicates whether the multilateral limit is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.2.3.5  MultilateralBalanceReturnCriteria <MulBalRtrCrit>
Presence: [0..1]
Definition: Defines the criteria used to report on a multilateral balance.
MultilateralBalanceReturnCriteria <MulBalRtrCrit> contains the following
CashBalanceReturnCriteria2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TypeIndicator <TpInd> [1..1] Indicator 43
   StatusIndicator <StsInd> [1..1] Indicator 43
   ValueDateIndicator <ValDtInd> [1..1] Indicator 44
   ProcessingDateIndicator <PrcgDtInd> [1..1] Indicator 44
   NumberOfPaymentsIndicator <NbOfPmtsInd> [1..1] Indicator 44
2.4.2.2.2.3.5.1  TypeIndicator <TpInd>
Presence: [1..1]
Definition: Indicates whether the balance type is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.2.3.5.2  StatusIndicator <StsInd>
Presence: [1..1]
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 43 February 2025
```

