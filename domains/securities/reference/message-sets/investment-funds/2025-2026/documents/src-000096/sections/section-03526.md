---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.22 Equalisation1", "66.1.26.22.2 Rate <Rate>"]
file_pages: [4776]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.22.2 Rate <Rate>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4776 to 4776.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4776

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.26.22.2  Rate <Rate>
Presence: [0..1]
Definition: Rate used for calculation of the equalisation.
Datatype: "PercentageRate" on page 5401
66.1.26.23  InvestmentPlanCharacteristics1
Definition: Characteristics of an investment plan.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlanType <PlanTp> [1..1]  4776
{Or     Code <Cd> [1..1] CodeSet 4777
Or}     Proprietary <Prtry> [1..1] ± 4777
   Frequency <Frqcy> [0..1] ± 4777
   TotalNumberOfInstalments <TtlNbOfInstlmts> [0..1] Quantity 4777
   Quantity <Qty> [0..1] ± 4778
   PlanContinuation <PlanConttn> [0..1] Indicator 4778
   AdditionalSubscription <AddtlSbcpt> [0..1] Indicator 4778
   AdditionalSubscriptionFunction <AddtlSbcptFctn> [0..1] Indicator 4778
   AdditionalInformation <AddtlInf> [0..*] ± 4778
Constraints
• InvestmentPlanRule
If PlanType/Code is not INVP the AdditionalSubscription and AdditionalSubscriptionFunction must
not be present.
66.1.26.23.1  PlanType <PlanTp>
Presence: [1..1]
Definition: Type of investment plan.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4776 May 2026
```

