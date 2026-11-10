---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.2 Derivative4", "13.1.2.2.1 Future <Futr>", "13.1.2.2.1.7 AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>", "13.1.2.2.1.7.1 AllocationPercentage <AllcnPctg>"]
file_pages: [163]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.2.1.7.1 AllocationPercentage <AllcnPctg>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 163 to 163.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 163

```text
13.1.2.2.1.7.1  AllocationPercentage <AllcnPctg>
Presence: [0..1]
Definition: Percent of the strike price that this underlying represents.
Datatype: "PercentageRate" on page 532
13.1.2.2.1.7.2  Quantity <Qty>
Presence: [0..1]
Definition: Unit amount of the underlying security.
Quantity <Qty> contains one of the following UnitOrFaceAmount1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 163
Or}   FaceAmount <FaceAmt> [1..1] Amount C1, C5 163
13.1.2.2.1.7.2.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, eg, a number of shares.
Datatype: "DecimalNumber" on page 532
13.1.2.2.1.7.2.2  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, ie, the principal, of a debt
instrument.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 506
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
13.1.2.2.1.7.3  SettlementType <SttlmTp>
Presence: [0..1]
Definition: Indicates order settlement period for the underlying instrument. Represents the number of
days until settlement; for example, 2 means T+1 settlement, 4 means T+3 settlement, 5 means T+4
settlement.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 163 March 2024
```

