---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.4 InstructionProcessingStatus <InstrPrcgSts>", "6.4.4.5 Pending <Pdg>", "6.4.4.5.2 PendingReason <PdgRsn>"]
file_pages: [342]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.4.5.2 PendingReason <PdgRsn>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 342 to 342.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 342

```text
PendingQuantity <PdgQty> contains one of the following elements (see "Quantity51Choice" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C13 1091
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 1091
6.4.4.5.2  PendingReason <PdgRsn>
Presence: [1..1]
Definition: Reason for the pending status.
PendingReason <PdgRsn> contains one of the following PendingStatus80Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 342
Or}   Reason <Rsn> [1..*]  C6 342
     ReasonCode <RsnCd> [1..1]  343
{Or       Code <Cd> [1..1] CodeSet 343
Or}       Proprietary <Prtry> [1..1] ± 344
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 344
6.4.4.5.2.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Reason not specified.
Datatype: "NoReasonCode" on page 1223
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
6.4.4.5.2.2  Reason <Rsn>
Presence: [1..*]
Definition: Reason for the pending status.
Impacted by: C6 "AdditionalReasonInforrmationRule"
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 342 February 2026
```

