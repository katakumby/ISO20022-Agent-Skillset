---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.29 ProcessingStatus69Choice", "9.1.21.29.5 Proprietary <Prtry>"]
file_pages: [300]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.29.5 Proprietary <Prtry>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 300 to 300.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 300

```text
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus24Choice" on page 294 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 294
Or}   Reason <Rsn> [1..*]  294
     Code <Cd> [1..1] ± 295
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 295
9.1.21.29.5  Proprietary <Prtry>
Presence: [1..1]
Definition: Status that cannot be reported using one of the available standard status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on page 270
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 270
   ProprietaryReason <PrtryRsn> [0..*] ± C5 270
9.1.21.29.6  Denied <Dnd>
Presence: [1..1]
Definition: Instruction/Request will not be executed.
Denied <Dnd> contains one of the following elements (see "DeniedStatus16Choice" on page 287 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 288
Or}   Reason <Rsn> [1..*]  288
     Code <Cd> [1..1] ± 288
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 288
9.1.21.29.7  Cancelled <Canc>
Presence: [1..1]
Definition: Cancellation requested executed.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 300 September 2025
```

