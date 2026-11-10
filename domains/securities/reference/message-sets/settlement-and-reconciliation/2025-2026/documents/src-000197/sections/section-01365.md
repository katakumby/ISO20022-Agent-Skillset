---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.8 SettlementDetails224"]
file_pages: [1832]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.8 SettlementDetails224

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1832 to 1832.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1832

```text
35.1.26.8  SettlementDetails224
Definition: Details of settlement of a transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldIndicator <HldInd> [0..1] Indicator 1832
   SecuritiesTransactionType <SctiesTxTp> [1..1] ± 1832
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1833
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 1833
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1833
   CashClearingSystem <CshClrSys> [0..1] ± 1834
   MarketClientSide <MktClntSd> [0..1] ± 1834
   Registration <Regn> [0..1] ± 1834
   RepurchaseType <RpTp> [0..1] ± 1834
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 1835
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1835
Constraints
• CashClearingSystemRule
The CashClearingSystem codes are to be used only by agents directly involved in the settlement
process, such as local settlement agents, CSDs and central banks.
• SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed between
account owner and account servicer.
35.1.26.8.1  HoldIndicator <HldInd>
Presence: [0..1]
Definition: Indicates whether the transaction is on hold/blocked/frozen.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.26.8.2  SecuritiesTransactionType <SctiesTxTp>
Presence: [1..1]
Definition: Identifies the type of securities transaction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1832 March 2026
```

