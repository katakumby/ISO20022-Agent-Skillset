---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["12 camt.081.001.02 IntraBalanceMovementModificationReportV02", "12.4 Message Building Blocks", "12.4.4 ReportOrError <RptOrErr>", "12.4.4.1 Modifications <Mods>", "12.4.4.1.5 Modification <Mod>", "12.4.4.1.5.7 RequestDetails <ReqDtls>", "12.4.4.1.5.7.6 ClearingChannel <ClrChanl>"]
file_pages: [273]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 12.4.4.1.5.7.6 ClearingChannel <ClrChanl>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 273 to 273.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 273

```text
• Meaning When True: Yes
• Meaning When False: No
12.4.4.1.5.7.6  ClearingChannel <ClrChanl>
Presence: [0..1]
Definition: Specifies the clearing channel to be used to process the payment instruction.
Datatype: "ClearingChannel2Code" on page 477
CodeName Name Definition
RTGS RealTimeGrossSettlementSystem Clearing channel is a real-time gross
settlement system.
RTNS RealTimeNetSettlementSystem Clearing channel is a real-time net
settlement system.
MPNS MassPaymentNetSystem Clearing channel is a mass payment net
settlement system.
BOOK BookTransfer Payment through internal book transfer.
12.4.4.1.5.7.7  Linkages <Lnkgs>
Presence: [0..*]
Definition: Information regarding the linkage requested.
Linkages <Lnkgs> contains the following Linkages57 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± C26 273
   MessageNumber <MsgNb> [0..1] ± C24 274
   Reference <Ref> [1..1]  274
{Or     SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 275
Or     IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 275
Or     IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 275
Or     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 275
Or     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 275
Or     PoolIdentification <PoolId> [1..1] Text 276
Or}     OtherTransactionIdentification <OthrTxId> [1..1] Text 276
   ReferenceOwner <RefOwnr> [0..1] ± 276
12.4.4.1.5.7.7.1  ProcessingPosition <PrcgPos>
Presence: [0..1]
Definition: When the transaction is to be executed relative to a linked transaction.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
273 March 2024
```

