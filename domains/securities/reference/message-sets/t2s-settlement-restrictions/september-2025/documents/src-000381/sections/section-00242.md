---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.18 DeniedStatus16Choice", "9.1.21.18.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [288]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.18.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 288 to 288.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 288

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 288
Or}   Reason <Rsn> [1..*]  288
     Code <Cd> [1..1] ± 288
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 288
9.1.21.18.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
9.1.21.18.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the denied status.
Reason <Rsn> contains the following DeniedReason11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 288
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 288
9.1.21.18.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the request has a denied status.
Code <Cd> contains one of the following elements (see "DeniedReason16Choice" on page 295 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 295
Or}   Proprietary <Prtry> [1..1] ± 296
9.1.21.18.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 344
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 288 September 2025
```

