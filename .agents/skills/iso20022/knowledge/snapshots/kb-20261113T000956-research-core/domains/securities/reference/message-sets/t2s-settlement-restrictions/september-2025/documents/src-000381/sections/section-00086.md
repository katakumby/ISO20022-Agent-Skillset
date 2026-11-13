---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "5.4 Message Building Blocks", "5.4.3 Modifications <Mods>", "5.4.3.4 Modification <Mod>", "5.4.3.4.4 RequestReference <ReqRef>"]
file_pages: [114, 115]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 5.4.3.4.4 RequestReference <ReqRef>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 114 to 115.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 114

```text
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
5.4.3.4.4  RequestReference <ReqRef>
Presence: [1..1]
Definition: Unambiguous identification of the modification request.
Datatype: "Max35Text" on page 345
5.4.3.4.5  StatusDate <StsDt>
Presence: [0..1]
Definition: Date and time at which the status was assigned.
Datatype: "ISODateTime" on page 340
5.4.3.4.6  RequestDetails <ReqDtls>
Presence: [0..1]
Definition: Details of the request providing the changes and references of the instruction for which the
modification is requested.
Impacted by: C15 "ModificationRequestPresenceRule", C17 "OtherProcessingRule", C26
"SettlementConditionModificationApplicabilityRule"
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 114 September 2025
```

## File page 115

```text
RequestDetails <ReqDtls> contains the following RequestDetails33 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
     CounterpartyMarketInfrastructureTransactionIdentifi
cation <CtrPtyMktInfrstrctrTxId>
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
     MessageNumber <MsgNb> [0..1] ± C27 122
     Reference <Ref> [1..1]  122
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 123
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 123
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 123
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 115 September 2025
```

