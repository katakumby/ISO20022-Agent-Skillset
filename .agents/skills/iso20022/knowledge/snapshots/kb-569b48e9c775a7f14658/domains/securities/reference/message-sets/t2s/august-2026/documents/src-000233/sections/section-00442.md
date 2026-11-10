---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["23 camt.085.001.02 IntraBalanceMovementPendingReportV02", "23.4 Message Building Blocks", "23.4.7 Movements <Mvmnts>", "23.4.7.1 StatusAndReason <StsAndRsn>"]
file_pages: [562]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.085.001.02"]
---

# 23.4.7.1 StatusAndReason <StsAndRsn>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 562 to 562.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 562

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     StatusDate <StsDt> [0..1] DateTime 572
     CashSubBalanceIdentification <CshSubBalId> [0..1] ± 572
     Linkages <Lnkgs> [0..*]  572
       ProcessingPosition <PrcgPos> [0..1] ± C19 573
       MessageNumber <MsgNb> [0..1] ± C16 573
       Reference <Ref> [1..1]  574
{Or         SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 574
Or         IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 574
Or         IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 575
Or         AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 575
Or         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 575
Or         PoolIdentification <PoolId> [1..1] Text 575
Or}         OtherTransactionIdentification <OthrTxId> [1..1] Text 575
       ReferenceOwner <RefOwnr> [0..1] ± 575
     Priority <Prty> [0..1] ± 576
     MessageOriginator <MsgOrgtr> [0..1] ± 576
     CreationDateTime <CreDtTm> [1..1] DateTime 576
     InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 576
     SupplementaryData <SplmtryData> [0..*] ± C18 576
Constraints
• StatusAndReasonRule
StatusAndReason must be present or Movement(*)/StatusAndReason must be present, but not both.
23.4.7.1  StatusAndReason <StsAndRsn>
Presence: [0..1]
Definition: Status and status reason of the transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities 562 August 2026
```

