---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.52 YieldCalculation <YldClctn>", "13.1.2.3.52.5 ValuePeriod <ValPrd>", "13.1.2.3.52.5.2 ToDateTime <ToDtTm>"]
file_pages: [219]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.52.5.2 ToDateTime <ToDtTm>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 219 to 219.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 219

```text
13.1.2.3.52.5.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the range ends.
Datatype: "ISODateTime" on page 529
13.1.2.3.52.5.3  DateTimeRange <DtTmRg>
Presence: [1..1]
Definition: Range of time between a start date and time and an end date and time.
DateTimeRange <DtTmRg> contains the following elements (see "DateTimePeriod1" on page 237 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 237
   ToDateTime <ToDtTm> [1..1] DateTime 237
13.1.2.3.52.6  CalculationDate <ClctnDt>
Presence: [1..1]
Definition: Clarifies yield irregularities associated with date, for example when it falls on a non-business
day.
Datatype: "ISODateTime" on page 529
13.1.2.3.53  InterestType <IntrstTp>
Presence: [0..1]
Definition: Indicates whether interest rate is fixed, variable or other.
Datatype: "InterestType3Code" on page 517
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
13.1.2.3.54  InstrumentStructureType <InstrmStrTp>
Presence: [0..1]
Definition: Indicates the type of deal for structured finance.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 219 March 2024
```

