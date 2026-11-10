---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.27 Market", "66.1.27.4 OtherTargetMarketRiskTolerance1", "66.1.27.4.1 RiskToleranceType <RskTlrnceTp>"]
file_pages: [4811]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.27.4.1 RiskToleranceType <RskTlrnceTp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4811 to 4811.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4811

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RiskToleranceType <RskTlrnceTp> [0..1] Text 4811
   Target <Trgt> [0..1]  4811
{Or     Code <Cd> [1..1] CodeSet 4811
Or}     Proprietary <Prtry> [1..1] ± 4811
   AdditionalInformation <AddtlInf> [0..1] ± 4812
66.1.27.4.1  RiskToleranceType <RskTlrnceTp>
Presence: [0..1]
Definition: Type of risk tolerance.
Datatype: "Max35Text" on page 5403
66.1.27.4.2  Target <Trgt>
Presence: [0..1]
Definition: Choice of formats for the specification of whether the product is aimed at the type of risk
tolerance.
Target <Trgt> contains one of the following TargetMarket1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4811
Or}   Proprietary <Prtry> [1..1] ± 4811
66.1.27.4.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies whether the product is aimed at the target expressed as a code.
Datatype: "TargetMarket1Code" on page 5365
CodeName Name Definition
YSCO InScope Yes, is applicable.
NEUT Neutral Neutral or has no impact.
NSCO NotInScope No, is not applicable.
66.1.27.4.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies whether the product is aimed at the target expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4811 May 2026
```

