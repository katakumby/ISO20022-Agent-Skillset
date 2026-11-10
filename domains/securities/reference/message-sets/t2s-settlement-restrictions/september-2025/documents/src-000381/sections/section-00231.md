---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.10 CancellationStatus15Choice", "9.1.21.10.2 Reason <Rsn>", "9.1.21.10.2.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [277]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.10.2.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 277 to 277.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 277

```text
Code <Cd> contains one of the following elements (see "CancellationReason21Choice" on page 285
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 285
Or}   Proprietary <Prtry> [1..1] ± 285
9.1.21.10.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 344
9.1.21.11  RejectionOrRepairStatus38Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 277
Or}   Reason <Rsn> [1..*]  277
     Code <Cd> [0..*]  278
{Or       Code <Cd> [1..1] CodeSet 278
Or}       Proprietary <Prtry> [1..1] ± 279
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 279
9.1.21.11.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
9.1.21.11.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the rejection or repair status.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 277 September 2025
```

