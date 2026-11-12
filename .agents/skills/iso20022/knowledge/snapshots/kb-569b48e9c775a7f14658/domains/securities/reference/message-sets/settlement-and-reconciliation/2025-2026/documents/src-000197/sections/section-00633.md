---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11", "28.2 Structure"]
file_pages: [953, 954]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.034.001.11"]
---

# 28.2 Structure

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 953 to 954.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 953

```text
28.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesFincgStsAdvc> [1..1]  C34
   TransactionIdentification <TxId> [1..1] ± C19 0
   ProcessingStatus <PrcgSts> [0..1]  960
{Or     PendingCancellation <PdgCxl> [1..1]  961
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 962
Or}       Reason <Rsn> [1..*]  962
         Code <Cd> [1..1]  962
{Or           Code <Cd> [1..1] CodeSet 963
Or}           Proprietary <Prtry> [1..1] ± 963
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 963
Or     AcknowledgedAccepted <AckdAccptd> [1..1] ± 963
Or     PendingProcessing <PdgPrcg> [1..1]  964
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 964
Or}       Reason <Rsn> [1..*]  964
         Code <Cd> [1..1]  965
{Or           Code <Cd> [1..1] CodeSet 965
Or}           Proprietary <Prtry> [1..1] ± 966
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 966
Or     Rejected <Rjctd> [1..1] ± 966
Or     Repair <Rpr> [1..1] ± 967
Or     Cancelled <Canc> [1..1] ± 967
Or     Proprietary <Prtry> [1..1] ± 968
Or     CancellationRequested <CxlReqd> [1..1] ± C4 968
Or}     ModificationRequested <ModReqd> [1..1] ± C4 968
   MatchingStatus <MtchgSts> [0..1] ± 0
   InferredMatchingStatus <IfrrdMtchgSts> [0..1] ± 0
   SettlementStatus <SttlmSts> [0..1] ± C25 0
   RepoCallRequestStatus <RepoCallReqSts> [0..1] ± 970
   TransactionDetails <TxDtls> [0..1]  C3, C26,
C28,
0
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 953 March 2026
```

## File page 954

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
C30,
C37
     SecuritiesFinancingTradeIdentification <SctiesFincgTradId> [0..1] Text 975
     SecuritiesFinancingUniqueTransactionIdentifier
<SctiesFincgUnqTxIdr>
[0..1] IdentifierSet 975
     ClosingLegIdentification <ClsgLegId> [0..1] Text 975
     PoolIdentification <PoolId> [0..1] Text 975
     CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 975
     TripartyAgentServiceProviderCollateralTransactionIdentific
ation <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 976
     ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 976
     AccountOwner <AcctOwnr> [0..1] ± 976
     SafekeepingAccount <SfkpgAcct> [0..1] ± 976
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 976
     SafekeepingPlace <SfkpgPlc> [0..1] ± C31 977
     PlaceOfTrade <PlcOfTrad> [0..1] ± 977
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C13,
C14,
C16,
C17,
C20
978
     SettlementQuantity <SttlmQty> [1..1] ± 979
     OpeningSettlementAmount <OpngSttlmAmt> [0..1] ± 979
     TerminationTransactionAmount <TermntnTxAmt> [0..1] ± 979
     DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  979
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C13,
C14,
C16,
C17,
C20
980
       ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 981
       CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  981
{Or         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 981
Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C6 981
Or}         LEI <LEI> [1..1] IdentifierSet 982
     OpeningSettlementDate <OpngSttlmDt> [1..1] ± 982
     TerminationDate <TermntnDt> [0..1] ± 982
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 954 March 2026
```

