---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.4 InstructionProcessingStatus <InstrPrcgSts>"]
file_pages: [333, 334]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.4 InstructionProcessingStatus <InstrPrcgSts>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 333 to 334.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 333

```text
If Code is present, the code CHAN must only be used in case no other corporate action event code
is appropriate and only for an event which relates to a change.
If Code is present, the code REDM must only be used when the redemption is decided by the issuer
and not by the securities holders.
6.4.4 InstructionProcessingStatus <InstrPrcgSts>
Presence: [1..*]
Definition: Information about the processing status of the instruction.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 333 February 2026
```

## File page 334

```text
InstructionProcessingStatus <InstrPrcgSts> contains one of the following
InstructionProcessingStatus60Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Cancelled <Canc> [1..1] ± 335
Or   AcceptedForFurtherProcessing <AccptdForFrthrPrcg> [1..1] ± 335
Or   Forwarded <Fwdd> [1..1]  335
     ForwardedQuantity <FwddQty> [0..1] ± 336
     ForwardedReason <FwddRsn> [1..1] ± 336
Or   Rejected <Rjctd> [1..1]  336
     RejectedQuantity <RjctdQty> [0..1] ± 337
     RejectedReason <RjctdRsn> [1..1]  337
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 337
Or}       Reason <Rsn> [1..*]  C5 338
         ReasonCode <RsnCd> [1..1]  338
{Or           Code <Cd> [1..1] CodeSet 338
Or}           Proprietary <Prtry> [1..1] ± 341
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 341
Or   Pending <Pdg> [1..1]  341
     PendingQuantity <PdgQty> [0..1] ± 341
     PendingReason <PdgRsn> [1..1]  342
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 342
Or}       Reason <Rsn> [1..*]  C6 342
         ReasonCode <RsnCd> [1..1]  343
{Or           Code <Cd> [1..1] CodeSet 343
Or}           Proprietary <Prtry> [1..1] ± 344
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 344
Or   Returned <Rtrd> [1..1]  345
     ReturnedQuantity <RtrdQty> [0..1] ± 345
     ReturnedReason <RtrdRsn> [1..1]  345
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 346
Or}       Reason <Rsn> [1..*]  C7 346
         ReasonCode <RsnCd> [1..1]  346
{Or           Code <Cd> [1..1] CodeSet 347
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 334 February 2026
```

