---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.15 AggregateBalancePerSafekeepingPlace44", "7.1.5.15.14 BalanceBreakdown <BalBrkdwn>"]
file_pages: [313]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.15.14 BalanceBreakdown <BalBrkdwn>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 313 to 313.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 313

```text
7.1.5.15.14  BalanceBreakdown <BalBrkdwn>
Presence: [0..*]
Definition: Breakdown of the aggregate balance per meaningful sub-balances and availability.
Impacted by: C10 "AvailableWithNoStatusRule", C35 "SubBalanceAdditionalDetailsRule"
BalanceBreakdown <BalBrkdwn> contains the following elements (see "SubBalanceInformation18"
on page 271 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SubBalanceType <SubBalTp> [1..1] ± 272
   Quantity <Qty> [1..1] ± 272
   SubBalanceAdditionalDetails <SubBalAddtlDtls> [0..1] Text 272
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 272
   AdditionalBalanceBreakdownDetails
<AddtlBalBrkdwnDtls>
[0..*] ± C20,
C36
273
Constraints
• AvailableWithNoStatusRule
If Subbalance type is AvailableWithNoStatus, then QuantityAndAvailability cannot be used.
On Condition
    /SubBalanceType/Code is equal to value 'AvailableWithNoAdditionalStatus'
Following Must be True
    /Quantity/Quantity/QuantityAndAvailability Must be absent
• SubBalanceAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
used, them it must not contain information that can be provided in a structured field.
7.1.5.15.15  AdditionalBalanceBreakdown <AddtlBalBrkdwn>
Presence: [0..*]
Definition: Provides additional instrument sub-balance information on all or parts of the reported
financial instrument (unregistered, tax exempt, etc.).
Impacted by: C21 "EligibleForCollateralPurposesRule", C37 "SubBalanceAdditionalDetailsRule"
AdditionalBalanceBreakdown <AddtlBalBrkdwn> contains the following elements (see
"AdditionalBalanceBreakdown1" on page 256 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SubBalanceType <SubBalTp> [1..1] ± 257
   Quantity <Qty> [1..1] ± 257
   SubBalanceAdditionalDetails <SubBalAddtlDtls> [0..1] Text 257
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 258
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 313 March 2026
```

