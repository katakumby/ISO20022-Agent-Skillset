---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.4 Message Building Blocks", "6.4.6 ReplacementProcessingStatus <RplcmntPrcgSts>", "6.4.6.1 Accepted <Accptd>"]
file_pages: [185]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6.4.6.1 Accepted <Accptd>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 185 to 185.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 185

```text
ReplacementProcessingStatus <RplcmntPrcgSts> contains one of the following
ReplacementProcessingStatus10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Accepted <Accptd> [1..1] ± C4 185
Or   Completed <Cmpltd> [1..1] ± C4 185
Or   Denied <Dnd> [1..1] ± C4 186
Or   InRepair <InRpr> [1..1] ± C4 186
Or   PartialReplacementAccepted <PrtlRplcmntAccptd> [1..1] ± C4 187
Or   Pending <Pdg> [1..1] ± C4 187
Or   ReceivedAtIntermediary <RcvdAtIntrmy> [1..1] ± C4 187
Or   ReceivedAtStockExchange <RcvdAtStockXchg> [1..1] ± C4 188
Or   Rejected <Rjctd> [1..1] ± C4 188
Or   ModificationRequested <ModReqd> [1..1] ± C4 189
Or}   ProprietaryStatus <PrtrySts> [0..1] ± 189
6.4.6.1  Accepted <Accptd>
Presence: [1..1]
Definition: Replacement of the trade is accepted.
Impacted by: C4 "AdditionalReasonInforrmationRule"
Accepted <Accptd> contains the following elements (see "ProprietaryReason4" on page 589 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 589
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 589
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
6.4.6.2  Completed <Cmpltd>
Presence: [1..1]
Definition: Replacement of the trade is completed.
Impacted by: C4 "AdditionalReasonInforrmationRule"
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 185 February 2025
```

