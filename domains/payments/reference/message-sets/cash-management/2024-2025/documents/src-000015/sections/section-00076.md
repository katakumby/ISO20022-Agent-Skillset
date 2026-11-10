---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.3 PaymentSearch <PmtSch>", "4.4.2.2.2.2.3.2 RequestedExecutionDate <ReqdExctnDt>", "4.4.2.2.2.2.3.2.1 DateTimeSearch <DtTmSch>"]
file_pages: [145]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.3.2.1 DateTimeSearch <DtTmSch>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 145 to 145.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 145

```text
RequestedExecutionDate <ReqdExctnDt> contains one of the following
DateAndDateTimeSearch3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DateTimeSearch <DtTmSch> [1..1]  145
{Or     FromDateTime <FrDtTm> [1..1] DateTime 145
Or     ToDateTime <ToDtTm> [1..1] DateTime 145
Or}     DateTimeRange <DtTmRg> [1..1] ± 145
Or}   DateSearch <DtSch> [1..1]  146
{Or     FromDate <FrDt> [1..1] Date 146
Or     ToDate <ToDt> [1..1] Date 146
Or     FromToDate <FrToDt> [1..1] ± 146
Or     EqualDate <EQDt> [1..1] Date 146
Or}     NotEqualDate <NEQDt> [1..1] Date 147
4.4.2.2.2.2.3.2.1  DateTimeSearch <DtTmSch>
Presence: [1..1]
Definition: Patterns to search a date time.
DateTimeSearch <DtTmSch> contains one of the following DateTimePeriod1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 145
Or   ToDateTime <ToDtTm> [1..1] DateTime 145
Or}   DateTimeRange <DtTmRg> [1..1] ± 145
4.4.2.2.2.2.3.2.1.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODateTime" on page 883
4.4.2.2.2.2.3.2.1.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the range ends.
Datatype: "ISODateTime" on page 883
4.4.2.2.2.2.3.2.1.3  DateTimeRange <DtTmRg>
Presence: [1..1]
Definition: Range of time between a start date and time and an end date and time.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 145 February 2025
```

