---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.13 AccountingStatementOfHoldings2", "66.1.5.13.1 StatementGeneralDetails <StmtGnlDtls>", "66.1.5.13.1.9 AuditedIndicator <AudtdInd>"]
file_pages: [4405]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.13.1.9 AuditedIndicator <AudtdInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4405 to 4405.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4405

```text
Datatype: "Max5NumericText" on page 5404
66.1.5.13.1.9  AuditedIndicator <AudtdInd>
Presence: [1..1]
Definition: Indicates whether the statement is audited.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.5.13.2  AccountDetails <AcctDtls>
Presence: [0..1]
Definition: The safekeeping or investment account of the statement that is being cancelled.
AccountDetails <AcctDtls> contains the following elements (see "SafekeepingAccount2" on
page 4643 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4643
   FungibleIndicator <FngbInd> [1..1] Indicator 4643
   Name <Nm> [0..1] Text 4644
   Designation <Dsgnt> [0..1] Text 4644
   IntermediaryInformation <IntrmyInf> [0..10] ± 4644
   AccountOwner <AcctOwnr> [0..1] ± 4644
   AccountServicer <AcctSvcr> [0..1] ± 4645
66.1.5.13.3  BalanceForAccount <BalForAcct>
Presence: [0..*]
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account.
Impacted by: C1 "AccruedInterestAmountSignRule", C6 "BalanceAtSafekeepingPlaceRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4405 May 2026
```

