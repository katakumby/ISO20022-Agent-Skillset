---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Miscellaneous", "7.1.18.25 Statement58", "7.1.18.25.3 HistoricData <HstrcData>"]
file_pages: [384]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.25.3 HistoricData <HstrcData>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 384 to 384.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 384

```text
7.1.18.25.3  HistoricData <HstrcData>
Presence: [1..1]
Definition: Specifies whether the data is either historical (true) or current (false).
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 553):
• Meaning When True: True
• Meaning When False: False
7.1.18.25.4  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 553):
• Meaning When True: Yes
• Meaning When False: No
7.1.18.25.5  SubAccountIndicator <SubAcctInd>
Presence: [1..1]
Definition: Indicates whether the statement reports holdings at subsafekeeping account level.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 553):
• Meaning When True: Yes
• Meaning When False: No
7.1.18.26  ModificationCancellationAllowed4Choice
Definition: Choice of format for the modification cancellation information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 384
Or}   Proprietary <Prtry> [1..1] ± 384
7.1.18.26.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether a third party is allowed to modify or cancel the transaction.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 553):
• Meaning When True: Yes
• Meaning When False: No
7.1.18.26.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Modification, cancellation allowed information expressed as a proprietary code.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 384 March 2026
```

