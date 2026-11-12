---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.1 SettlementDetails220", "35.1.26.1.31 CashSubBalanceType <CshSubBalTp>"]
file_pages: [1792]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.1.31 CashSubBalanceType <CshSubBalTp>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1792 to 1792.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1792

```text
35.1.26.1.31  CashSubBalanceType <CshSubBalTp>
Presence: [0..1]
Definition: Specifies the cash sub balance type indicator, for example, the restriction type for a market
infrastructure.
CashSubBalanceType <CshSubBalTp> contains the following elements (see
"GenericIdentification30" on page 1502 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.26.2  SettlementDetails234
Definition: Details of settlement of a transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldIndicator <HldInd> [0..1] Indicator 1792
   SecuritiesTransactionType <SctiesTxTp> [1..1] ± 1793
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1793
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 1793
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1793
   CashClearingSystem <CshClrSys> [0..1] ± 1794
   MarketClientSide <MktClntSd> [0..1] ± 1794
   Registration <Regn> [0..1] ± 1794
   RepurchaseType <RpTp> [0..1] ± 1794
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 1795
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1795
Constraints
• CashClearingSystemRule
The CashClearingSystem codes are to be used only by agents directly involved in the settlement
process, such as local settlement agents, CSDs and central banks.
• SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed between
account owner and account servicer.
35.1.26.2.1  HoldIndicator <HldInd>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1792 March 2026
```

