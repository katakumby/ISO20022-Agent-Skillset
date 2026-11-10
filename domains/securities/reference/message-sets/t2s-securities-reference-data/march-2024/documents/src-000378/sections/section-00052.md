---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["6 reda.010.001.01 SecurityQueryV01", "6.4 Message Building Blocks", "6.4.4 SmallSetReturnCriteria <SmlSetRtrCrit>", "6.4.4.14 SecuritiesQuantityType <SctiesQtyTp>"]
file_pages: [92, 93]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.010.001.01"]
---

# 6.4.4.14 SecuritiesQuantityType <SctiesQtyTp>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 92 to 93.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 92

```text
• Meaning When True: Requested
• Meaning When False: Not Requested
6.4.4.14  SecuritiesQuantityType <SctiesQtyTp>
Presence: [1..1]
Definition: Quantity of a security.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 531):
• Meaning When True: Requested
• Meaning When False: Not Requested
6.4.4.15  MinimumDenomination <MinDnmtn>
Presence: [1..1]
Definition: Indicates the minimum quantity (unit or nominal) of a security.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 531):
• Meaning When True: Requested
• Meaning When False: Not Requested
6.4.4.16  MinimumMultipleQuantity <MinMltplQty>
Presence: [1..1]
Definition: Minimum multiple quantity (unit or nominal) of securities.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 531):
• Meaning When True: Requested
• Meaning When False: Not Requested
6.4.4.17  DeviatingSettlementUnit <DevtgSttlmUnit>
Presence: [1..1]
Definition: Minimum quantity of securities that can be purchased without incurring a larger fee. For
example, if the round lot size is 100 and the trade is for 125 shares, then 100 will be processed without
a fee and the remaining 25 will incur a service fee for being an odd lot size.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 531):
• Meaning When True: Requested
• Meaning When False: Not Requested
6.4.5 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C10 "SupplementaryDataRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.010.001.01 SecurityQueryV01
Target2-Securities - Securities Reference Data 92 March 2024
```

## File page 93

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 486 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 486
   Envelope <Envlp> [1..1] (External Schema) 486
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.010.001.01 SecurityQueryV01
Target2-Securities - Securities Reference Data 93 March 2024
```

