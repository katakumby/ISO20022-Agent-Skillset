---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.2 Structure"]
file_pages: [164, 165]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6.2 Structure

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 164 to 165.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 164

```text
6.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesTradConfStsAdvc> [1..1]  C36
   Identification <Id> [1..1]  170
     TransactionIdentification <TxId> [1..1] Text 171
   References <Refs> [1..*]  171
     MessageNumber <MsgNb> [0..1] ± C35 171
     Reference <Ref> [1..1] ± C22 172
   AffirmationStatus <AffirmSts> [0..1]  173
{Or     Affirmed <Affrmd> [1..1] ± C4 173
Or     Unaffirmed <Uaffrmd> [1..1] ± 173
Or}     ProprietaryStatus <PrtrySts> [0..1] ± 174
   ProcessingStatus <PrcgSts> [0..1]  174
{Or     AcknowledgedAccepted <AckdAccptd> [1..1] ± C4 175
Or     AlreadyMatchedAndAffirmed <AlrdyMtchdAndAffrmd> [1..1] ± C4 175
Or     DefaultAction <DfltActn> [1..1] ± C4 175
Or     Done <Done> [1..1] ± C4 176
Or     ForcedRejection <ForcdRjctn> [1..1] ± C4 176
Or     FullyExecutedConfirmationSent <FullyExctdConfSnt> [1..1] ± C4 177
Or     Future <Futr> [1..1] ± C4 177
Or     Generated <Gnrtd> [1..1] ± C4 177
Or     InRepair <InRpr> [1..1] ± 178
Or     NoInstruction <NoInstr> [1..1] ± C4 178
Or     OpenOrder <OpnOrdr> [1..1] ± C4 179
Or     PendingProcessing <PdgPrcg> [1..1] ± 179
Or     ReceivedAtIntermediary <RcvdAtIntrmy> [1..1] ± C4 179
Or     Rejected <Rjctd> [1..1] ± 180
Or     SettlementInstructionSent <SttlmInstrSnt> [1..1] ± C4 180
Or     StandingInstruction <StgInstr> [1..1] ± C4 181
Or     TradingSuspendedByStockExchange
<TradgSspdByStockXchg>
[1..1] ± C4 181
Or     Treated <Trtd> [1..1] ± C4 181
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 164 February 2025
```

## File page 165

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}     ProprietaryStatus <PrtrySts> [0..1] ± 182
   MatchingStatus <MtchgSts> [0..1]  182
{Or     Matched <Mtchd> [1..1] ± C4 182
Or     MatchedWithTolerance <MtchdWthTlrnce> [1..1] ± C4 183
Or     MatchingAlleged <MtchgAllgd> [1..1] ± 183
Or     Unmatched <Umtchd> [1..1] ± 184
Or}     ProprietaryStatus <PrtrySts> [0..1] ± 184
   ReplacementProcessingStatus <RplcmntPrcgSts> [0..1]  184
{Or     Accepted <Accptd> [1..1] ± C4 185
Or     Completed <Cmpltd> [1..1] ± C4 185
Or     Denied <Dnd> [1..1] ± C4 186
Or     InRepair <InRpr> [1..1] ± C4 186
Or     PartialReplacementAccepted <PrtlRplcmntAccptd> [1..1] ± C4 187
Or     Pending <Pdg> [1..1] ± C4 187
Or     ReceivedAtIntermediary <RcvdAtIntrmy> [1..1] ± C4 187
Or     ReceivedAtStockExchange <RcvdAtStockXchg> [1..1] ± C4 188
Or     Rejected <Rjctd> [1..1] ± C4 188
Or     ModificationRequested <ModReqd> [1..1] ± C4 189
Or}     ProprietaryStatus <PrtrySts> [0..1] ± 189
   CancellationProcessingStatus <CxlPrcgSts> [0..1]  189
{Or     CancellationPending <CxlPdg> [1..1] ± 190
Or     CancellationRequested <CxlReqd> [1..1] ± C4 190
Or     CancellationCompleted <CxlCmpltd> [1..1] ± C4 191
Or}     ProprietaryStatus <PrtrySts> [0..1] ± 191
   PartyTradingDetails <PtyTradgDtls> [0..1] ± C11,
C32,
C38
191
   CounterpartyTradingDetails <CtrPtyTradgDtls> [0..1] ± C11,
C32,
C38
194
   ConfirmationParties <ConfPties> [0..*]  197
     Investor <Invstr> [0..*] ± C18 198
     Buyer <Buyr> [0..1] ± 199
     Borrower <Brrwr> [0..1] ± 200
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 165 February 2025
```

