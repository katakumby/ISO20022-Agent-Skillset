---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.15 AggregateBalancePerSafekeepingPlace44", "7.1.5.15.16 HoldingAdditionalDetails <HldgAddtlDtls>"]
file_pages: [314]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.15.16 HoldingAdditionalDetails <HldgAddtlDtls>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 314 to 314.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 314

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
7.1.5.15.16  HoldingAdditionalDetails <HldgAddtlDtls>
Presence: [0..1]
Definition: Provides additional information on the holding.
Datatype: "Max350Text" on page 557
7.1.6 Cash
7.1.6.1  CashSettlementSystem4Choice
Definition: Choice of format for the cash settlement system.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 314
Or}   Proprietary <Prtry> [1..1] ± 314
7.1.6.1.1  Code <Cd>
Presence: [1..1]
Definition: Cash settlement system expressed as an ISO 20022 code.
Datatype: "CashSettlementSystem2Code" on page 494
CodeName Name Definition
GROS GrossSettlementSystem Settle money through gross settlement
system.
NETS NetSettlementSystem Settle money through net settlement
system.
7.1.6.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Cash settlement system expressed as a proprietary code.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 314 March 2026
```

