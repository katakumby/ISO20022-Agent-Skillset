---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.4 Message Building Blocks", "6.4.4 ProcessingStatus <PrcgSts>", "6.4.4.19 ProprietaryStatus <PrtrySts>"]
file_pages: [182]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6.4.4.19 ProprietaryStatus <PrtrySts>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 182 to 182.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 182

```text
Treated <Trtd> contains the following elements (see "ProprietaryReason4" on page 589 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 589
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 589
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
6.4.4.19  ProprietaryStatus <PrtrySts>
Presence: [0..1]
Definition: Provides a proprietary status and a proprietary reason of the processing status of the trade.
ProprietaryStatus <PrtrySts> contains the following elements (see "ProprietaryStatusAndReason6"
on page 588 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 588
   ProprietaryReason <PrtryRsn> [0..*] ± C4 588
6.4.5 MatchingStatus <MtchgSts>
Presence: [0..1]
Definition: Provides details on the matching status of a trade.
MatchingStatus <MtchgSts> contains one of the following MatchingStatus35Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Matched <Mtchd> [1..1] ± C4 182
Or   MatchedWithTolerance <MtchdWthTlrnce> [1..1] ± C4 183
Or   MatchingAlleged <MtchgAllgd> [1..1] ± 183
Or   Unmatched <Umtchd> [1..1] ± 184
Or}   ProprietaryStatus <PrtrySts> [0..1] ± 184
6.4.5.1  Matched <Mtchd>
Presence: [1..1]
Definition: Trade is matched.
Impacted by: C4 "AdditionalReasonInforrmationRule"
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 182 February 2025
```

