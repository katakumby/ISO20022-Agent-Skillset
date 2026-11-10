---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.4 ReturnCriteria <RtrCrit>", "4.4.2.2.2.4.3 AccountCashEntryReturnCriteria <AcctCshNtryRtrCrit>", "4.4.2.2.2.4.3.1 EntryReferenceIndicator <NtryRefInd>"]
file_pages: [197]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.4.3.1 EntryReferenceIndicator <NtryRefInd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 197 to 197.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 197

```text
AccountCashEntryReturnCriteria <AcctCshNtryRtrCrit> contains the following
AccountCashEntryReturnCriteria3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EntryReferenceIndicator <NtryRefInd> [0..1] Indicator 197
   AccountTypeIndicator <AcctTpInd> [0..1] Indicator 197
   EntryAmountIndicator <NtryAmtInd> [0..1] Indicator 197
   AccountCurrencyIndicator <AcctCcyInd> [0..1] Indicator 197
   EntryStatusIndicator <NtryStsInd> [0..1] Indicator 198
   EntryDateIndicator <NtryDtInd> [0..1] Indicator 198
   AccountServicerIndicator <AcctSvcrInd> [0..1] Indicator 198
   AccountOwnerIndicator <AcctOwnrInd> [0..1] Indicator 198
4.4.2.2.2.4.3.1  EntryReferenceIndicator <NtryRefInd>
Presence: [0..1]
Definition: Indicates whether the entry reference is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.3.2  AccountTypeIndicator <AcctTpInd>
Presence: [0..1]
Definition: Indicates whether the account type is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.3.3  EntryAmountIndicator <NtryAmtInd>
Presence: [0..1]
Definition: Indicates whether the entry amount is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.3.4  AccountCurrencyIndicator <AcctCcyInd>
Presence: [0..1]
Definition: Indicates whether the account currency is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 197 February 2025
```

