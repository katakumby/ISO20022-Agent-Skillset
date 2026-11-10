---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.89 Statement74", "35.1.16.89.8 ActivityIndicator <ActvtyInd>"]
file_pages: [1637]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.89.8 ActivityIndicator <ActvtyInd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1637 to 1637.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1637

```text
StatementBasis <StmtBsis> contains one of the following elements (see "StatementBasis7Choice" on
page 1858 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1858
Or}   Proprietary <Prtry> [1..1] ± 1858
35.1.16.89.8  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.16.89.9  AuditedIndicator <AudtdInd>
Presence: [1..1]
Definition: Indicates whether the statement is audited or not.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.16.89.10  SubAccountIndicator <SubAcctInd>
Presence: [1..1]
Definition: Indicates whether the statement reports holdings at sub-safekeeping account level.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.16.89.11  TaxLotIndicator <TaxLotInd>
Presence: [0..1]
Definition: Indicates whether the statement contains tax lot details.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.16.89.12  SecurityInterestOrSetOff <SctyIntrstOrSetOff>
Presence: [0..1]
Definition: Indicates whether the holdings on the account are subject to security interest, lien or right of
set-off.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1637 March 2026
```

