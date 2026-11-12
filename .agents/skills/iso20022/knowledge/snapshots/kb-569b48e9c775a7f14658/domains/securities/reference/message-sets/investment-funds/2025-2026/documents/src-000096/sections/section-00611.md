---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.1 MasterReference <MstrRef>"]
file_pages: [840]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.1 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 840 to 840.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 840

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       PreviousTax <PrvsTax> [0..1] Amount C1, C10 939
       StartDate <StartDt> [0..1] ± 939
       EndDate <EndDt> [0..1] ± 940
       AdditionalInformation <AddtlInf> [0..*] ± 940
     AdditionalInformation <AddtlInf> [0..*] ± 940
   QueryResponse <QryRspn> [0..*] Text 940
   StatusInitiator <StsInitr> [0..1] ± 940
   StatusIssuer <StsIssr> [0..1] ± 941
   StatusRecipient <StsRcpt> [0..1] ± 941
   AdditionalInformation <AddtlInf> [0..*] ± 941
Constraints
• ConversionRule
If at least one occurence of TransferEventType is ConversionStatus (CONV) then Conversion must
be present.
On Condition
    /TransferEventType[*]/Code is equal to value 'ConversionStatus'
Following Must be True
    /Conversion Must be present
• TransferStatusEventType1Rule
If at least one occurence of TransferEventType is Information (INFO) then TransferStatus/Status/
Status must be equal to Received (RECE).
On Condition
    /TransferEventType[*]/Code is equal to value 'Information'
Following Must be True
    /TransferStatus/Status/Status Must be equal to value 'Received'
• TransferStatusEventType2Rule
If at least one occurence of TransferEventType is ConversionStatus (CONV) then TransferStatus/
Status/Status must be equal to Received (RECE).
On Condition
    /TransferEventType[*]/Code is equal to value 'ConversionStatus'
Following Must be True
    /TransferStatus/Status/Status Must be equal to value 'Received'
34.4.4.1  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual transfers as assigned by the
instructing party. This identifier links the individual transfers together.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 840 May 2026
```

