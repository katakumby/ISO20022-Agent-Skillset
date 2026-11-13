---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["10 camt.072.001.02 IntraBalanceMovementModificationRequestV02", "10.4 Message Building Blocks", "10.4.5 RequestDetails <ReqDtls>", "10.4.5.6 ClearingChannel <ClrChanl>"]
file_pages: [161]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.072.001.02"]
---

# 10.4.5.6 ClearingChannel <ClrChanl>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 161 to 161.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 161

```text
Definition: Specifies whether partial settlement is allowed.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
10.4.5.6  ClearingChannel <ClrChanl>
Presence: [0..1]
Definition: Specifies the clearing channel to be used to process the payment instruction.
Datatype: "ClearingChannel2Code" on page 3221
CodeName Name Definition
RTGS RealTimeGrossSettlementSystem Clearing channel is a real-time gross
settlement system.
RTNS RealTimeNetSettlementSystem Clearing channel is a real-time net
settlement system.
MPNS MassPaymentNetSystem Clearing channel is a mass payment net
settlement system.
BOOK BookTransfer Payment through internal book transfer.
10.4.5.7  Linkages <Lnkgs>
Presence: [0..*]
Definition: Information regarding the linkage requested.
Linkages <Lnkgs> contains the following Linkages57 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± C16 162
   MessageNumber <MsgNb> [0..1] ± C14 162
   Reference <Ref> [1..1]  162
{Or     SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 163
Or     IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 163
Or     IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 163
Or     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 163
Or     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 163
Or     PoolIdentification <PoolId> [1..1] Text 164
Or}     OtherTransactionIdentification <OthrTxId> [1..1] Text 164
   ReferenceOwner <RefOwnr> [0..1] ± 164
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities 161 August 2026
```

