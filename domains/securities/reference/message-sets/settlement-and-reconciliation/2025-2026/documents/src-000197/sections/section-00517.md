---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10", "24.2 Structure"]
file_pages: [785]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.030.001.10"]
---

# 24.2 Structure

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 785 to 785.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 785

```text
24.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmCondsModReq> [1..1]  C14,
C17,
C20,
C21
   AccountOwner <AcctOwnr> [0..1] ± 788
   SafekeepingAccount <SfkpgAcct> [0..1] ± 788
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 789
   RequestDetails <ReqDtls> [1..*]  C8, C10,
C22
789
     Reference <Ref> [1..1] ± C13 790
     RestrictionReference <RstrctnRef> [0..*] ± 791
     AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 791
     RetainIndicator <RtnInd> [0..1] Indicator 792
     Linkage <Lkg> [0..1] ± 792
     Priority <Prty> [0..1] ± 792
     OtherProcessing <OthrPrcg> [0..*] ± 792
     PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 793
     SecuritiesRTGS <SctiesRTGS> [0..1] ± 793
     HoldIndicator <HldInd> [0..1] ± 793
     MatchingDenial <MtchgDnl> [0..1] ± 794
     UnilateralSplit <UnltrlSplt> [0..1] ± 794
     Linkages <Lnkgs> [0..*] ± 794
   AdditionalInformation <AddtlInf> [0..*]  C11,
C12,
C15,
C18
795
     AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 796
     ClassificationType <ClssfctnTp> [0..1] ± 796
     SafekeepingAccount <SfkpgAcct> [0..1] ± 796
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 796
     FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C3, C4,
C6, C7,
C9
797
     Quantity <Qty> [0..1] ± C5 798
     EffectiveDate <FctvDt> [0..1] ± 798
Approved by the Securities SEG on 27 January 2026 sese.030.001.10
SecuritiesSettlementConditionsModificationRequest
V10
Settlement And Reconciliation - Maintenance 2025 - 2026 785 March 2026
```

