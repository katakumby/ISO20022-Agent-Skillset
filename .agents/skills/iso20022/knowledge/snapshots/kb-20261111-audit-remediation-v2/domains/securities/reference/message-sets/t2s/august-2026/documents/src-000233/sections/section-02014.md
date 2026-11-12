---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["79 semt.034.001.01 IntraPositionMovementPendingReportV01", "79.4 Message Building Blocks", "79.4.5 Movements <Mvmnts>", "79.4.5.2 Movement <Mvmnt>", "79.4.5.2.14 StatusDate <StsDt>"]
file_pages: [2742]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.034.001.01"]
---

# 79.4.5.2.14 StatusDate <StsDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2742 to 2742.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2742

```text
IntendedSettlementDate <IntnddSttlmDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
79.4.5.2.14  StatusDate <StsDt>
Presence: [0..1]
Definition: Date and time at which the status was assigned.
Datatype: "ISODateTime" on page 3320
79.4.5.2.15  AcknowledgedStatusTimeStamp <AckdStsTmStmp>
Presence: [0..1]
Definition: Time stamp on when the transaction is acknowledged.
Datatype: "ISODateTime" on page 3320
79.4.5.2.16  Linkages <Lnkgs>
Presence: [0..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
Linkages <Lnkgs> contains the following Linkages57 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± C21 2743
   MessageNumber <MsgNb> [0..1] ± C18 2743
   Reference <Ref> [1..1]  2743
{Or     SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 2744
Or     IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 2744
Or     IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 2744
Or     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 2744
Or     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 2744
Or     PoolIdentification <PoolId> [1..1] Text 2745
Or}     OtherTransactionIdentification <OthrTxId> [1..1] Text 2745
   ReferenceOwner <RefOwnr> [0..1] ± 2745
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities 2742 August 2026
```

