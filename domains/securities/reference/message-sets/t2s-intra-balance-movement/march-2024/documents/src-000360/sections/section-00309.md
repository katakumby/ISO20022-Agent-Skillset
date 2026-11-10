---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["16 camt.085.001.02 IntraBalanceMovementPendingReportV02", "16.4 Message Building Blocks", "16.4.7 Movements <Mvmnts>", "16.4.7.2 Movement <Mvmnt>", "16.4.7.2.1 StatusAndReason <StsAndRsn>"]
file_pages: [374]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.085.001.02"]
---

# 16.4.7.2.1 StatusAndReason <StsAndRsn>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 374 to 374.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 374

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Linkages <Lnkgs> [0..*]  381
     ProcessingPosition <PrcgPos> [0..1] ± C19 382
     MessageNumber <MsgNb> [0..1] ± C16 382
     Reference <Ref> [1..1]  383
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 383
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 383
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 384
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 384
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 384
Or       PoolIdentification <PoolId> [1..1] Text 384
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 384
     ReferenceOwner <RefOwnr> [0..1] ± 384
   Priority <Prty> [0..1] ± 385
   MessageOriginator <MsgOrgtr> [0..1] ± 385
   CreationDateTime <CreDtTm> [1..1] DateTime 385
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 385
   SupplementaryData <SplmtryData> [0..*] ± C18 385
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
16.4.7.2.1  StatusAndReason <StsAndRsn>
Presence: [0..1]
Definition: Status and status reason of the transaction.
StatusAndReason <StsAndRsn> contains the following elements (see "PendingStatusAndReason2"
on page 437 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingStatus <PrcgSts> [0..*] ± 437
   SettlementStatus <SttlmSts> [0..*] ± C14 437
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
374 March 2024
```

