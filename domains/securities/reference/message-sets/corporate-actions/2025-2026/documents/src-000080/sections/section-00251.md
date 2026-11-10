---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.4 InstructionProcessingStatus <InstrPrcgSts>", "6.4.4.3 Forwarded <Fwdd>", "6.4.4.3.1 ForwardedQuantity <FwddQty>"]
file_pages: [336]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.4.3.1 ForwardedQuantity <FwddQty>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 336 to 336.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 336

```text
Forwarded <Fwdd> contains the following ForwardedStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ForwardedQuantity <FwddQty> [0..1] ± 336
   ForwardedReason <FwddRsn> [1..1] ± 336
6.4.4.3.1  ForwardedQuantity <FwddQty>
Presence: [0..1]
Definition: Quantity of instructed securities previously accepted has now been forwarded along the
chain.
ForwardedQuantity <FwddQty> contains one of the following elements (see "Quantity51Choice" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C13 1091
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 1091
6.4.4.3.2  ForwardedReason <FwddRsn>
Presence: [1..1]
Definition: Reason for the forwarded status.
ForwardedReason <FwddRsn> contains the following elements (see "NoSpecifiedReason1" on
page 1144 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1144
6.4.4.4  Rejected <Rjctd>
Presence: [1..1]
Definition: Status information related to an instruction request rejected for further processing due to
system reasons.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 336 February 2026
```

