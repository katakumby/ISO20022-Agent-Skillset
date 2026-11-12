---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.4 InstructionProcessingStatus <InstrPrcgSts>", "6.4.4.4 Rejected <Rjctd>", "6.4.4.4.1 RejectedQuantity <RjctdQty>"]
file_pages: [337]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.4.4.1 RejectedQuantity <RjctdQty>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 337 to 337.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 337

```text
Rejected <Rjctd> contains the following RejectedStatus15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RejectedQuantity <RjctdQty> [0..1] ± 337
   RejectedReason <RjctdRsn> [1..1]  337
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 337
Or}     Reason <Rsn> [1..*]  C5 338
       ReasonCode <RsnCd> [1..1]  338
{Or         Code <Cd> [1..1] CodeSet 338
Or}         Proprietary <Prtry> [1..1] ± 341
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 341
6.4.4.4.1  RejectedQuantity <RjctdQty>
Presence: [0..1]
Definition: Quantity of instructed securities for which processing is rejected.
RejectedQuantity <RjctdQty> contains one of the following elements (see "Quantity51Choice" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C13 1091
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 1091
6.4.4.4.2  RejectedReason <RjctdRsn>
Presence: [1..1]
Definition: Reason for the rejected status.
RejectedReason <RjctdRsn> contains one of the following RejectedStatus64Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 337
Or}   Reason <Rsn> [1..*]  C5 338
     ReasonCode <RsnCd> [1..1]  338
{Or       Code <Cd> [1..1] CodeSet 338
Or}       Proprietary <Prtry> [1..1] ± 341
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 341
6.4.4.4.2.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Reason not specified.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 337 February 2026
```

