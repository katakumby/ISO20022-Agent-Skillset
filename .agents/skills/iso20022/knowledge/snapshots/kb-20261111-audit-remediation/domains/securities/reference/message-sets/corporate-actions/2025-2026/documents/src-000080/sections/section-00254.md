---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.4 InstructionProcessingStatus <InstrPrcgSts>", "6.4.4.4 Rejected <Rjctd>", "6.4.4.4.2 RejectedReason <RjctdRsn>", "6.4.4.4.2.2 Reason <Rsn>", "6.4.4.4.2.2.1 ReasonCode <RsnCd>", "6.4.4.4.2.2.1.2 Proprietary <Prtry>"]
file_pages: [341]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.4.4.2.2.1.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 341 to 341.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 341

```text
CodeName Name Definition
DSEC InvalidSecurity Unrecognised or invalid financial
instrument identification.
6.4.4.4.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Rejection reason specified as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
6.4.4.4.2.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Additional information about the rejection status.
Datatype: "Max210Text" on page 1249
6.4.4.5  Pending <Pdg>
Presence: [1..1]
Definition: Status information related to a pending instruction.
Pending <Pdg> contains the following PendingStatus3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PendingQuantity <PdgQty> [0..1] ± 341
   PendingReason <PdgRsn> [1..1]  342
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 342
Or}     Reason <Rsn> [1..*]  C6 342
       ReasonCode <RsnCd> [1..1]  343
{Or         Code <Cd> [1..1] CodeSet 343
Or}         Proprietary <Prtry> [1..1] ± 344
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 344
6.4.4.5.1  PendingQuantity <PdgQty>
Presence: [0..1]
Definition: Quantity of instructed securities for which processing is pending.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 341 February 2026
```

