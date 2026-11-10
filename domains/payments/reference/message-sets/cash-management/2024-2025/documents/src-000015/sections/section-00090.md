---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.3 PaymentSearch <PmtSch>", "4.4.2.2.2.2.3.4 Status <Sts>", "4.4.2.2.2.2.3.4.1 PaymentInstructionStatus <PmtInstrSts>", "4.4.2.2.2.2.3.4.1.3 PendingAndFinalStatus <PdgAndFnlSts>"]
file_pages: [159]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.3.4.1.3 PendingAndFinalStatus <PdgAndFnlSts>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 159 to 159.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 159

```text
CodeName Name Definition
RJTD Rejected Transaction has been rejected by the
clearing agent.
CAND Cancelled Transaction has been cancelled.
FNLD Finalised Transaction has been successfully
processed by the clearing agent.
Settlement will take place outside of the
system.
4.4.2.2.2.2.3.4.1.3  PendingAndFinalStatus <PdgAndFnlSts>
Presence: [1..1]
Definition: State of a payment instruction at a specified time.
Datatype: "CashPaymentStatus2Code" on page 850
CodeName Name Definition
PDNG Pending The payment is awaiting settlement.
FINL Final The payment has been settled or
stopped.
4.4.2.2.2.2.3.4.2  PaymentInstructionStatusDateTime <PmtInstrStsDtTm>
Presence: [0..1]
Definition: Date and time at which the status was assigned to the transfer.
PaymentInstructionStatusDateTime <PmtInstrStsDtTm> contains one of the following
DateTimePeriod1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 159
Or   ToDateTime <ToDtTm> [1..1] DateTime 159
Or}   DateTimeRange <DtTmRg> [1..1] ± 159
4.4.2.2.2.2.3.4.2.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODateTime" on page 883
4.4.2.2.2.2.3.4.2.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the range ends.
Datatype: "ISODateTime" on page 883
4.4.2.2.2.2.3.4.2.3  DateTimeRange <DtTmRg>
Presence: [1..1]
Definition: Range of time between a start date and time and an end date and time.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 159 February 2025
```

