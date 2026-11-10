---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.2 Message Datatypes", "9.2.2 CodeSet", "9.2.2.42 SecuritiesSettlementStatus1Code"]
file_pages: [339]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.2.2.42 SecuritiesSettlementStatus1Code

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 339 to 339.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 339

```text
9.2.2.42  SecuritiesSettlementStatus1Code
Definition: Provides the status of settlement of an instruction.
Type: CodeSet
CodeName Name Definition
PEND Pending Instruction is pending. Settlement at the
instructed settlement date is still
possible.
PENF Failing Instruction is failing. Settlement at the
instructed settlement date is no longer
possible.
9.2.2.43  SecuritiesTransactionType5Code
Definition: Specifies underlying information regarding the type of transaction.
Type: CodeSet
CodeName Name Definition
TRAD Trade Relates to the settlement of a trade.
9.2.2.44  SettlementDate4Code
Definition: Specifies the date of settlement, in coded form.
Type: CodeSet
CodeName Name Definition
WISS WhenIssued Settlement is to be done when the
security is issued.
9.2.2.45  SettlementTransactionCondition5Code
Definition: Specifies the conditions under which the order/trade is to be settled.
Type: CodeSet
CodeName Name Definition
PART PartialAllowed Partial settlement is allowed.
NPAR PartialNotAllowed Partial settlement is not allowed.
PARC PartialSettlementCashThresholdAllowed Partial settlement is allowed but must
satisfy a cash value minimum (value
defined in static data).
PARQ PartialSettlementQuantityThresholdAllowed Partial settlement is allowed but must
satisfy a minimum quantity of securities
(quantity defined in static data).
9.2.2.46  StatementUpdateType1Code
Definition: Specifies the nature of a statement update, for example, it is a complete statement.
Type: CodeSet
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 339 September 2025
```

