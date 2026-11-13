---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13"]
file_pages: [830]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7 pacs.009.001.13 FinancialInstitutionCreditTransferV13

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 830 to 830.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 830

```text
7 pacs.009.001.13
FinancialInstitutionCreditTransferV13
7.1 MessageDefinition Functionality
Scope
The FinancialInstitutionCreditTransfer message is sent by a debtor financial institution to a creditor
financial institution, directly or through other agents and/or a payment clearing and settlement system.
It is used to move funds from a debtor account to a creditor, where both debtor and creditor are
financial institutions.
Usage
The FinancialInstitutionCreditTransfer message is exchanged between agents and can contain one or
more credit transfer instructions where debtor and creditor are both financial institutions.
The FinancialInstitutionCreditTransfer message does not allow for grouping: a
CreditTransferTransactionInformation block must be present for each credit transfer transaction.
The FinancialInstitutionCreditTransfer message can be used in domestic and cross-border scenarios.
Outline
The FinancialInstitutionCreditTransferV13 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. GroupHeader
Set of characteristics shared by all individual transactions included in the message.
B. CreditTransferTransactionInformation
Set of elements providing information specific to the individual credit transfer(s).
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
830 March 2026
```

