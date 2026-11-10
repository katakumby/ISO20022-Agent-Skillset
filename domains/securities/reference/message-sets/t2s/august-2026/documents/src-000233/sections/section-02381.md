---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.31 CancellationStatus14Choice", "82.1.30.31.2 Reason <Rsn>"]
file_pages: [3168]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.31.2 Reason <Rsn>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3168 to 3168.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3168

```text
82.1.30.31.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the cancellation status.
Reason <Rsn> contains the following elements (see "CancellationReason9" on page 3135 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 3135
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3135
82.1.30.32  MatchingStatus24Choice
Definition: Choice of format for the matching status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Matched <Mtchd> [1..1] ± C6 3168
Or   Unmatched <Umtchd> [1..1]  3169
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3169
Or}     Reason <Rsn> [1..*]  3169
       Code <Cd> [1..1]  3169
{Or         Code <Cd> [1..1] CodeSet 3170
Or}         Proprietary <Prtry> [1..1] ± 3172
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3172
Or}   Proprietary <Prtry> [1..1] ± 3172
82.1.30.32.1  Matched <Mtchd>
Presence: [1..1]
Definition: Status is matched.
Impacted by: C6 "AdditionalReasonInforrmationRule"
Matched <Mtchd> contains the following elements (see "ProprietaryReason4" on page 3139 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 3140
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3140
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3168 August 2026
```

