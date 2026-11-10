---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["22 camt.084.001.02 IntraBalanceMovementPostingReportV02", "22.4 Message Building Blocks", "22.4.7 SubBalance <SubBal>", "22.4.7.2 Movement <Mvmnt>", "22.4.7.2.13 CashSubBalanceIdentification <CshSubBalId>"]
file_pages: [544]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 22.4.7.2.13 CashSubBalanceIdentification <CshSubBalId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 544 to 544.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 544

```text
Datatype: "ISODateTime" on page 3320
22.4.7.2.13  CashSubBalanceIdentification <CshSubBalId>
Presence: [0..1]
Definition: Number identifying a lot constituting the sub-balance.
CashSubBalanceIdentification <CshSubBalId> contains the following elements (see
"GenericIdentification37" on page 2965 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
22.4.7.2.14  Linkages <Lnkgs>
Presence: [0..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
Linkages <Lnkgs> contains the following Linkages57 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± C16 544
   MessageNumber <MsgNb> [0..1] ± C14 545
   Reference <Ref> [1..1]  545
{Or     SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 546
Or     IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 546
Or     IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 546
Or     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 546
Or     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 546
Or     PoolIdentification <PoolId> [1..1] Text 547
Or}     OtherTransactionIdentification <OthrTxId> [1..1] Text 547
   ReferenceOwner <RefOwnr> [0..1] ± 547
22.4.7.2.14.1  ProcessingPosition <PrcgPos>
Presence: [0..1]
Definition: When the transaction is to be executed relative to a linked transaction.
Impacted by: C16 "WithLinkageRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities 544 August 2026
```

