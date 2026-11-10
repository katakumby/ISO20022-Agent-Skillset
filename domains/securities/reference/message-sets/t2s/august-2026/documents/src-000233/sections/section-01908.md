---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["74 semt.029.001.01 IntraPositionMovementQueryResponseV01", "74.2 Structure"]
file_pages: [2613, 2614]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 74.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2613 to 2614.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2613

```text
74.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraPosMvmntQryRspn> [1..1]  C3, C4,
C18,
C19
   Pagination <Pgntn> [1..1] ± 2617
   ReportGeneralDetails <RptGnlDtls> [1..1]  C20 2617
     QueryReference <QryRef> [0..1] Text 2618
     ReportIdentification <RptId> [0..1] Text 2618
     QueryType <QryTp> [1..1] CodeSet 2618
     ActivityIndicator <ActvtyInd> [1..1] Indicator 2618
   Movements <Mvmnts> [0..*]  C1, C21,
C23
2619
     AccountOwner <AcctOwnr> [0..1] ± 2622
     SafekeepingAccount <SfkpgAcct> [0..1] ± 2622
     StatusAndReason <StsAndRsn> [0..1]  2622
       ProcessingStatus <PrcgSts> [0..*] ± 2622
       SettlementStatus <SttlmSts> [0..*] ± C16 2623
       Settled <Sttld> [0..1] ± C6 2623
     Movement <Mvmnt> [1..*]  C14 2624
       AccountOwner <AcctOwnr> [0..1] ± 2626
       SafekeepingAccount <SfkpgAcct> [0..1] ± 2627
       StatusAndReason <StsAndRsn> [0..1]  2627
         ProcessingStatus <PrcgSts> [0..*] ± 2627
         SettlementStatus <SttlmSts> [0..*] ± C16 2627
         Settled <Sttld> [0..1] ± C6 2628
       AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 2628
       AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 2628
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 2629
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 2629
       PoolIdentification <PoolId> [0..1] Text 2629
       CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 2629
       MovementDetails <MvmntDtls> [0..1]  2629
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2613 August 2026
```

## File page 2614

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         BalanceFrom <BalFr> [1..1] ± 2631
         BalanceTo <BalTo> [1..1] ± 2631
         FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C9, C10,
C12,
C13,
C15
2631
         FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C5, C17 2632
         SettlementQuantity <SttlmQty> [1..1] ± 2634
         SettledQuantity <SttldQty> [0..1] ± 2634
         PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± 2635
         RemainingToBeSettledQuantity <RmngToBeSttldQty> [0..1] ± 2635
         IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 2635
         EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 2636
         StatusDate <StsDt> [0..1] DateTime 2636
         AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 2636
         Linkages <Lnkgs> [0..*]  2636
           ProcessingPosition <PrcgPos> [0..1] ± C25 2637
           MessageNumber <MsgNb> [0..1] ± C22 2637
           Reference <Ref> [1..1]  2638
{Or             SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 2638
Or             IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 2638
Or             IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 2639
Or             AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 2639
Or             MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 2639
Or             PoolIdentification <PoolId> [1..1] Text 2639
Or}             OtherTransactionIdentification <OthrTxId> [1..1] Text 2639
           ReferenceOwner <RefOwnr> [0..1] ± 2639
         SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 2640
         Priority <Prty> [0..1] ± 2640
         CorporateActionEventType <CorpActnEvtTp> [0..1] ± C11 2640
         MessageOriginator <MsgOrgtr> [0..1] ± 2641
         CreationDateTime <CreDtTm> [1..1] DateTime 2641
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2614 August 2026
```

