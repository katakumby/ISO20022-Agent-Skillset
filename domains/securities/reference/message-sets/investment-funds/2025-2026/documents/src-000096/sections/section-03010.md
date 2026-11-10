---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "57.4 Message Building Blocks", "57.4.3 StatusReport <StsRpt>", "57.4.3.1 CancellationStatusReport <CxlStsRpt>", "57.4.3.1.2 CancellationStatus <CxlSts>", "57.4.3.1.2.2 Rejected <Rjctd>", "57.4.3.1.2.2.1 Reason <Rsn>", "57.4.3.1.2.2.1.1 Code <Cd>"]
file_pages: [4215]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.017.001.05"]
---

# 57.4.3.1.2.2.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4215 to 4215.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4215

```text
Reason <Rsn> contains one of the following RejectedReason66Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4215
Or}   Proprietary <Prtry> [1..1] ± 4215
57.4.3.1.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Rejected reason expressed as a code.
Datatype: "RejectedStatusReason14Code" on page 5354
CodeName Name Definition
ULNK UnknownLinkagesReference Linked reference is not known.
NSLA NotCompliantWithSLA Instruction is not compliant with the
service level agreement.
CUTO CutOffTime Instruction has been received after the
cut-off time.
NALC NotAllowedToCancel Instructing party is not allowed to request
a cancellation.
LEGL LegallyImpossible Legally impossible to cancel.
ADEA AfterDeadline Instruction was received after the
Receiver's deadline.
NRGM NoCancellationMatch The cancellation request has been
rejected since more than one instruction
match to the cancellation criteria.
57.4.3.1.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Rejected reason expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 4552 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
57.4.3.1.2.2.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the rejected reason.
Datatype: "Max350Text" on page 5403
Approved by the Securities SEG on 27 January 2026 setr.017.001.05 OrderCancellationStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4215 May 2026
```

