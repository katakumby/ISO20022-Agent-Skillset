---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.5 SettlementDetails230", "35.1.26.5.1 SecuritiesTransactionType <SctiesTxTp>"]
file_pages: [1811]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.5.1 SecuritiesTransactionType <SctiesTxTp>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1811 to 1811.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1811

```text
ReceiveDelivery: Delivery (DELI)
SettlementTransactionType: CollateralIn (COLI).
• SettlementDetailsElementsUsageRule
Conditions of use of the codes for the SettlementDetails field must be pre-agreed between account
owner and account servicer.
35.1.26.5.1  SecuritiesTransactionType <SctiesTxTp>
Presence: [0..1]
Definition: Identifies the type of securities transaction.
SecuritiesTransactionType <SctiesTxTp> contains one of the following elements (see
"SecuritiesTransactionType59Choice" on page 1624 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1624
Or}   Proprietary <Prtry> [1..1] ± 1626
35.1.26.5.2  SettlementTransactionCondition <SttlmTxCond>
Presence: [0..*]
Definition: Conditions under which the order/trade is to be settled.
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition42Choice" on page 2030 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2030
Or}   Proprietary <Prtry> [1..1] ± 2032
35.1.26.5.3  BeneficialOwnership <BnfclOwnrsh>
Presence: [0..1]
Definition: Specifies whether there is change of beneficial ownership.
BeneficialOwnership <BnfclOwnrsh> contains one of the following elements (see
"BeneficialOwnership4Choice" on page 1600 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1600
Or}   Proprietary <Prtry> [1..1] ± 1600
35.1.26.5.4  CCPEligibility <CCPElgblty>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is CCP (Central Counterparty) eligible.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1811 March 2026
```

