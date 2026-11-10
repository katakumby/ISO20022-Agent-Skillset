---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.4 ReturnCriteria <RtrCrit>", "4.4.2.2.2.4.1 PaymentToReturnCriteria <PmtToRtrCrit>", "4.4.2.2.2.4.1.2 MemberIdentificationIndicator <MmbIdInd>"]
file_pages: [195]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.4.1.2 MemberIdentificationIndicator <MmbIdInd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 195 to 195.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 195

```text
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.1.2  MemberIdentificationIndicator <MmbIdInd>
Presence: [0..1]
Definition: Indicates whether the member identification is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.1.3  CountryIdentificationIndicator <CtryIdInd>
Presence: [0..1]
Definition: Indicates whether the country identification is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.1.4  AccountIdentificationIndicator <AcctIdInd>
Presence: [0..1]
Definition: Indicates whether the account identification is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.2  PaymentFromReturnCriteria <PmtFrRtrCrit>
Presence: [0..1]
Definition: Origin of the payment (be it a member or a system or both).
PaymentFromReturnCriteria <PmtFrRtrCrit> contains the following SystemReturnCriteria2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemIdentificationIndicator <SysIdInd> [0..1] Indicator 195
   MemberIdentificationIndicator <MmbIdInd> [0..1] Indicator 196
   CountryIdentificationIndicator <CtryIdInd> [0..1] Indicator 196
   AccountIdentificationIndicator <AcctIdInd> [0..1] Indicator 196
4.4.2.2.2.4.2.1  SystemIdentificationIndicator <SysIdInd>
Presence: [0..1]
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 195 February 2025
```

