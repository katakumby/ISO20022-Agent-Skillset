---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "25.2 Structure"]
file_pages: [804]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.031.001.11"]
---

# 25.2 Structure

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 804 to 804.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 804

```text
25.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmCondModStsAdvc> [1..1]  C6, C7
   RequestReference <ReqRef> [1..1] Text 806
   AccountOwner <AcctOwnr> [0..1] ± 806
   SafekeepingAccount <SfkpgAcct> [0..1] ± 806
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 806
   RequestDetails <ReqDtls> [0..1]  C3, C4,
C8
807
     Reference <Ref> [1..1] ± C5 808
     RestrictionReference <RstrctnRef> [0..*] ± 808
     AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 809
     RetainIndicator <RtnInd> [0..1] Indicator 809
     Linkage <Lkg> [0..1] ± 809
     Priority <Prty> [0..1] ± 809
     OtherProcessing <OthrPrcg> [0..*] ± 810
     PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 810
     SecuritiesRTGS <SctiesRTGS> [0..1] ± 810
     HoldIndicator <HldInd> [0..1] ± 811
     MatchingDenial <MtchgDnl> [0..1] ± 811
     UnilateralSplit <UnltrlSplt> [0..1] ± 811
     Linkages <Lnkgs> [0..*] ± 811
   ProcessingStatus <PrcgSts> [1..1]  812
{Or     AcknowledgedAccepted <AckdAccptd> [1..1] ± 812
Or     Rejected <Rjctd> [1..1] ± 812
Or     Completed <Cmpltd> [1..1] ± C1 813
Or     Denied <Dnd> [1..1] ± 813
Or     Pending <Pdg> [1..1] ± 813
Or}     Proprietary <Prtry> [1..1] ± 814
   SupplementaryData <SplmtryData> [0..*] ± C10 814
Approved by the Securities SEG on 27 January 2026 sese.031.001.11
SecuritiesSettlementConditionModificationStatusAd
viceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 804 March 2026
```

