---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.3 SubBalanceType11Choice", "7.1.5.3.2 Proprietary <Prtry>"]
file_pages: [261]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.3.2 Proprietary <Prtry>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 261 to 261.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 261

```text
7.1.5.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason a security is not available or additional information about the financial instrument for
which the balance is given, for example, unregistered, registered in nominee name.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.5.4  AdditionalBalanceInformation18
Definition: Subbalances providing additional information on a specific position but that is not to be
accounted for in the building of the aggregate balance, for example, registered.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SubBalanceType <SubBalTp> [1..1] ± 261
   Quantity <Qty> [1..1] ± 262
   SubBalanceAdditionalDetails <SubBalAddtlDtls> [0..1] Text 262
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 262
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
7.1.5.4.1  SubBalanceType <SubBalTp>
Presence: [1..1]
Definition: Reason for the sub-balance.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 261 March 2026
```

