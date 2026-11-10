---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.4 Message Building Blocks", "6.4.3 AffirmationStatus <AffirmSts>", "6.4.3.3 ProprietaryStatus <PrtrySts>"]
file_pages: [174]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6.4.3.3 ProprietaryStatus <PrtrySts>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 174 to 174.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 174

```text
6.4.3.3  ProprietaryStatus <PrtrySts>
Presence: [0..1]
Definition: Provides a proprietary status and a proprietary reason of the affirmation of the trade.
ProprietaryStatus <PrtrySts> contains the following elements (see "ProprietaryStatusAndReason6"
on page 588 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 588
   ProprietaryReason <PrtryRsn> [0..*] ± C4 588
6.4.4 ProcessingStatus <PrcgSts>
Presence: [0..1]
Definition: Provides the processing status of a trade.
ProcessingStatus <PrcgSts> contains one of the following ProcessingStatus98Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± C4 175
Or   AlreadyMatchedAndAffirmed <AlrdyMtchdAndAffrmd> [1..1] ± C4 175
Or   DefaultAction <DfltActn> [1..1] ± C4 175
Or   Done <Done> [1..1] ± C4 176
Or   ForcedRejection <ForcdRjctn> [1..1] ± C4 176
Or   FullyExecutedConfirmationSent <FullyExctdConfSnt> [1..1] ± C4 177
Or   Future <Futr> [1..1] ± C4 177
Or   Generated <Gnrtd> [1..1] ± C4 177
Or   InRepair <InRpr> [1..1] ± 178
Or   NoInstruction <NoInstr> [1..1] ± C4 178
Or   OpenOrder <OpnOrdr> [1..1] ± C4 179
Or   PendingProcessing <PdgPrcg> [1..1] ± 179
Or   ReceivedAtIntermediary <RcvdAtIntrmy> [1..1] ± C4 179
Or   Rejected <Rjctd> [1..1] ± 180
Or   SettlementInstructionSent <SttlmInstrSnt> [1..1] ± C4 180
Or   StandingInstruction <StgInstr> [1..1] ± C4 181
Or   TradingSuspendedByStockExchange
<TradgSspdByStockXchg>
[1..1] ± C4 181
Or   Treated <Trtd> [1..1] ± C4 181
Or}   ProprietaryStatus <PrtrySts> [0..1] ± 182
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 174 February 2025
```

