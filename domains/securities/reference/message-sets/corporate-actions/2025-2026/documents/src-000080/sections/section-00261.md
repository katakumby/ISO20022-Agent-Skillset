---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.4 InstructionProcessingStatus <InstrPrcgSts>", "6.4.4.8 StandingInstruction <StgInstr>"]
file_pages: [348]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.4.8 StandingInstruction <StgInstr>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 348 to 348.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 348

```text
6.4.4.8  StandingInstruction <StgInstr>
Presence: [1..1]
Definition: Standing instruction has been applied.
StandingInstruction <StgInstr> contains the following elements (see "NoSpecifiedReason1" on
page 1144 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1144
6.4.4.9  ReceivedByIssuerOrOfferor <RcvdByIssrOrOfferr>
Presence: [1..1]
Definition: Instruction has been received and accepted by the issuer or offeror.
ReceivedByIssuerOrOfferor <RcvdByIssrOrOfferr> contains the following
ReceivedByIssuerOrOfferorStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AcceptedByIssuerQuantity <AccptdByIssrQty> [0..1] ± 348
   ReceivedByIssuerOrOfferorReason
<RcvdByIssrOrOfferrRsn>
[1..1] ± 348
6.4.4.9.1  AcceptedByIssuerQuantity <AccptdByIssrQty>
Presence: [0..1]
Definition: Quantity of instructed securities previously accepted has now been accepted by the Issuer.
AcceptedByIssuerQuantity <AccptdByIssrQty> contains one of the following elements (see
"Quantity51Choice" on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C13 1091
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 1091
6.4.4.9.2  ReceivedByIssuerOrOfferorReason <RcvdByIssrOrOfferrRsn>
Presence: [1..1]
Definition: Reason for the pending status.
ReceivedByIssuerOrOfferorReason <RcvdByIssrOrOfferrRsn> contains the following elements
(see "NoSpecifiedReason1" on page 1144 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1144
6.4.4.10  ProprietaryStatus <PrtrySts>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 348 February 2026
```

