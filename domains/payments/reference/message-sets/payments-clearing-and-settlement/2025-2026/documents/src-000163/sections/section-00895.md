---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.11 Miscellaneous", "10.1.11.1 OriginalGroupInformation27", "10.1.11.1.5 OriginalControlSum <OrgnlCtrlSum>"]
file_pages: [1190]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.11.1.5 OriginalControlSum <OrgnlCtrlSum>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1190 to 1190.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1190

```text
10.1.11.1.5  OriginalControlSum <OrgnlCtrlSum>
Presence: [0..1]
Definition: Total of all individual amounts included in the original message, irrespective of currencies.
Datatype: "DecimalNumber" on page 1242
10.1.11.2  Authorisation1Choice
Definition: Provides the details on the user identification or any user key that allows to check if the
initiating party is allowed to issue the transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1190
Or}   Proprietary <Prtry> [1..1] Text 1190
10.1.11.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the authorisation, in a coded form.
Datatype: "Authorisation1Code" on page 1225
CodeName Name Definition
AUTH PreAuthorisedFile Indicates a file has been pre authorised
or approved within the originating
customer environment and no further
approval is required.
FDET FileLevelAuthorisationDetails Indicates that a file requires additional
file level approval, with the ability to view
both the payment information block and
supporting customer credit transaction
detail.
FSUM FileLevelAuthorisationSummary Indicates that a file requires additional
file level approval, with the ability to view
only the payment information block level
information.
ILEV InstructionLevelAuthorisation Indicates that a file requires all customer
transactions to be authorised or
approved.
10.1.11.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the authorisation, in a free text form.
Datatype: "Max128Text" on page 1244
10.1.11.3  SupplementaryData1
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1190 March 2026
```

