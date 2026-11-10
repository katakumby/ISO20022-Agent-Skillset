---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03", "5.4 Message Building Blocks", "5.4.3 Status <Sts>", "5.4.3.2 UnaffirmedReason <UaffrmdRsn>"]
file_pages: [152]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.030.001.03"]
---

# 5.4.3.2 UnaffirmedReason <UaffrmdRsn>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 152 to 152.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 152

```text
AffirmationStatus <AffirmSts> contains one of the following elements (see
"AffirmationStatus10Choice" on page 595 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 595
Or}   Proprietary <Prtry> [1..1] ± 595
5.4.3.2  UnaffirmedReason <UaffrmdRsn>
Presence: [0..1]
Definition: Specifies the reason why the instruction has an unaffirmed status.
UnaffirmedReason <UaffrmdRsn> contains one of the following elements (see
"UnaffirmedReason3Choice" on page 594 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 594
Or}   Proprietary <Prtry> [1..1] ± 595
5.4.3.3  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional information about the reason in narrative form.
Datatype: "Max210Text" on page 668
5.4.4 ClearingDetails <ClrDtls>
Presence: [0..1]
Definition: Provides clearing member information.
ClearingDetails <ClrDtls> contains the following Clearing6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingMember <ClrMmb> [1..*] ± 152
   ClearingSegment <ClrSgmt> [0..1] ± 153
5.4.4.1  ClearingMember <ClrMmb>
Presence: [1..*]
Definition: Provides details about the clearing member identification and account.
Approved by the Securities SEG on 13 February 2025 setr.030.001.03
SecuritiesTradeConfirmationResponseV03
Post Trade Matching - Maintenance 2024 - 2025 152 February 2025
```

