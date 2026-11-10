---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["9 seev.037.001.17 CorporateActionMovementReversalAdviceV17", "9.4 Message Building Blocks", "9.4.8 CorporateActionDetails <CorpActnDtls>", "9.4.8.4 FollowingEventTypeIndicator <FllwngEvtTpInd>"]
file_pages: [681]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.037.001.17"]
---

# 9.4.8.4 FollowingEventTypeIndicator <FllwngEvtTpInd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 681 to 681.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 681

```text
AdditionalBusinessProcessIndicator <AddtlBizPrcInd> contains one of the following elements (see
"AdditionalBusinessProcessFormat11Choice" on page 972 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 972
Or}   Proprietary <Prtry> [1..1] ± 973
9.4.8.4  FollowingEventTypeIndicator <FllwngEvtTpInd>
Presence: [0..1]
Definition: Specifies the event type of the following event.
FollowingEventTypeIndicator <FllwngEvtTpInd> contains one of the following elements (see
"IntermediateSecuritiesDistributionTypeFormat19Choice" on page 986 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 986
Or}   Proprietary <Prtry> [1..1] ± 987
9.4.8.5  LotteryType <LtryTp>
Presence: [0..1]
Definition: Specifies the type of lottery announced.
LotteryType <LtryTp> contains one of the following elements (see "LotteryTypeFormat4Choice" on
page 979 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 979
Or}   Proprietary <Prtry> [1..1] ± 979
9.4.9 CorporateActionConfirmationDetails
<CorpActnConfDtls>
Presence: [1..1]
Definition: Information about the corporate action option.
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 681 February 2026
```

