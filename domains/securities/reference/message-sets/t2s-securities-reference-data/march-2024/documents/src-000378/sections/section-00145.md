---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.26 ExtendibleIndicator <XtndblInd>"]
file_pages: [207]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.26 ExtendibleIndicator <XtndblInd>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 207 to 207.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 207

```text
13.1.2.3.26  ExtendibleIndicator <XtndblInd>
Presence: [0..1]
Definition: Indicates whether the security is extendible,eg, repayment may be extended or maturity
changed.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.2.3.27  ExtendiblePeriod <XtndblPrd>
Presence: [0..1]
Definition: Period during which a date might be extended.
ExtendiblePeriod <XtndblPrd> contains one of the following DateTimePeriod1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 207
Or   ToDateTime <ToDtTm> [1..1] DateTime 207
Or}   DateTimeRange <DtTmRg> [1..1] ± 207
13.1.2.3.27.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODateTime" on page 529
13.1.2.3.27.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the range ends.
Datatype: "ISODateTime" on page 529
13.1.2.3.27.3  DateTimeRange <DtTmRg>
Presence: [1..1]
Definition: Range of time between a start date and time and an end date and time.
DateTimeRange <DtTmRg> contains the following elements (see "DateTimePeriod1" on page 237 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 237
   ToDateTime <ToDtTm> [1..1] DateTime 237
13.1.2.3.28  VariableRateIndicator <VarblRateInd>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 207 March 2024
```

