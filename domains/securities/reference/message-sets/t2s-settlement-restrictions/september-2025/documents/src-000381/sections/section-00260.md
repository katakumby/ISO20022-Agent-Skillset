---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.34 ProcessingStatus100Choice", "9.1.21.34.3 Cancelled <Canc>"]
file_pages: [306]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.34.3 Cancelled <Canc>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 306 to 306.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 306

```text
9.1.21.34.3  Cancelled <Canc>
Presence: [1..1]
Definition: Instruction has been cancelled. The status on the processing of a cancellation request must
be provided using a cancellation request report message.
Cancelled <Canc> contains one of the following elements (see "CancellationStatus14Choice" on
page 290 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 290
Or}   Reason <Rsn> [1..*] ± 290
9.1.21.34.4  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies a choice of status for the processing of an intra-balance movement.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on page 270
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 270
   ProprietaryReason <PrtryRsn> [0..*] ± C5 270
9.1.21.35  PendingReason34
Definition: Specifies the reason why the instruction or request has a pending status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  306
{Or     Code <Cd> [1..1] CodeSet 307
Or}     Proprietary <Prtry> [1..1] ± 307
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 307
9.1.21.35.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending status.
Code <Cd> contains one of the following PendingReason75Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 307
Or}   Proprietary <Prtry> [1..1] ± 307
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 306 September 2025
```

