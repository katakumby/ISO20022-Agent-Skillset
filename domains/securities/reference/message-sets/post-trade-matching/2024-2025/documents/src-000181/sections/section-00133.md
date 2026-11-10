---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.4 Message Building Blocks", "6.4.3 AffirmationStatus <AffirmSts>"]
file_pages: [173]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6.4.3 AffirmationStatus <AffirmSts>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 173 to 173.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 173

```text
ComplianceIdentification and CancellationRequestIdentification must not appear more than once in
the message.
6.4.3 AffirmationStatus <AffirmSts>
Presence: [0..1]
Definition: Provides details on the affitrmation status of a trade.
AffirmationStatus <AffirmSts> contains one of the following AffirmationStatus11Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Affirmed <Affrmd> [1..1] ± C4 173
Or   Unaffirmed <Uaffrmd> [1..1] ± 173
Or}   ProprietaryStatus <PrtrySts> [0..1] ± 174
6.4.3.1  Affirmed <Affrmd>
Presence: [1..1]
Definition: Status of affirmation of a trade.
Impacted by: C4 "AdditionalReasonInforrmationRule"
Affirmed <Affrmd> contains the following elements (see "ProprietaryReason4" on page 589 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 589
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 589
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
6.4.3.2  Unaffirmed <Uaffrmd>
Presence: [1..1]
Definition: Trade has been unaffirmed.
Unaffirmed <Uaffrmd> contains one of the following elements (see "AffirmationReason2Choice" on
page 597 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..*]  597
     Code <Cd> [1..1] ± 597
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 597
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 598
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 173 February 2025
```

