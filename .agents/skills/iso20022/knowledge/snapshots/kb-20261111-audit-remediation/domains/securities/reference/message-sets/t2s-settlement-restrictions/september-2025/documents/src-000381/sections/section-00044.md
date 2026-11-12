---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["3 semt.029.001.01 IntraPositionMovementQueryResponseV01", "3.2 Structure"]
file_pages: [58, 59]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 3.2 Structure

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 58 to 59.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 58

```text
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraPosMvmntQryRspn> [1..1]  C3, C4,
C18,
C19
   Pagination <Pgntn> [1..1] ± 62
   ReportGeneralDetails <RptGnlDtls> [1..1]  C20 62
     QueryReference <QryRef> [0..1] Text 63
     ReportIdentification <RptId> [0..1] Text 63
     QueryType <QryTp> [1..1] CodeSet 63
     ActivityIndicator <ActvtyInd> [1..1] Indicator 63
   Movements <Mvmnts> [0..*]  C1, C21,
C23
64
     AccountOwner <AcctOwnr> [0..1] ± 67
     SafekeepingAccount <SfkpgAcct> [0..1] ± 67
     StatusAndReason <StsAndRsn> [0..1]  67
       ProcessingStatus <PrcgSts> [0..*] ± 67
       SettlementStatus <SttlmSts> [0..*] ± C16 68
       Settled <Sttld> [0..1] ± C6 68
     Movement <Mvmnt> [1..*]  C14 69
       AccountOwner <AcctOwnr> [0..1] ± 71
       SafekeepingAccount <SfkpgAcct> [0..1] ± 72
       StatusAndReason <StsAndRsn> [0..1]  72
         ProcessingStatus <PrcgSts> [0..*] ± 72
         SettlementStatus <SttlmSts> [0..*] ± C16 72
         Settled <Sttld> [0..1] ± C6 73
       AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 73
       AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 73
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 74
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 74
       PoolIdentification <PoolId> [0..1] Text 74
       CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 74
       MovementDetails <MvmntDtls> [0..1]  74
Approved by the Securities SEG on 21 August 2025 semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities - Settlement Restrictions 58 September 2025
```

## File page 59

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         BalanceFrom <BalFr> [1..1] ± 76
         BalanceTo <BalTo> [1..1] ± 76
         FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C9, C10,
C12,
C13,
C15
76
         FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C5, C17 77
         SettlementQuantity <SttlmQty> [1..1] ± 79
         SettledQuantity <SttldQty> [0..1] ± 79
         PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± 80
         RemainingToBeSettledQuantity <RmngToBeSttldQty> [0..1] ± 80
         IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 80
         EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 81
         StatusDate <StsDt> [0..1] DateTime 81
         AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 81
         Linkages <Lnkgs> [0..*]  81
           ProcessingPosition <PrcgPos> [0..1] ± C25 82
           MessageNumber <MsgNb> [0..1] ± C22 82
           Reference <Ref> [1..1]  83
{Or             SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 83
Or             IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 83
Or             IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 84
Or             AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 84
Or             MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 84
Or             PoolIdentification <PoolId> [1..1] Text 84
Or}             OtherTransactionIdentification <OthrTxId> [1..1] Text 84
           ReferenceOwner <RefOwnr> [0..1] ± 84
         SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 85
         Priority <Prty> [0..1] ± 85
         CorporateActionEventType <CorpActnEvtTp> [0..1] ± C11 85
         MessageOriginator <MsgOrgtr> [0..1] ± 86
         CreationDateTime <CreDtTm> [1..1] DateTime 86
Approved by the Securities SEG on 21 August 2025 semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities - Settlement Restrictions 59 September 2025
```

