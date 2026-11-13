---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "76.4 Message Building Blocks", "76.4.3 Modifications <Mods>", "76.4.3.4 Modification <Mod>", "76.4.3.4.4 RequestReference <ReqRef>"]
file_pages: [2669, 2670]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 76.4.3.4.4 RequestReference <ReqRef>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2669 to 2670.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2669

```text
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus71Choice" on page 3152 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 3152
Or   Pending <Pdg> [1..1] ± 3153
Or   Rejected <Rjctd> [1..1] ± 3153
Or   Repair <Rpr> [1..1] ± 3153
Or   Denied <Dnd> [1..1] ± 3154
Or   Completed <Cmpltd> [1..1] ± C6 3154
Or}   Proprietary <Prtry> [1..1] ± 3155
76.4.3.4.4  RequestReference <ReqRef>
Presence: [1..1]
Definition: Unambiguous identification of the modification request.
Datatype: "Max35Text" on page 3328
76.4.3.4.5  StatusDate <StsDt>
Presence: [0..1]
Definition: Date and time at which the status was assigned.
Datatype: "ISODateTime" on page 3320
76.4.3.4.6  RequestDetails <ReqDtls>
Presence: [0..1]
Definition: Details of the request providing the changes and references of the instruction for which the
modification is requested.
Impacted by: C15 "ModificationRequestPresenceRule", C17 "OtherProcessingRule", C26
"SettlementConditionModificationApplicabilityRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2669 August 2026
```

## File page 2670

```text
RequestDetails <ReqDtls> contains the following RequestDetails33 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1]  C23 2671
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 2672
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 2672
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 2672
     CounterpartyMarketInfrastructureTransactionIdentifi
cation <CtrPtyMktInfrstrctrTxId>
[0..1] Text 2672
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 2672
     PoolIdentification <PoolId> [0..1] Text 2672
     CommonIdentification <CmonId> [0..1] Text 2673
     TradeIdentification <TradId> [0..1] Text 2673
   RestrictionReference <RstrctnRef> [0..*] ± 2673
   AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 2673
   RetainIndicator <RtnInd> [0..1] Indicator 2673
   Linkage <Lkg> [0..1] ± 2673
   Priority <Prty> [0..1] ± 2674
   OtherProcessing <OthrPrcg> [0..*] ± 2674
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 2674
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 2675
   HoldIndicator <HldInd> [0..1] ± 2675
   MatchingDenial <MtchgDnl> [0..1] ± 2675
   UnilateralSplit <UnltrlSplt> [0..1] ± 2675
   Linkages <Lnkgs> [0..*]  2676
     ProcessingPosition <PrcgPos> [0..1] ± C29 2676
     MessageNumber <MsgNb> [0..1] ± C27 2677
     Reference <Ref> [1..1]  2677
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 2678
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 2678
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 2678
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2670 August 2026
```

