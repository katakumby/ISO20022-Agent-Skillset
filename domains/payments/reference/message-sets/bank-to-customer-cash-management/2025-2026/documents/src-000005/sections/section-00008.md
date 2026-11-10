---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks"]
file_pages: [23]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4 Message Building Blocks

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 23 to 23.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 23

```text
C21 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C22 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C23 MessageOrReportPaginationRule
MessagePagination may be present or ReportPagination may be present, but not both.
Following Must be True
    /GroupHeader/MessagePagination Must be absent
 Or    /Report[*]/ReportPagination Must be absent
This constraint is defined at the MessageDefinition level.
C24 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C25 PaymentTypeOrLocalInstrumentRule
PaymentTypeInformation or LocalInstrument must be absent, both can be absent.
C26 ReferenceGuideline
At least one reference should be present to identify the underlying transaction(s).
C27 RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
C28 ReturnReasonRule
If Reason/Code is equal to NARR, then AdditionalInformation must be present.
C29 SupplementaryDataRule
The SupplementaryData building block at message level must not be used to provide additional
information about a transaction. The SupplementaryData element at transaction level should be
used for that purpose.
This constraint is defined at the MessageDefinition level.
C30 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C31 UnderlyingAllocationGuideline
UnderlyingAllocation may only be present if bilaterally agreed.
2.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
2.4.1 GroupHeader <GrpHdr>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
23 March 2026
```

