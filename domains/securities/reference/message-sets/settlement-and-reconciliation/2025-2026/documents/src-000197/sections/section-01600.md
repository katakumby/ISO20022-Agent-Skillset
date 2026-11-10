---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.120 ResponseStatus1Code"]
file_pages: [2136]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.120 ResponseStatus1Code

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 2136 to 2136.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2136

```text
CodeName Name Definition
WTHD Withdrawal Relates to a repo rollover of a position
extending the closing or maturity date.
35.2.2.120  ResponseStatus1Code
Definition: Specifies the status of the received collateral message (collateral claim, a collateral proposal
or a proposal/request for collateral substitution) from a collateral management perspective.
Type: CodeSet
CodeName Name Definition
ACCP PartlyAccepted Part of the collateral is accepted, a part
rejected.
ACCT Accepted Claim, substitution, proposal is fully
accepted.
REJT Rejected Claim, substitution, proposal is fully
rejected.
SUBR SubstitutionAccepted Party A agrees with the return part of the
substitution and accepts to wait for the
proposal of the new collateral.
35.2.2.121  RestrictionReference1Code
Definition: Specifies the restriction references to be applied to a transaction.
Type: CodeSet
Format
minLength 1
maxLength 4
CodeName Name Definition
ADDC AddCashRestrictionReference Addition of a cash restriction reference
representing a cash sub-balance to be
utilised within the settlement instruction
for the debiting or crediting of cash.
ADDS AddSecuritiesRestrictionReference Addition of a securities restriction
reference representing a securities sub-
position to be utilised within the
settlement instruction for the delivery or
receipt of securities.
REMC RemoveCashRestrictionReference Removal of a cash restriction reference,
already present within the settlement
instruction, representing a cash sub-
balance to be utilised within the
settlement instruction for the debiting or
crediting of cash.
REMS RemoveSecuritiesRestrictionReference Removal of a securities restriction
reference, already present within the
settlement instruction, representing a
securities sub-position to be utilised
within the settlement instruction for the
delivery or receipt of securities.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2136 March 2026
```

