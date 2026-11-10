---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.4 Message Building Blocks", "6.4.5 MatchingStatus <MtchgSts>", "6.4.5.4 Unmatched <Umtchd>"]
file_pages: [184]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6.4.5.4 Unmatched <Umtchd>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 184 to 184.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 184

```text
MatchingAlleged <MtchgAllgd> contains one of the following elements (see
"MatchingReason5Choice" on page 598 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..*]  598
     Code <Cd> [1..1]  598
{Or       Code <Cd> [1..1] CodeSet 599
Or}       Proprietary <Prtry> [1..1] ± 599
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 599
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 599
6.4.5.4  Unmatched <Umtchd>
Presence: [1..1]
Definition: Trade is unmatched or mismatched.
Unmatched <Umtchd> contains one of the following elements (see "MatchingReason6Choice" on
page 592 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..*]  593
     Code <Cd> [1..1] ± 593
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 593
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 593
6.4.5.5  ProprietaryStatus <PrtrySts>
Presence: [0..1]
Definition: Provides a proprietary status and a proprietary reason of the processing status of the trade.
ProprietaryStatus <PrtrySts> contains the following elements (see "ProprietaryStatusAndReason6"
on page 588 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 588
   ProprietaryReason <PrtryRsn> [0..*] ± C4 588
6.4.6 ReplacementProcessingStatus <RplcmntPrcgSts>
Presence: [0..1]
Definition: Provides the replacement processing status of a trade.
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 184 February 2025
```

