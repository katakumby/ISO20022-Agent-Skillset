---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["19 camt.081.001.02 IntraBalanceMovementModificationReportV02", "19.4 Message Building Blocks", "19.4.4 ReportOrError <RptOrErr>", "19.4.4.1 Modifications <Mods>", "19.4.4.1.5 Modification <Mod>", "19.4.4.1.5.6 StatusDate <StsDt>"]
file_pages: [460, 461]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 19.4.4.1.5.6 StatusDate <StsDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 460 to 461.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 460

```text
19.4.4.1.5.6  StatusDate <StsDt>
Presence: [0..1]
Definition: Date and time at which the status was assigned.
Datatype: "ISODateTime" on page 3320
19.4.4.1.5.7  RequestDetails <ReqDtls>
Presence: [0..1]
Definition: Details of the request providing the changes and references of the instruction for which the
modification is requested.
Impacted by: C18 "ModificationRequestPresenceRule", C19 "OtherProcessingRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 460 August 2026
```

## File page 461

```text
RequestDetails <ReqDtls> contains the following RequestDetails22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1]  462
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 462
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 462
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 462
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 462
     PoolIdentification <PoolId> [0..1] Text 463
   Linkage <Lkg> [0..1] ± 463
   Priority <Prty> [0..1] ± 463
   OtherProcessing <OthrPrcg> [0..*] ± 463
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] Indicator 463
   ClearingChannel <ClrChanl> [0..1] CodeSet 464
   Linkages <Lnkgs> [0..*]  464
     ProcessingPosition <PrcgPos> [0..1] ± C26 464
     MessageNumber <MsgNb> [0..1] ± C24 465
     Reference <Ref> [1..1]  465
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 466
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 466
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 466
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 466
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 466
Or       PoolIdentification <PoolId> [1..1] Text 467
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 467
     ReferenceOwner <RefOwnr> [0..1] ± 467
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 461 August 2026
```

