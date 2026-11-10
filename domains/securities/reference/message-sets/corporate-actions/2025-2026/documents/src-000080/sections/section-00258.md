---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.4 InstructionProcessingStatus <InstrPrcgSts>", "6.4.4.6 Returned <Rtrd>"]
file_pages: [345]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.4.6 Returned <Rtrd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 345 to 345.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 345

```text
Datatype: "Max210Text" on page 1249
6.4.4.6  Returned <Rtrd>
Presence: [1..1]
Definition: Instructed units are returned or partially returned to the instructing party.
Returned <Rtrd> contains the following ReturnedStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReturnedQuantity <RtrdQty> [0..1] ± 345
   ReturnedReason <RtrdRsn> [1..1]  345
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 346
Or}     Reason <Rsn> [1..*]  C7 346
       ReasonCode <RsnCd> [1..1]  346
{Or         Code <Cd> [1..1] CodeSet 347
Or}         Proprietary <Prtry> [1..1] ± 347
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 347
6.4.4.6.1  ReturnedQuantity <RtrdQty>
Presence: [0..1]
Definition: Quantity of securities that have been returned.
ReturnedQuantity <RtrdQty> contains one of the following elements (see "Quantity51Choice" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C13 1091
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 1091
6.4.4.6.2  ReturnedReason <RtrdRsn>
Presence: [1..1]
Definition: Reason for the pending status.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 345 February 2026
```

