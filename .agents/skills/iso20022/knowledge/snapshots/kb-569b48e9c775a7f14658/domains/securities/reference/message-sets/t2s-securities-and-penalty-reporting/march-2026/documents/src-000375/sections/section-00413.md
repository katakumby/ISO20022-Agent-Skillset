---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.41 PenaltyAmountType1Code"]
file_pages: [517]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.41 PenaltyAmountType1Code

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 517 to 517.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 517

```text
CodeName Name Definition
NRST NoRestrictions Ownership or transfer of a security that
is not subject to restrictions.
RSTR Restrictions Ownership or transfer of a security that
is subject to restrictions, and not
pursuant to 144A.
7.2.2.41  PenaltyAmountType1Code
Definition: Specifies the type of the penalty amount.
Type: CodeSet
CodeName Name Definition
CASH Cash Penalty is based on the amount of cash
failed to be delivered and the penalty
rate is the discount rate of the relevant
currency.
SECU Securities Penalty is based on the quantity of
securities failed to be delivered and
penalty rate of the securities.
7.2.2.42  PenaltyCalculationMethod1Code
Definition: Specifies the calculation method for the penalty.
Type: CodeSet
CodeName Name Definition
BOTH Both Sum of the penalty based on the quantity
of securities
failed to be delivered and penalty rate of
the securities and the penalty based on
the amount of cash failed to be delivered
and the discount rate of the currency.
CASH Cash Penalty is based on the amount of cash
failed to be delivered and the penalty
rate is the discount rate of the relevant
currency.
MIXE Mixed Penalty is based on the quantity of
securities failed to be delivered and
penalty rate is the discount rate of the
relevant currency.
SECU Securities Penalty is based on the quantity of
securities failed to be delivered and
penalty rate of the securities.
7.2.2.43  PenaltyListType1Code
Definition: Specifies the type of report for the penalties.
Type: CodeSet
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 517 March 2026
```

