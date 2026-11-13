---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.17 AggregateBalancePerSafekeepingPlace44", "82.1.5.17.16 HoldingAdditionalDetails <HldgAddtlDtls>"]
file_pages: [2906]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.17.16 HoldingAdditionalDetails <HldgAddtlDtls>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2906 to 2906.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2906

```text
Constraints
• EligibleForCollateralPurposesRule
If Subbalance type is EligibleForCollateralPurposes, then QuantityAndAvailability cannot be used.
On Condition
    /SubBalanceType/Code is equal to value 'EligibleForCollateralPurposes'
Following Must be True
    /Quantity/Quantity/QuantityAndAvailability Must be absent
• SubBalanceAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
used, them it must not contain information that can be provided in a structured field.
82.1.5.17.16  HoldingAdditionalDetails <HldgAddtlDtls>
Presence: [0..1]
Definition: Provides additional information on the holding.
Datatype: "Max350Text" on page 3328
82.1.6 Cash
82.1.6.1  CashSettlementSystem4Choice
Definition: Choice of format for the cash settlement system.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2906
Or}   Proprietary <Prtry> [1..1] ± 2906
82.1.6.1.1  Code <Cd>
Presence: [1..1]
Definition: Cash settlement system expressed as an ISO 20022 code.
Datatype: "CashSettlementSystem2Code" on page 3220
CodeName Name Definition
GROS GrossSettlementSystem Settle money through gross settlement
system.
NETS NetSettlementSystem Settle money through net settlement
system.
82.1.6.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Cash settlement system expressed as a proprietary code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2906 August 2026
```

