---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.3 PaymentSearch <PmtSch>", "4.4.2.2.2.2.3.11 PaymentType <PmtTp>", "4.4.2.2.2.2.3.11.2 Proprietary <Prtry>"]
file_pages: [165]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.3.11.2 Proprietary <Prtry>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 165 to 165.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 165

```text
4.4.2.2.2.2.3.11.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Payment type that is not included in a predefined list.
Datatype: "Max35Text" on page 889
4.4.2.2.2.2.3.12  Priority <Prty>
Presence: [0..*]
Definition: Urgency or order of importance that the originator would like the recipient of the payment
instruction to apply to the processing of the payment instruction.
Priority <Prty> contains one of the following Priority1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 165
Or}   Proprietary <Prtry> [1..1] Text 165
4.4.2.2.2.2.3.12.1  Code <Cd>
Presence: [1..1]
Definition: Priority code, in a coded form.
Datatype: "Priority5Code" on page 871
CodeName Name Definition
HIGH High Priority level is high.
LOWW Low Priority level is low.
NORM Normal Priority level is normal.
URGT Urgent Priority level is urgent (highest priority
possible).
4.4.2.2.2.2.3.12.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Priority code bilaterally agreed between parties.
Datatype: "Max35Text" on page 889
4.4.2.2.2.2.3.13  ProcessingValidityTime <PrcgVldtyTm>
Presence: [0..*]
Definition: Date and time range within which the payment instruction must be processed.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 165 February 2025
```

