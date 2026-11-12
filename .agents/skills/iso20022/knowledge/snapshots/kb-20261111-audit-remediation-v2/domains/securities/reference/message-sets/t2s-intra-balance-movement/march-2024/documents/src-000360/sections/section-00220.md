---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["12 camt.081.001.02 IntraBalanceMovementModificationReportV02", "12.4 Message Building Blocks", "12.4.4 ReportOrError <RptOrErr>", "12.4.4.1 Modifications <Mods>", "12.4.4.1.5 Modification <Mod>", "12.4.4.1.5.6 StatusDate <StsDt>"]
file_pages: [269, 270]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 12.4.4.1.5.6 StatusDate <StsDt>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 269 to 270.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 269

```text
12.4.4.1.5.6  StatusDate <StsDt>
Presence: [0..1]
Definition: Date and time at which the status was assigned.
Datatype: "ISODateTime" on page 493
12.4.4.1.5.7  RequestDetails <ReqDtls>
Presence: [0..1]
Definition: Details of the request providing the changes and references of the instruction for which the
modification is requested.
Impacted by: C18 "ModificationRequestPresenceRule", C19 "OtherProcessingRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
269 March 2024
```

## File page 270

```text
RequestDetails <ReqDtls> contains the following RequestDetails22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1]  271
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 271
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 271
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 271
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 271
     PoolIdentification <PoolId> [0..1] Text 272
   Linkage <Lkg> [0..1] ± 272
   Priority <Prty> [0..1] ± 272
   OtherProcessing <OthrPrcg> [0..*] ± 272
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] Indicator 272
   ClearingChannel <ClrChanl> [0..1] CodeSet 273
   Linkages <Lnkgs> [0..*]  273
     ProcessingPosition <PrcgPos> [0..1] ± C26 273
     MessageNumber <MsgNb> [0..1] ± C24 274
     Reference <Ref> [1..1]  274
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 275
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 275
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 275
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 275
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 275
Or       PoolIdentification <PoolId> [1..1] Text 276
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 276
     ReferenceOwner <RefOwnr> [0..1] ± 276
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
270 March 2024
```

