---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.4 InstructionProcessingStatus <InstrPrcgSts>", "6.4.4.1 Cancelled <Canc>"]
file_pages: [335]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.4.1 Cancelled <Canc>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 335 to 335.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 335

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] ± 347
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 347
Or   DefaultAction <DfltActn> [1..1] ± 347
Or   StandingInstruction <StgInstr> [1..1] ± 348
Or   ReceivedByIssuerOrOfferor <RcvdByIssrOrOfferr> [1..1]  348
     AcceptedByIssuerQuantity <AccptdByIssrQty> [0..1] ± 348
     ReceivedByIssuerOrOfferorReason
<RcvdByIssrOrOfferrRsn>
[1..1] ± 348
Or}   ProprietaryStatus <PrtrySts> [1..1] ± 348
6.4.4.1  Cancelled <Canc>
Presence: [1..1]
Definition: Status and quantity information related to a cancelled instruction request.
Cancelled <Canc> contains the following elements (see "CancelledStatus5" on page 1140 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CancelledQuantity <CancQty> [0..1] ± 1140
   CancellationReason <CxlRsn> [1..1] ± 1140
6.4.4.2  AcceptedForFurtherProcessing <AccptdForFrthrPrcg>
Presence: [1..1]
Definition: Status information related to an instruction request that is accepted. This means that the
instruction has been received, is processable and has been validated for further processing.
AcceptedForFurtherProcessing <AccptdForFrthrPrcg> contains the following elements (see
"AcceptedStatus2" on page 1154 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AcceptedQuantity <AccptdQty> [0..1] ± 1154
   AcceptedReason <AccptdRsn> [1..1] ± 1154
6.4.4.3  Forwarded <Fwdd>
Presence: [1..1]
Definition: Instruction has been accepted and forwarded to the next intermediary in the chain.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 335 February 2026
```

