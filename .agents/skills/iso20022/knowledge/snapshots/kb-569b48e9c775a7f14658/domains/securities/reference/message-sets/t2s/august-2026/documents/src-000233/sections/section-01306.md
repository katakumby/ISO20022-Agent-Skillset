---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.3 Debt <Debt>", "32.4.3.1.1.2.3.52 YieldCalculation <YldClctn>", "32.4.3.1.1.2.3.52.5 ValuePeriod <ValPrd>", "32.4.3.1.1.2.3.52.5.2 ToDateTime <ToDtTm>"]
file_pages: [1896]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.3.52.5.2 ToDateTime <ToDtTm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1896 to 1896.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1896

```text
32.4.3.1.1.2.3.52.5.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the range ends.
Datatype: "ISODateTime" on page 3320
32.4.3.1.1.2.3.52.5.3  DateTimeRange <DtTmRg>
Presence: [1..1]
Definition: Range of time between a start date and time and an end date and time.
DateTimeRange <DtTmRg> contains the following elements (see "DateTimePeriod1" on page 2916 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 2916
   ToDateTime <ToDtTm> [1..1] DateTime 2916
32.4.3.1.1.2.3.52.6  CalculationDate <ClctnDt>
Presence: [1..1]
Definition: Clarifies yield irregularities associated with date, for example when it falls on a non-business
day.
Datatype: "ISODateTime" on page 3320
32.4.3.1.1.2.3.53  InterestType <IntrstTp>
Presence: [0..1]
Definition: Indicates whether interest rate is fixed, variable or other.
Datatype: "InterestType3Code" on page 3260
CodeName Name Definition
ZCPN ZeroCoupon Indicates that the type of interest is a
zero coupon.
FIXD Fixed Indicates that the type of interest is fixed.
FLRN FloatingRateNote Indicates that the type of interest is a
floating rate note.
DUAL DualBasis Indicates that the type of interest is a
dual basis.
INDE Index Indicates that the type of interest is
index.
DSCO Discounted Indicates that the type of interest is
discounted.
32.4.3.1.1.2.3.54  InstrumentStructureType <InstrmStrTp>
Presence: [0..1]
Definition: Indicates the type of deal for structured finance.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1896 August 2026
```

