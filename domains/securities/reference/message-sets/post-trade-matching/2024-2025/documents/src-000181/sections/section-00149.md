---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.4 Message Building Blocks", "6.4.6 ReplacementProcessingStatus <RplcmntPrcgSts>", "6.4.6.10 ModificationRequested <ModReqd>"]
file_pages: [189]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6.4.6.10 ModificationRequested <ModReqd>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 189 to 189.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 189

```text
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
6.4.6.10  ModificationRequested <ModReqd>
Presence: [1..1]
Definition: Replacement of the trade is Modification Requested.
Impacted by: C4 "AdditionalReasonInforrmationRule"
ModificationRequested <ModReqd> contains the following elements (see "ProprietaryReason4" on
page 589 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 589
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 589
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
6.4.6.11  ProprietaryStatus <PrtrySts>
Presence: [0..1]
Definition: Provides a proprietary status and a proprietary reason of the processing status of the trade.
ProprietaryStatus <PrtrySts> contains the following elements (see "ProprietaryStatusAndReason6"
on page 588 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 588
   ProprietaryReason <PrtryRsn> [0..*] ± C4 588
6.4.7 CancellationProcessingStatus <CxlPrcgSts>
Presence: [0..1]
Definition: Provides details on the cancellation status of a trade.
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 189 February 2025
```

