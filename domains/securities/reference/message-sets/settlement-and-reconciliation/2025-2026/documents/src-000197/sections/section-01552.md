---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.24 CorporateActionOption5Code"]
file_pages: [2057]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.24 CorporateActionOption5Code

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 2057 to 2057.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2057

```text
35.2.2.24  CorporateActionOption5Code
Definition: Specifies the corporate action options available to the account owner.
Type: CodeSet
CodeName Name Definition
CASH Cash Option to choose cash.
SECU Security Distribution of securities to holders.
35.2.2.25  CounterpartyResponseStatusReason1Code
Definition: Specifies the type of counterparty's action the response is related to.
Type: CodeSet
CodeName Name Definition
CPTR CounterpartyTransaction Specifies that the response is related to
an allegement from the counterparty.
CPCX CounterpartyCancellation Specifies that the response is related to
the cancellation request of the
counterparty.
CPMD CounterpartyModification Specifies that the response is related to
the modification request of the
counterparty.
35.2.2.26  CountryCode
Definition: Code to identify a country, a dependency, or another area of particular geopolitical interest,
on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).
Type: CodeSet
Format
pattern [A-Z]{2,2}
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
35.2.2.27  CreditDebitCode
Definition: Specifies if an operation is an increase or a decrease.
Type: CodeSet
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2057 March 2026
```

