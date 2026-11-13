---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.3 PaymentSearch <PmtSch>", "4.4.2.2.2.2.3.13 ProcessingValidityTime <PrcgVldtyTm>", "4.4.2.2.2.2.3.13.1 FromDateTime <FrDtTm>"]
file_pages: [166]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.3.13.1 FromDateTime <FrDtTm>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 166 to 166.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 166

```text
ProcessingValidityTime <PrcgVldtyTm> contains one of the following DateTimePeriod1Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 166
Or   ToDateTime <ToDtTm> [1..1] DateTime 166
Or}   DateTimeRange <DtTmRg> [1..1] ± 166
4.4.2.2.2.2.3.13.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODateTime" on page 883
4.4.2.2.2.2.3.13.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the range ends.
Datatype: "ISODateTime" on page 883
4.4.2.2.2.2.3.13.3  DateTimeRange <DtTmRg>
Presence: [1..1]
Definition: Range of time between a start date and time and an end date and time.
DateTimeRange <DtTmRg> contains the following elements (see "DateTimePeriod1" on page 801 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 802
   ToDateTime <ToDtTm> [1..1] DateTime 802
4.4.2.2.2.2.3.14  Instruction <Instr>
Presence: [0..*]
Definition: Further information related to the processing of the payment instruction. The instruction can
relate to a level of service between the bank and the customer, or give instructions to and for specific
parties in the payment chain.
Datatype: "Instruction1Code" on page 859
CodeName Name Definition
PBEN PayTheBeneficiary (Ultimate) creditor to be paid only after
verification of identity.
TTIL TimeTill Payment instruction is valid and eligible
for execution until the date and time
stipulated. Otherwise, the payment
instruction will be rejected.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 166 February 2025
```

