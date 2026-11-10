---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["23 camt.085.001.02 IntraBalanceMovementPendingReportV02", "23.4 Message Building Blocks", "23.4.7 Movements <Mvmnts>", "23.4.7.2 Movement <Mvmnt>", "23.4.7.2.1 StatusAndReason <StsAndRsn>"]
file_pages: [565]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.085.001.02"]
---

# 23.4.7.2.1 StatusAndReason <StsAndRsn>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 565 to 565.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 565

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Linkages <Lnkgs> [0..*]  572
     ProcessingPosition <PrcgPos> [0..1] ± C19 573
     MessageNumber <MsgNb> [0..1] ± C16 573
     Reference <Ref> [1..1]  574
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 574
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 574
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 575
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 575
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 575
Or       PoolIdentification <PoolId> [1..1] Text 575
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 575
     ReferenceOwner <RefOwnr> [0..1] ± 575
   Priority <Prty> [0..1] ± 576
   MessageOriginator <MsgOrgtr> [0..1] ± 576
   CreationDateTime <CreDtTm> [1..1] DateTime 576
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 576
   SupplementaryData <SplmtryData> [0..*] ± C18 576
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
23.4.7.2.1  StatusAndReason <StsAndRsn>
Presence: [0..1]
Definition: Status and status reason of the transaction.
StatusAndReason <StsAndRsn> contains the following elements (see "PendingStatusAndReason2"
on page 3136 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingStatus <PrcgSts> [0..*] ± 3137
   SettlementStatus <SttlmSts> [0..*] ± C14 3137
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities 565 August 2026
```

