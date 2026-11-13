---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06"]
file_pages: [1016]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.010.001.06"]
---

# 8 pacs.010.001.06 FinancialInstitutionDirectDebitV06

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1016 to 1016.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1016

```text
8 pacs.010.001.06
FinancialInstitutionDirectDebitV06
8.1 MessageDefinition Functionality
Scope:
The FinancialInstitutionDirectDebit message is sent by an exchange or clearing house, or a financial
institution, directly or through another agent, to the DebtorAgent. It is used to instruct the DebtorAgent
to move funds from one or more debtor(s) account(s) to one or more creditor(s), where both debtor and
creditor are financial institutions.
Usage:
The FinancialInstitutionDirectDebit message is exchanged between agents and can contain one or
more financial institution direct debit instruction(s) for one or more creditor(s). The
FinancialInstitutionDirectDebit message can be used in domestic and cross-border scenarios.
Outline
The FinancialInstitutionDirectDebitV06 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. GroupHeader
Common characteristics for all individual transactions included in the message.
B. CreditInstruction
Characteristics that apply to the credit side of the payment transaction(s) included in the message.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 12 January 2026 pacs.010.001.06 FinancialInstitutionDirectDebitV06
Payments Clearing and Settlement - Maintenance 2025 -
2026
1016 March 2026
```

