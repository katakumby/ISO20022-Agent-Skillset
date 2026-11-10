---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11", "28.4 Message Building Blocks", "28.4.6 RepoCallRequestStatus <RepoCallReqSts>", "28.4.7.28 SettlementParameters <SttlmParams>"]
file_pages: [985]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.034.001.11"]
---

# 28.4.7.28 SettlementParameters <SttlmParams>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 985 to 985.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 985

```text
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
28.4.7.28  SettlementParameters <SttlmParams>
Presence: [0..1]
Definition: Parameters applied to the settlement of a security transfer.
Impacted by: C8 "CashClearingSystemRule", C33 "SettlementDetailsRule"
SettlementParameters <SttlmParams> contains the following elements (see "SettlementDetails227"
on page 1816 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldIndicator <HldInd> [0..1] Indicator 1817
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1817
   SettlingCapacity <SttlgCpcty> [0..1] ± 1818
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1818
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 1818
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1819
   CashClearingSystem <CshClrSys> [0..1] ± 1819
   TaxCapacity <TaxCpcty> [0..1] ± 1819
   MarketClientSide <MktClntSd> [0..1] ± 1819
   BlockTrade <BlckTrad> [0..1] ± 1820
   LegalRestrictions <LglRstrctns> [0..1] ± 1820
   SettlementSystemMethod <SttlmSysMtd> [0..1] ± 1820
   NettingEligibility <NetgElgblty> [0..1] ± 1820
   CCPEligibility <CCPElgblty> [0..1] ± 1821
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 1821
   EligibleForCollateral <ElgblForColl> [0..1] Indicator 1821
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 985 March 2026
```

