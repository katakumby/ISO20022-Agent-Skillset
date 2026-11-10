---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "8.4 Message Building Blocks", "8.4.8 SubAccountDetails <SubAcctDtls>", "8.4.8.5 FinancialInstrumentDetails <FinInstrmDtls>", "8.4.8.5.7 Transaction <Tx>", "8.4.8.5.7.19 TransactionDetails <TxDtls>", "8.4.8.5.7.19.5 SettlementParameters <SttlmParams>"]
file_pages: [263]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.017.001.14"]
---

# 8.4.8.5.7.19.5 SettlementParameters <SttlmParams>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 263 to 263.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 263

```text
CodeName Name Definition
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
8.4.8.5.7.19.5  SettlementParameters <SttlmParams>
Presence: [0..1]
Definition: Parameters applied to the settlement of a security transfer.
Impacted by: C5 "CashClearingSystemRule", C37 "SettlementDetailsRule"
SettlementParameters <SttlmParams> contains the following elements (see "SettlementDetails231"
on page 1801 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1802
   SettlingCapacity <SttlgCpcty> [0..1] ± 1803
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1803
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 1803
   Registration <Regn> [0..1] ± 1803
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1804
   CashClearingSystem <CshClrSys> [0..1] ± 1804
   TaxCapacity <TaxCpcty> [0..1] ± 1804
   RepurchaseType <RpTp> [0..1] ± 1804
   MarketClientSide <MktClntSd> [0..1] ± 1805
   BlockTrade <BlckTrad> [0..1] ± 1805
   LegalRestrictions <LglRstrctns> [0..1] ± 1805
   SettlementSystemMethod <SttlmSysMtd> [0..1] ± 1805
   NettingEligibility <NetgElgblty> [0..1] ± 1806
   CCPEligibility <CCPElgblty> [0..1] ± 1806
   LetterOfGuarantee <LttrOfGrnt> [0..1] ± 1806
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 1807
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 263 March 2026
```

