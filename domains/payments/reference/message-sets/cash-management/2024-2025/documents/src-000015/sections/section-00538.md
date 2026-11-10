---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["30 camt.069.001.05 GetStandingOrderV05", "30.4 Message Building Blocks", "30.4.2 StandingOrderQueryDefinition <StgOrdrQryDef>", "30.4.2.2 StandingOrderCriteria <StgOrdrCrit>", "30.4.2.2.2 NewCriteria <NewCrit>", "30.4.2.2.2.3 ReturnCriteria <RtrCrit>", "30.4.2.2.2.3.4 ResponsiblePartyIndicator <RspnsblPtyInd>"]
file_pages: [703]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.069.001.05"]
---

# 30.4.2.2.2.3.4 ResponsiblePartyIndicator <RspnsblPtyInd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 703 to 703.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 703

```text
Definition: Indicates whether the system member identification is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
30.4.2.2.2.3.4  ResponsiblePartyIndicator <RspnsblPtyInd>
Presence: [0..1]
Definition: Indicates whether the responsible party identification is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
30.4.2.2.2.3.5  CurrencyIndicator <CcyInd>
Presence: [0..1]
Definition: Indicates whether the account currency is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
30.4.2.2.2.3.6  DebtorAccountIndicator <DbtrAcctInd>
Presence: [0..1]
Definition: Indicates whether the account type is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
30.4.2.2.2.3.7  CreditorAccountIndicator <CdtrAcctInd>
Presence: [0..1]
Definition: Indicates whether the multilateral limit is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
30.4.2.2.2.3.8  AssociatedPoolAccount <AssoctdPoolAcct>
Presence: [0..1]
Definition: Indicates whether the associated pool account is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
Approved by the Payments SEG on 04 February 2025 camt.069.001.05 GetStandingOrderV05
Cash Management - Maintenance 2024 - 2025 703 February 2025
```

