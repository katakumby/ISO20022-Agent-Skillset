---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12", "20.4 Message Building Blocks", "20.4.7 QuantityAndAccountDetails <QtyAndAcctDtls>", "20.4.7.12 SafekeepingPlace <SfkpgPlc>"]
file_pages: [682, 683]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.026.001.12"]
---

# 20.4.7.12 SafekeepingPlace <SfkpgPlc>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 682 to 683.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 682

```text
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown63" on
page 1736 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 1736
   LotQuantity <LotQty> [0..1] ± C12 1737
   SecuritiesSubBalanceType <SctiesSubBalTp> [0..1] ± 1737
   LotDateTime <LotDtTm> [0..1] ± 1737
   LotPrice <LotPric> [0..1] ± 1738
   TypeOfPrice <TpOfPric> [0..1] ± 1738
20.4.7.12  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
Impacted by: C50 "SafekeepingPlaceFormatOrLEIRule"
SafekeepingPlace <SfkpgPlc> contains the following elements (see "SafeKeepingPlace5" on
page 1749 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceFormat <SfkpgPlcFrmt> [0..1] ± 1749
   LEI <LEI> [0..1] IdentifierSet 1750
Constraints
• SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
Following Must be True
    /SafekeepingPlaceFormat Must be present
 Or    /LEI Must be present
20.4.8 SettlementParameters <SttlmParams>
Presence: [1..1]
Definition: Parameters which explicitly state the conditions that must be fulfilled before a particular
transaction of a financial instrument can be settled. These parameters are defined by the instructing
party in compliance with settlement rules in the market the transaction will settle in.
Impacted by: C11 "CashClearingSystemRule", C56 "SettlementDetailsRule"
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 682 March 2026
```

## File page 683

```text
SettlementParameters <SttlmParams> contains the following elements (see "SettlementDetails223"
on page 1835 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Priority <Prty> [0..1] ± 1837
   SecuritiesTransactionType <SctiesTxTp> [1..1] ± 1837
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1837
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 1837
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1838
   BlockTrade <BlckTrad> [0..1] ± 1838
   CCPEligibility <CCPElgblty> [0..1] ± 1838
   CashClearingSystem <CshClrSys> [0..1] ± 1838
   ExposureType <XpsrTp> [0..1] ± 1839
   MarketClientSide <MktClntSd> [0..1] ± 1839
   NettingEligibility <NetgElgblty> [0..1] ± 1839
   Registration <Regn> [0..1] ± 1839
   RepurchaseType <RpTp> [0..1] ± 1840
   LegalRestrictions <LglRstrctns> [0..1] ± 1840
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 1840
   SettlingCapacity <SttlgCpcty> [0..1] ± 1840
   SettlementSystemMethod <SttlmSysMtd> [0..1] ± 1841
   TaxCapacity <TaxCpcty> [0..1] ± 1841
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1841
   AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 1842
   LetterOfGuarantee <LttrOfGrnt> [0..1] ± 1842
   EligibleForCollateral <ElgblForColl> [0..1] Indicator 1842
   SecuritiesSubBalanceType <SctiesSubBalTp> [0..1] ± 1842
   CashSubBalanceType <CshSubBalTp> [0..1] ± 1843
Constraints
• CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the settlement
process, such as local settlement agents, CSDs and central banks.
• SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed between
account owner and account servicer.
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 683 March 2026
```

