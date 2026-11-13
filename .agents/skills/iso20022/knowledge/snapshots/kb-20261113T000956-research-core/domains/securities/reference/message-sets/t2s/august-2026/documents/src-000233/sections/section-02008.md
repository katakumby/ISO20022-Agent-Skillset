---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["79 semt.034.001.01 IntraPositionMovementPendingReportV01", "79.4 Message Building Blocks", "79.4.5 Movements <Mvmnts>"]
file_pages: [2732, 2733]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.034.001.01"]
---

# 79.4.5 Movements <Mvmnts>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2732 to 2733.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2732

```text
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
79.4.5 Movements <Mvmnts>
Presence: [0..*]
Definition: Identifies the transactions.
Impacted by: C19 "StatusAndReasonRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities 2732 August 2026
```

## File page 2733

```text
Movements <Mvmnts> contains the following IntraPositionPending11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatusAndReason <StsAndRsn> [0..1] ± 2734
   Movement <Mvmnt> [1..*]  C13 2734
     StatusAndReason <StsAndRsn> [0..1] ± 2736
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 2736
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 2736
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 2736
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 2737
     CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 2737
     PoolIdentification <PoolId> [0..1] Text 2737
     BalanceFrom <BalFr> [1..1] ± 2737
     BalanceTo <BalTo> [1..1] ± 2737
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C11,
C12,
C14
2737
     FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C4, C16 2739
     SettlementQuantity <SttlmQty> [1..1] ± 2741
     IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 2741
     StatusDate <StsDt> [0..1] DateTime 2742
     AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 2742
     Linkages <Lnkgs> [0..*]  2742
       ProcessingPosition <PrcgPos> [0..1] ± C21 2743
       MessageNumber <MsgNb> [0..1] ± C18 2743
       Reference <Ref> [1..1]  2743
{Or         SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 2744
Or         IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 2744
Or         IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 2744
Or         AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 2744
Or         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 2744
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities 2733 August 2026
```

