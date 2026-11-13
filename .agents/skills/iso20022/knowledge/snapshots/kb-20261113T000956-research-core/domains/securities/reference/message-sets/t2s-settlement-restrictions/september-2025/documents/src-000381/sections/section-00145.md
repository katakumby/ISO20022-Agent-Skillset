---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["8 semt.034.001.01 IntraPositionMovementPendingReportV01", "8.4 Message Building Blocks", "8.4.5 Movements <Mvmnts>", "8.4.5.1 StatusAndReason <StsAndRsn>"]
file_pages: [179, 180]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.034.001.01"]
---

# 8.4.5.1 StatusAndReason <StsAndRsn>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 179 to 180.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 179

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         PoolIdentification <PoolId> [1..1] Text 190
Or}         OtherTransactionIdentification <OthrTxId> [1..1] Text 190
       ReferenceOwner <RefOwnr> [0..1] ± 190
     SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 190
     Priority <Prty> [0..1] ± 190
     CorporateActionEventType <CorpActnEvtTp> [0..1] ± C10 191
     MessageOriginator <MsgOrgtr> [0..1] ± 191
     CreationDateTime <CreDtTm> [1..1] DateTime 191
     InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 191
     SupplementaryData <SplmtryData> [0..*] ± C20 192
Constraints
• StatusAndReasonRule
StatusAndReason must be present or Movement(*)/StatusAndReason must be present, but not both.
8.4.5.1  StatusAndReason <StsAndRsn>
Presence: [0..1]
Definition: Status and status reason of the transaction.
StatusAndReason <StsAndRsn> contains the following elements (see "PendingStatusAndReason4"
on page 268 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingStatus <PrcgSts> [0..*] ± 268
   SettlementStatus <SttlmSts> [0..*] ± C15 268
8.4.5.2  Movement <Mvmnt>
Presence: [1..*]
Definition: Identifies the individual transaction.
Impacted by: C13 "NoAccountOwnerTransactionIdentificationRule"
Approved by the Securities SEG on 21 August 2025 semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities - Settlement Restrictions 179 September 2025
```

## File page 180

```text
Movement <Mvmnt> contains the following IntraPositionPending12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatusAndReason <StsAndRsn> [0..1] ± 181
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 181
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 181
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 181
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 182
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 182
   PoolIdentification <PoolId> [0..1] Text 182
   BalanceFrom <BalFr> [1..1] ± 182
   BalanceTo <BalTo> [1..1] ± 182
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C11,
C12,
C14
182
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C4, C16 184
   SettlementQuantity <SttlmQty> [1..1] ± 186
   IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 186
   StatusDate <StsDt> [0..1] DateTime 187
   AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 187
   Linkages <Lnkgs> [0..*]  187
     ProcessingPosition <PrcgPos> [0..1] ± C21 188
     MessageNumber <MsgNb> [0..1] ± C18 188
     Reference <Ref> [1..1]  188
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 189
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 189
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 189
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 189
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 189
Or       PoolIdentification <PoolId> [1..1] Text 190
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 190
Approved by the Securities SEG on 21 August 2025 semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities - Settlement Restrictions 180 September 2025
```

