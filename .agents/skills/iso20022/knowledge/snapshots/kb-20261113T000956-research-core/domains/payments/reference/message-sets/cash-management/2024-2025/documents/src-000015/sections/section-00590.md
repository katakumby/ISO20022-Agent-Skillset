---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["34 camt.102.001.03 CreateStandingOrderV03", "34.4 Message Building Blocks", "34.4.3 ValueSet <ValSet>", "34.4.3.8 ValidityPeriod <VldtyPrd>", "34.4.3.8.1 FromDate <FrDt>"]
file_pages: [765, 766]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.102.001.03"]
---

# 34.4.3.8.1 FromDate <FrDt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 765 to 766.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 765

```text
ValidityPeriod <VldtyPrd> contains one of the following DatePeriod2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 765
Or   ToDate <ToDt> [1..1] Date 765
Or}   FromToDate <FrToDt> [1..1] ± 765
34.4.3.8.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 883
34.4.3.8.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 883
34.4.3.8.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Range of time between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 800 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 800
   ToDate <ToDt> [1..1] Date 800
34.4.3.9  ZeroSweepIndicator <ZeroSweepInd>
Presence: [0..1]
Definition: Indicates whether the standing order is defined as a zero sweeping order. When true, the
liquidity transfer standing order will transfer all amount of money out of the account so the resulting
balance is zero.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 886):
• Meaning When True: True
• Meaning When False: False
34.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C10 "SupplementaryDataRule"
Approved by the Payments SEG on 04 February 2025 camt.102.001.03 CreateStandingOrderV03
Cash Management - Maintenance 2024 - 2025 765 February 2025
```

## File page 766

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 815 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 816
   Envelope <Envlp> [1..1] (External Schema) 816
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Payments SEG on 04 February 2025 camt.102.001.03 CreateStandingOrderV03
Cash Management - Maintenance 2024 - 2025 766 February 2025
```

