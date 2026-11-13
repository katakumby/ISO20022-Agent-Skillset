---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "76.4 Message Building Blocks", "76.4.3 Modifications <Mods>", "76.4.3.4 Modification <Mod>", "76.4.3.4.7 Underlying <Undrlyg>", "76.4.3.4.7.2 SettlementTransaction <SttlmTx>", "76.4.3.4.7.2.7 ReceivingSettlementParties <RcvgSttlmPties>"]
file_pages: [2687]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 76.4.3.4.7.2.7 ReceivingSettlementParties <RcvgSttlmPties>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2687 to 2687.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2687

```text
Constraints
• Party2PresenceRule
If Party2 is present, then Party1 must be present.
On Condition
    /Party2 is present
Following Must be True
    /Party1 Must be present
• Party3PresenceRule
If Party3 is present, then Party2 must be present.
On Condition
    /Party3 is present
Following Must be True
    /Party2 Must be present
• Party4PresenceRule
If Party4 is present, then Party3 must be present.
On Condition
    /Party4 is present
Following Must be True
    /Party3 Must be present
• Party5PresenceRule
If Party5 is present, then Party4 must be present.
On Condition
    /Party5 is present
Following Must be True
    /Party4 Must be present
76.4.3.4.7.2.7  ReceivingSettlementParties <RcvgSttlmPties>
Presence: [0..1]
Definition: Identifies the chain of receiving settlement parties.
Impacted by: C18 "Party2PresenceRule", C19 "Party3PresenceRule", C20 "Party4PresenceRule", C21
"Party5PresenceRule"
ReceivingSettlementParties <RcvgSttlmPties> contains the following elements (see
"SettlementParties78" on page 3115 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 3115
   Party1 <Pty1> [0..1] ± 3116
   Party2 <Pty2> [0..1] ± 3116
   Party3 <Pty3> [0..1] ± 3117
   Party4 <Pty4> [0..1] ± 3117
   Party5 <Pty5> [0..1] ± 3117
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2687 August 2026
```

