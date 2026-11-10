---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.23 InvestmentPlanCharacteristics1", "66.1.26.23.1 PlanType <PlanTp>", "66.1.26.23.1.1 Code <Cd>"]
file_pages: [4777]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.23.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4777 to 4777.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4777

```text
PlanType <PlanTp> contains one of the following InvestmentFundPlanType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4777
Or}   Proprietary <Prtry> [1..1] ± 4777
66.1.26.23.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of investment fund plan expressed as a code.
Datatype: "InvestmentFundPlanType1Code" on page 5318
CodeName Name Definition
INVP SavingsInvestmentPlan Savings investment plan.
SWIP SwitchPlan Switch plan.
WTHP WithdrawalPlan Withdrawal plan.
66.1.26.23.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of investment fund plan expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.26.23.2  Frequency <Frqcy>
Presence: [0..1]
Definition: Frequency of the investment plan.
Frequency <Frqcy> contains one of the following elements (see "Frequency20Choice" on page 4535
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4536
Or}   Proprietary <Prtry> [1..1] ± 4536
66.1.26.23.3  TotalNumberOfInstalments <TtlNbOfInstlmts>
Presence: [0..1]
Definition: Total number of times the amount must be invested at the predefined frequency as of the
start date of the investment plan.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4777 May 2026
```

