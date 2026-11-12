---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "5.4 Message Building Blocks", "5.4.3 Modifications <Mods>", "5.4.3.3 ProcessingStatus <PrcgSts>"]
file_pages: [110, 111, 112]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 5.4.3.3 ProcessingStatus <PrcgSts>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 110 to 112.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 110

```text
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 193 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 193
   Type <Tp> [0..1] ± 193
   Name <Nm> [0..1] Text 193
5.4.3.3  ProcessingStatus <PrcgSts>
Presence: [0..1]
Definition: Status and status reason of the transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus71Choice" on page 279 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 280
Or   Pending <Pdg> [1..1] ± 280
Or   Rejected <Rjctd> [1..1] ± 280
Or   Repair <Rpr> [1..1] ± 281
Or   Denied <Dnd> [1..1] ± 281
Or   Completed <Cmpltd> [1..1] ± C5 282
Or}   Proprietary <Prtry> [1..1] ± 282
5.4.3.4  Modification <Mod>
Presence: [1..*]
Definition: Identifies the individual transaction.
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 110 September 2025
```

## File page 111

```text
Modification <Mod> contains the following SecuritiesModificationTransaction2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [0..1] ± 113
   SafekeepingAccount <SfkpgAcct> [0..1] ± 113
   ProcessingStatus <PrcgSts> [0..1] ± 113
   RequestReference <ReqRef> [1..1] Text 114
   StatusDate <StsDt> [0..1] DateTime 114
   RequestDetails <ReqDtls> [0..1]  C15,
C17,
C26
114
     Reference <Ref> [1..1]  C23 116
       AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 117
       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 117
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 117
       CounterpartyMarketInfrastructureTransactionIdenti
fication <CtrPtyMktInfrstrctrTxId>
[0..1] Text 117
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 117
       PoolIdentification <PoolId> [0..1] Text 117
       CommonIdentification <CmonId> [0..1] Text 118
       TradeIdentification <TradId> [0..1] Text 118
     RestrictionReference <RstrctnRef> [0..*] ± 118
     AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 118
     RetainIndicator <RtnInd> [0..1] Indicator 118
     Linkage <Lkg> [0..1] ± 118
     Priority <Prty> [0..1] ± 119
     OtherProcessing <OthrPrcg> [0..*] ± 119
     PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 119
     SecuritiesRTGS <SctiesRTGS> [0..1] ± 120
     HoldIndicator <HldInd> [0..1] ± 120
     MatchingDenial <MtchgDnl> [0..1] ± 120
     UnilateralSplit <UnltrlSplt> [0..1] ± 120
     Linkages <Lnkgs> [0..*]  121
       ProcessingPosition <PrcgPos> [0..1] ± C29 121
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 111 September 2025
```

## File page 112

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       MessageNumber <MsgNb> [0..1] ± C27 122
       Reference <Ref> [1..1]  122
{Or         SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 123
Or         IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 123
Or         IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 123
Or         AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 123
Or         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 123
Or         PoolIdentification <PoolId> [1..1] Text 124
Or}         OtherTransactionIdentification <OthrTxId> [1..1] Text 124
       ReferenceOwner <RefOwnr> [0..1] ± 124
   Underlying <Undrlyg> [0..1]  124
{Or     IntraPositionMovement <IntraPosMvmnt> [1..1]  125
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C16
126
       SettlementQuantity <SttlmQty> [1..1] ± 127
       SettlementDate <SttlmDt> [1..1] ± 127
       BalanceFrom <BalFr> [0..1] ± 127
       BalanceTo <BalTo> [0..1] ± 128
       SecuritiesSubBalanceIdentification
<SctiesSubBalId>
[0..1] ± 128
       Priority <Prty> [0..1] ± 128
Or}     SettlementTransaction <SttlmTx> [1..1]  128
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C16
129
       SettlementQuantity <SttlmQty> [1..1] ± 130
       SettlementAmount <SttlmAmt> [0..1] ± 130
       TradeDate <TradDt> [0..1] ± 131
       SettlementDate <SttlmDt> [1..1] ± 131
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 112 September 2025
```

