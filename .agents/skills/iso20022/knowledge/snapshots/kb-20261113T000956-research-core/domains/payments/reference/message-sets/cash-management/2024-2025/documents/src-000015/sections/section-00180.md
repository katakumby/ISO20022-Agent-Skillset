---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.4 Payment <Pmt>", "5.4.2.1.3.2.1.4.9 ProcessingValidityTime <PrcgVldtyTm>"]
file_pages: [295]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.4.9 ProcessingValidityTime <PrcgVldtyTm>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 295 to 295.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 295

```text
5.4.2.1.3.2.1.4.9  ProcessingValidityTime <PrcgVldtyTm>
Presence: [0..1]
Definition: Date and time range within which the payment instruction must be processed.
.
ProcessingValidityTime <PrcgVldtyTm> contains one of the following DateTimePeriod1Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 295
Or   ToDateTime <ToDtTm> [1..1] DateTime 295
Or}   DateTimeRange <DtTmRg> [1..1] ± 295
5.4.2.1.3.2.1.4.9.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODateTime" on page 883
5.4.2.1.3.2.1.4.9.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the range ends.
Datatype: "ISODateTime" on page 883
5.4.2.1.3.2.1.4.9.3  DateTimeRange <DtTmRg>
Presence: [1..1]
Definition: Range of time between a start date and time and an end date and time.
DateTimeRange <DtTmRg> contains the following elements (see "DateTimePeriod1" on page 801 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 802
   ToDateTime <ToDtTm> [1..1] DateTime 802
5.4.2.1.3.2.1.4.10  InstructionCopy <InstrCpy>
Presence: [0..1]
Definition: Copy of the original instruction, in free form text.
Datatype: "Max20000Text" on page 888
5.4.2.1.3.2.1.4.11  Type <Tp>
Presence: [0..1]
Definition: Type, or nature, of the payment, such as express payment.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 295 February 2025
```

