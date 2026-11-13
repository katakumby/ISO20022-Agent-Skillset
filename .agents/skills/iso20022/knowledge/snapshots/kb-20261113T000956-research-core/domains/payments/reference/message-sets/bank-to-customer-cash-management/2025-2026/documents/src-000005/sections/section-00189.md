---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks"]
file_pages: [282]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
preceding_topic_continuations: [{"constraint_ids": ["C21", "C22", "C23", "C24", "C25", "C26", "C27", "C28", "C29", "C30", "C31"], "until_heading": "3.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 282, "topic": "3.3 Constraints", "reference_path": "domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000005/sections/section-00188.md"}]
---

# 3.4 Message Building Blocks

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 282 to 282.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 282, C21–C31 before **3.4 Message Building Blocks** continue [3.3 Constraints](section-00188.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 282

```text
C21 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C22 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C23 MessageOrStatementPaginationRule
MessagePagination may be present or StatementPagination may be present, but not both.
Following Must be True
    /GroupHeader/MessagePagination Must be absent
 Or    /Statement[*]/StatementPagination Must be absent
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
3.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
3.4.1 GroupHeader <GrpHdr>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
282 March 2026
```

