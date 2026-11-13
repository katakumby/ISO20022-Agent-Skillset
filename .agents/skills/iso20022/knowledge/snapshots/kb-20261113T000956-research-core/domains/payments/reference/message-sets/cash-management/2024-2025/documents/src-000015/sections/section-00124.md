---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.4 ReturnCriteria <RtrCrit>", "4.4.2.2.2.4.2 PaymentFromReturnCriteria <PmtFrRtrCrit>", "4.4.2.2.2.4.2.2 MemberIdentificationIndicator <MmbIdInd>"]
file_pages: [196]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.4.2.2 MemberIdentificationIndicator <MmbIdInd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 196 to 196.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 196

```text
Definition: Indicates whether the system identification is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.2.2  MemberIdentificationIndicator <MmbIdInd>
Presence: [0..1]
Definition: Indicates whether the member identification is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.2.3  CountryIdentificationIndicator <CtryIdInd>
Presence: [0..1]
Definition: Indicates whether the country identification is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.2.4  AccountIdentificationIndicator <AcctIdInd>
Presence: [0..1]
Definition: Indicates whether the account identification is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.3  AccountCashEntryReturnCriteria <AcctCshNtryRtrCrit>
Presence: [0..1]
Definition: Defines the criteria used to report on the cash entry.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 196 February 2025
```

