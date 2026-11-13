---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.24 ModificationProcessingStatus9Choice", "9.1.21.24.2 Proprietary <Prtry>"]
file_pages: [293]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.24.2 Proprietary <Prtry>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 293 to 293.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 293

```text
9.1.21.24.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the status of a modification request.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 224 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
9.1.21.25  PendingStatus39Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 293
Or}   Reason <Rsn> [1..*]  293
     Code <Cd> [1..1] ± 293
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 294
9.1.21.25.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
9.1.21.25.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending status.
Reason <Rsn> contains the following PendingReason17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 293
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 294
9.1.21.25.2.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 293 September 2025
```

