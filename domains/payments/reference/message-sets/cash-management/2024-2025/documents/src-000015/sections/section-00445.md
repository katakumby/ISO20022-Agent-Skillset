---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["22 camt.024.001.08 ModifyStandingOrderV08", "22.4 Message Building Blocks", "22.4.3 NewStandingOrderValueSet <NewStgOrdrValSet>", "22.4.3.8 ValidityPeriod <VldtyPrd>", "22.4.3.8.1 FromDate <FrDt>"]
file_pages: [602, 603]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.024.001.08"]
---

# 22.4.3.8.1 FromDate <FrDt>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 602 to 603.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 602

```text
ValidityPeriod <VldtyPrd> contains one of the following DatePeriod2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 602
Or   ToDate <ToDt> [1..1] Date 602
Or}   FromToDate <FrToDt> [1..1] ± 602
22.4.3.8.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 883
22.4.3.8.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 883
22.4.3.8.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Range of time between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 800 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 800
   ToDate <ToDt> [1..1] Date 800
22.4.3.9  ZeroSweepIndicator <ZeroSweepInd>
Presence: [0..1]
Definition: Indicates whether the standing order is defined as a zero sweeping order. When true, the
liquidity transfer standing order will transfer all amount of money out of the account so the resulting
balance is zero.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 886):
• Meaning When True: True
• Meaning When False: False
22.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C10 "SupplementaryDataRule"
Approved by the Payments SEG on 04 February 2025 camt.024.001.08 ModifyStandingOrderV08
Cash Management - Maintenance 2024 - 2025 602 February 2025
```

## File page 603

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
Approved by the Payments SEG on 04 February 2025 camt.024.001.08 ModifyStandingOrderV08
Cash Management - Maintenance 2024 - 2025 603 February 2025
```

