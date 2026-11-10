---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["26 head.002.001.01 BusinessFileHeaderV01", "26.4 Message Building Blocks", "26.4.1 PayloadDescription <PyldDesc>", "26.4.1.1 PayloadData <PyldData>"]
file_pages: [616]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.002.001.01"]
---

# 26.4.1.1 PayloadData <PyldData>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 616 to 616.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 616

```text
PayloadDescription <PyldDesc> contains the following PayloadDescription2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PayloadData <PyldData> [1..1]  616
     PayloadIdentifier <PyldIdr> [1..1] Text 616
     CreationDateAndTime <CreDtAndTm> [1..1] DateTime 616
     PossibleDuplicateFlag <PssblDplctFlg> [0..1] Indicator 616
   ApplicationSpecifics <ApplSpcfcs> [0..1]  617
     SystemUser <SysUsr> [0..1] Text 617
     Signature <Sgntr> [0..1] (External Schema) 617
     TotalNumberOfDocuments <TtlNbOfDocs> [1..1] Quantity 617
   PayloadType <PyldTp> [1..1] Text 618
   ManifestData <MnfstData> [0..*]  618
     DocumentType <DocTp> [1..1] Text 618
     NumberOfDocuments <NbOfDocs> [1..1] Quantity 618
26.4.1.1  PayloadData <PyldData>
Presence: [1..1]
Definition: This component is used to identify the instance of the document exchanged.
PayloadData <PyldData> contains the following PayloadData2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PayloadIdentifier <PyldIdr> [1..1] Text 616
   CreationDateAndTime <CreDtAndTm> [1..1] DateTime 616
   PossibleDuplicateFlag <PssblDplctFlg> [0..1] Indicator 616
26.4.1.1.1  PayloadIdentifier <PyldIdr>
Presence: [1..1]
Definition: String of characters that uniquely identifies the file, which was delivered by the sender.
Datatype: "Max35Text" on page 3328
26.4.1.1.2  CreationDateAndTime <CreDtAndTm>
Presence: [1..1]
Definition: Date and time when the file was created by the sender.
Datatype: "ISODateTime" on page 3320
26.4.1.1.3  PossibleDuplicateFlag <PssblDplctFlg>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
head.002.001.01 BusinessFileHeaderV01
Target2-Securities 616 August 2026
```

