---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.4 Message Building Blocks", "6.4.4 ProcessingStatus <PrcgSts>", "6.4.4.6 FullyExecutedConfirmationSent <FullyExctdConfSnt>"]
file_pages: [177]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6.4.4.6 FullyExecutedConfirmationSent <FullyExctdConfSnt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 177 to 177.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 177

```text
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
6.4.4.6  FullyExecutedConfirmationSent <FullyExctdConfSnt>
Presence: [1..1]
Definition: The trade is fully executed and the confirmation is sent.
Impacted by: C4 "AdditionalReasonInforrmationRule"
FullyExecutedConfirmationSent <FullyExctdConfSnt> contains the following elements (see
"ProprietaryReason4" on page 589 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 589
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 589
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
6.4.4.7  Future <Futr>
Presence: [1..1]
Definition: Trade is future.
Impacted by: C4 "AdditionalReasonInforrmationRule"
Future <Futr> contains the following elements (see "ProprietaryReason4" on page 589 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 589
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 589
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
6.4.4.8  Generated <Gnrtd>
Presence: [1..1]
Definition: Trade is generated.
Impacted by: C4 "AdditionalReasonInforrmationRule"
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 177 February 2025
```

