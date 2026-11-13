---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.14 Miscellaneous", "9.1.14.15 HoldIndicator6", "9.1.14.15.1 Indicator <Ind>"]
file_pages: [244]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.14.15.1 Indicator <Ind>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 244 to 244.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 244

```text
9.1.14.15.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether the transaction is on hold/blocked/frozen.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 342):
• Meaning When True: Yes
• Meaning When False: No
9.1.14.15.2  Reason <Rsn>
Presence: [0..*]
Definition: Specifies the reason of the registration status.
Reason <Rsn> contains the following elements (see "RegistrationReason5" on page 238 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  239
{Or     Code <Cd> [1..1] CodeSet 239
Or}     Proprietary <Prtry> [1..1] ± 239
   AdditionalInformation <AddtlInf> [0..1] Text 240
9.1.14.16  ProcessingPosition7Choice
Definition: Choice of format for the processing position.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 244
Or}   Proprietary <Prtry> [1..1] ± 245
Constraints
• WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and which
must be executed together. Even if one single transactions/instructions/notifications can not be
executed, then all the other transactions/instructions/notifications must also be kept pending.
Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/instructions/
notifications.
9.1.14.16.1  Code <Cd>
Presence: [1..1]
Definition: Processing position expressed as an ISO 20022 code.
Datatype: "ProcessingPosition3Code" on page 334
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 244 September 2025
```

