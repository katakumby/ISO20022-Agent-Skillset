---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "33.4 Message Building Blocks", "33.4.3 Reference <Ref>"]
file_pages: [812]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.010.001.07"]
---

# 33.4.3 Reference <Ref>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 812 to 812.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 812

```text
33.4.3 Reference <Ref>
Presence: [0..1]
Definition: Reference to the message or communication that was previously received.
Reference <Ref> contains one of the following elements (see "References64Choice" on page 4551 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   RelatedReference <RltdRef> [1..2] ± 4551
Or}   OtherReference <OthrRef> [1..2] ± 4551
33.4.4 StatusReport <StsRpt>
Presence: [1..1]
Definition: Status of the transfer cancellation instruction.
StatusReport <StsRpt> contains the following CancellationStatusAndReason5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MasterReference <MstrRef> [0..1] Text 812
   TransferReference <TrfRef> [1..1] Text 812
   ClientReference <ClntRef> [0..1] ± 813
   CancellationReference <CxlRef> [0..1] Text 813
   Status <Sts> [1..1]  813
{Or     Status <Sts> [1..1] ± 813
Or     Rejected <Rjctd> [1..1] ± 814
Or     Complete <Cmplt> [1..1] ± 814
Or}     Pending <Pdg> [1..1] ± 814
   StatusInitiator <StsInitr> [0..1] ± 814
33.4.4.1  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual transfers as assigned by the
instructing party. This identifier links the individual transfers together.
Datatype: "Max35Text" on page 5403
33.4.4.2  TransferReference <TrfRef>
Presence: [1..1]
Definition: Unique and unambiguous identification of the transfer, as assigned by the instructing party.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 sese.010.001.07
TransferCancellationStatusReportV07
Investment Funds - Maintenance 2025 - 2026 812 May 2026
```

