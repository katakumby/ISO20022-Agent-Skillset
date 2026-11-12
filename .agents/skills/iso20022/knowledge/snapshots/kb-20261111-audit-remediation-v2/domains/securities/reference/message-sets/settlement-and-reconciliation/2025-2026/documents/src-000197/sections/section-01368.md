---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.8 SettlementDetails224", "35.1.26.8.10 SecuritiesRTGS <SctiesRTGS>"]
file_pages: [1835, 1836]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.8.10 SecuritiesRTGS <SctiesRTGS>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1835 to 1836.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1835

```text
35.1.26.8.10  SecuritiesRTGS <SctiesRTGS>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is to be settled through an RTGS or a non
RTGS system.
SecuritiesRTGS <SctiesRTGS> contains one of the following elements (see
"SecuritiesRTGS4Choice" on page 1554 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1554
Or}   Proprietary <Prtry> [1..1] ± 1554
35.1.26.8.11  StampDutyTaxBasis <StmpDtyTaxBsis>
Presence: [0..1]
Definition: Specifies the stamp duty type or exemption reason applicable to the settlement transaction.
StampDutyTaxBasis <StmpDtyTaxBsis> contains the following elements (see
"GenericIdentification30" on page 1502 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.26.9  SettlementDetails223
Definition: Details of settlement of a transaction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1835 March 2026
```

## File page 1836

```text
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1836 March 2026
```

