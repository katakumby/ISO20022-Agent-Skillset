---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.4 Message Building Blocks", "6.4.7 CancellationProcessingStatus <CxlPrcgSts>", "6.4.7.1 CancellationPending <CxlPdg>"]
file_pages: [190]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6.4.7.1 CancellationPending <CxlPdg>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 190 to 190.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 190

```text
CancellationProcessingStatus <CxlPrcgSts> contains one of the following
CancellationProcessingStatus10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CancellationPending <CxlPdg> [1..1] ± 190
Or   CancellationRequested <CxlReqd> [1..1] ± C4 190
Or   CancellationCompleted <CxlCmpltd> [1..1] ± C4 191
Or}   ProprietaryStatus <PrtrySts> [0..1] ± 191
6.4.7.1  CancellationPending <CxlPdg>
Presence: [1..1]
Definition: Trade is in cancelation pending.
CancellationPending <CxlPdg> contains one of the following elements (see
"CancellationReason39Choice" on page 603 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 603
Or}   Reason <Rsn> [1..*]  603
     Code <Cd> [1..1]  604
{Or       Code <Cd> [1..1] CodeSet 604
Or}       Proprietary <Prtry> [1..1] ± 604
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 604
6.4.7.2  CancellationRequested <CxlReqd>
Presence: [1..1]
Definition: Cancelation request for the trade.
Impacted by: C4 "AdditionalReasonInforrmationRule"
CancellationRequested <CxlReqd> contains the following elements (see "ProprietaryReason4" on
page 589 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 589
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 589
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 190 February 2025
```

