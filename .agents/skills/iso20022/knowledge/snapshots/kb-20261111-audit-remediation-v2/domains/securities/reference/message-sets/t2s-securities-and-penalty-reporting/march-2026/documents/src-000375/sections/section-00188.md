---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.4 Amount Range", "7.1.4.2 ActiveCurrencyAndAmountRange3", "7.1.4.2.3 Currency <Ccy>"]
file_pages: [256]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.4.2.3 Currency <Ccy>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 256 to 256.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 256

```text
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
7.1.4.2.3  Currency <Ccy>
Presence: [1..1]
Definition: Medium of exchange of value, used to qualify an amount.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 492
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
7.1.4.3  AmountRangeBoundary1
Definition: Limit for an amount range.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 256
   Included <Incl> [1..1] Indicator 256
7.1.4.3.1  BoundaryAmount <BdryAmt>
Presence: [1..1]
Definition: Amount value of the range limit.
Datatype: "ImpliedCurrencyAndAmount" on page 491
7.1.4.3.2  Included <Incl>
Presence: [1..1]
Definition: Indicates whether the boundary amount is included in the range of amount values.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 553):
• Meaning When True: Yes
• Meaning When False: No
7.1.5 Balance
7.1.5.1  AdditionalBalanceBreakdown1
Definition: Subbalances providing additional information on a specific position but that is not to be
accounted for in the building of the aggregate balance, for example, registered.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 256 March 2026
```

