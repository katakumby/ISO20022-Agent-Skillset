---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.12 ProcessingStatus71Choice", "9.1.21.12.6 Completed <Cmpltd>"]
file_pages: [282]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.12.6 Completed <Cmpltd>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 282 to 282.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 282

```text
9.1.21.12.6  Completed <Cmpltd>
Presence: [1..1]
Definition: Modification request was completed.
Impacted by: C5 "AdditionalReasonInforrmationRule"
Completed <Cmpltd> contains the following elements (see "ProprietaryReason4" on page 272 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 273
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 273
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
9.1.21.12.7  Proprietary <Prtry>
Presence: [1..1]
Definition: Status that cannot be reported using one of the available standard status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on page 270
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 270
   ProprietaryReason <PrtryRsn> [0..*] ± C5 270
9.1.21.13  PendingStatus38Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 282
Or}   Reason <Rsn> [1..*]  283
     Code <Cd> [1..1] ± 283
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 283
9.1.21.13.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 331
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 282 September 2025
```

