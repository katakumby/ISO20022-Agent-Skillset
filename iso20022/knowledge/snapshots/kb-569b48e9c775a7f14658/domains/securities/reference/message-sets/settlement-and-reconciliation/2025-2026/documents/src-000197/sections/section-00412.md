---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13", "19.4 Message Building Blocks", "19.4.2 Linkages <Lnkgs>", "19.4.7.12 SafekeepingPlace <SfkpgPlc>"]
file_pages: [630, 631]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.025.001.13"]
---

# 19.4.7.12 SafekeepingPlace <SfkpgPlc>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 630 to 631.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 630

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
19.4.7.12  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
Impacted by: C51 "SafekeepingPlaceFormatOrLEIRule"
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
19.4.8 SettlementParameters <SttlmParams>
Presence: [1..1]
Definition: Parameters which explicitly state the conditions that must be fulfilled before a particular
transaction of a financial instrument can be settled. These parameters are defined by the instructing
party in compliance with settlement rules in the market the transaction will settle in.
Impacted by: C11 "CashClearingSystemRule", C58 "SettlementDetailsRule"
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 630 March 2026
```

## File page 631

```text
SettlementParameters <SttlmParams> contains the following elements (see "SettlementDetails221"
on page 1850 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Priority <Prty> [0..1] ± 1852
   SecuritiesTransactionType <SctiesTxTp> [1..1] ± 1852
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1852
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 1852
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1853
   BlockTrade <BlckTrad> [0..1] ± 1853
   CCPEligibility <CCPElgblty> [0..1] ± 1853
   CashClearingSystem <CshClrSys> [0..1] ± 1853
   ExposureType <XpsrTp> [0..1] ± 1854
   MarketClientSide <MktClntSd> [0..1] ± 1854
   NettingEligibility <NetgElgblty> [0..1] ± 1854
   Registration <Regn> [0..1] ± 1854
   RepurchaseType <RpTp> [0..1] ± 1855
   LegalRestrictions <LglRstrctns> [0..1] ± 1855
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 1855
   SettlingCapacity <SttlgCpcty> [0..1] ± 1855
   SettlementSystemMethod <SttlmSysMtd> [0..1] ± 1856
   TaxCapacity <TaxCpcty> [0..1] ± 1856
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1856
   AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 1857
   LetterOfGuarantee <LttrOfGrnt> [0..1] ± 1857
   EligibleForCollateral <ElgblForColl> [0..1] Indicator 1857
   SecuritiesSubBalanceType <SctiesSubBalTp> [0..1] ± 1857
   CashSubBalanceType <CshSubBalTp> [0..1] ± 1858
Constraints
• CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the settlement
process, such as local settlement agents, CSDs and central banks.
• SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed between
account owner and account servicer.
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 631 March 2026
```

