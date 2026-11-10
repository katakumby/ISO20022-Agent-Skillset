---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.4 Derivative <Deriv>", "32.4.3.1.1.2.4.2 Option <Optn>", "32.4.3.1.1.2.4.2.5 ConversionPeriod <ConvsPrd>"]
file_pages: [1935]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.4.2.5 ConversionPeriod <ConvsPrd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1935 to 1935.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1935

```text
Definition: Minimum quantity of securities that must be exercised.
MinimumExercisableQuantity <MinExrcblQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
32.4.3.1.1.2.4.2.5  ConversionPeriod <ConvsPrd>
Presence: [0..1]
Definition: Period during which a convertible security may be converted according to the terms of the
issue.
ConversionPeriod <ConvsPrd> contains one of the following DateTimePeriod1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 1935
Or   ToDateTime <ToDtTm> [1..1] DateTime 1935
Or}   DateTimeRange <DtTmRg> [1..1] ± 1935
32.4.3.1.1.2.4.2.5.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODateTime" on page 3320
32.4.3.1.1.2.4.2.5.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the range ends.
Datatype: "ISODateTime" on page 3320
32.4.3.1.1.2.4.2.5.3  DateTimeRange <DtTmRg>
Presence: [1..1]
Definition: Range of time between a start date and time and an end date and time.
DateTimeRange <DtTmRg> contains the following elements (see "DateTimePeriod1" on page 2916 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 2916
   ToDateTime <ToDtTm> [1..1] DateTime 2916
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1935 August 2026
```

